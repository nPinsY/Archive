import csv
import datetime
import os
from dateutil import tz, parser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tabulate import tabulate

# Constants
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SET_EVENTS_FILE = 'set_events.csv'
TIMEZONE = 'America/New_York'  # Fixed timezone
COLORS = {
    'blue': '1', 'green': '2', 'purple': '3', 'red': '4',
    'yellow': '5', 'orange': '6', 'turquoise': '7', 'gray': '8',
    'bold blue': '9', 'bold green': '10', 'bold red': '11'
}
COLORS_REVERSE = {v: k for k, v in COLORS.items()}

# Exception Handling Decorator
def handle_file_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as e:
            print(f"An I/O error occurred: {e}")
        except FileNotFoundError:
            print(f"File not found error.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return wrapper

# Main Function
def main():
    service = initialize_calendar_service()
    display_next_events(service, 5)

    while True:
        print("\nChoose an option:\n1. Create Google Calendar Event\n2. Create Set Event\n3. Update Set Event\n4. Delete Set Event\n5. Exit")
        choice = input("\nYour choice: ").strip().lower()
        if choice in ['1', 'Create Google Calendar Event']:
            create_event(service)
        elif choice in ['2', 'create set event']:
            create_set_event()
        elif choice in ['3', 'update set event']:
            update_set_event()
        elif choice in ['4', 'delete set event']:
            delete_set_event()
        elif choice in ['5', 'exit']:
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize Google Calendar Service
def initialize_calendar_service():
    creds = get_credentials()
    try:
        return build("calendar", "v3", credentials=creds)
    except HttpError as error:
        print(f"An error occurred: {error}")
        exit()

# Credential Handling
def get_credentials():
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

# Display Next Events
def display_next_events(service, count):
    now = datetime.datetime.now(tz.gettz(TIMEZONE)).isoformat()
    try:
        events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=count, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print("No upcoming events found.")
        else:
            table_data = [[event['summary'], event['start'].get('dateTime', event['start'].get('date')), event['end'].get('dateTime', event['end'].get('date')), event.get('location', 'No location')] for event in events]
            print(f"\n{tabulate(table_data, headers=['Event', 'Start', 'End', 'Location'])}\n")
    except HttpError as error:
        print(f"An error occurred while retrieving events: {error}")

# Create_set_event function
def create_set_event():
    event_name = get_input("Enter event name (or type 'Exit' to return): ")
    if event_name.lower() == 'exit' or event_exists(event_name):
        return

    description = get_input("Enter event description: ")
    color_id = get_color_id()  # Corrected function call
    duration = get_duration()
    save_set_event({'name': event_name, 'description': description, 'color_id': color_id, 'duration': duration})
    print(f"Set Event '{event_name}' created.")

# Create Event
def create_event(service):
    event_name = input("Enter Set Event name (or type 'Exit' to return): ").strip()
    if event_name.lower() == 'exit':
        return

    set_event = get_set_event(event_name)
    if not set_event:
        print("Set Event not found. Please try again.")
        return

    start_input = input("Enter start time (any format): ")
    start_time, end_time = calculate_event_times(start_input, set_event)

    if not start_time or not end_time:
        print("Invalid time input.")
        return  # Return to main menu

    event = build_event(set_event, start_time, end_time)
    try:
        created_event = service.events().insert(calendarId="primary", body=event).execute()
        print("Event created: %s" % (created_event.get("htmlLink")))
    except HttpError as error:
        print(f"An error occurred: {error}")

# Save_set_event function
@handle_file_exceptions
def save_set_event(event_data):
    events = read_csv(SET_EVENTS_FILE)
    events.append(event_data)
    write_csv(SET_EVENTS_FILE, events, ['name', 'description', 'color_id', 'duration'])

# Calculate Event Times
def calculate_event_times(start_input, set_event):
    try:
        start_time = parser.parse(start_input, fuzzy=True)
        duration_hours, duration_minutes = [int(part) for part in set_event['duration'].split(':')]
        end_time = start_time + datetime.timedelta(hours=duration_hours, minutes=duration_minutes)
        return start_time.isoformat(), end_time.isoformat()
    except (ValueError, OverflowError) as e:
        print(f"Invalid date/time input: {start_input}. Please try again in a different format. Error: {e}")
        return None, None

# Build Event for Google Calendar
def build_event(set_event, start_time, end_time):
    return {
        "summary": set_event['name'],
        "description": set_event['description'],
        "start": {"dateTime": start_time, "timeZone": TIMEZONE},
        "end": {"dateTime": end_time, "timeZone": TIMEZONE},
        "colorId": set_event['color_id']
    }

# Update Set Event in CSV
@handle_file_exceptions
def update_csv_set_event(updated_event, original_name):
    events = read_csv(SET_EVENTS_FILE)
    for event in events:
        if event['name'].lower() == original_name.lower():
            event.update(updated_event)
    write_csv(SET_EVENTS_FILE, events, ['name', 'description', 'color_id', 'duration'])

@handle_file_exceptions
def delete_csv_set_event(event_name):
    events = read_csv(SET_EVENTS_FILE)
    events = [event for event in events if event['name'].lower() != event_name.lower()]
    write_csv(SET_EVENTS_FILE, events, ['name', 'description', 'color_id', 'duration'])


# Update Set Event
@handle_file_exceptions
def update_set_event():
    list_set_events()
    event_name = input("Enter the Set Event name to update (or type 'Exit' to return): ").strip()
    if event_name.lower() == 'exit':
        return

    if not event_exists(event_name):
        print(f"Set Event '{event_name}' not found. Please try again.")
        return

    field_choice = input("\nSelect the field to update:\n1. Name\n2. Description\n3. Color\n4. Duration\n\nEnter your choice: ").strip()
    if field_choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a number between 1 and 4.")
        return

    updated_event = get_updated_event_data(event_name, field_choice)
    if updated_event:
        update_csv_set_event(updated_event, event_name)
        print(f"Set Event '{event_name}' updated.")

# Delete Set Event
def delete_set_event():
    if not list_set_events():
        return  # Return to main menu

    event_name = input("Enter the Set Event name to delete (or type 'Exit' to return): ").strip()
    if event_name.lower() == 'exit':
        return

    if not event_exists(event_name):
        print("Set Event not found. Please try again.")
        return

    confirm = input(f"Are you sure you want to delete '{event_name}'? (yes/no): ").strip().lower()
    if confirm not in ['yes', 'y']:
        print("Deletion cancelled.")
        return

    delete_csv_set_event(event_name)
    print(f"Set Event '{event_name}' deleted.")

# Get Duration
def get_duration():
    while True:
        duration_input = input("Enter duration (HH:MM): ").strip()
        try:
            hours, minutes = [int(part) for part in duration_input.split(":")]
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return f"{hours:02d}:{minutes:02d}"
            else:
                print("Invalid duration. Hours must be between 0-23 and minutes between 0-59.")
        except ValueError:
            print("Invalid duration format. Please enter in HH:MM format.")

@handle_file_exceptions
def get_set_event(event_name):
    events = read_csv(SET_EVENTS_FILE)
    for event in events:
        if event['name'].lower() == event_name.lower():
            return event
    return None

# Get Set Event Details
def get_set_event_details():
    description = input("Enter event description: ").strip()
    color_id = get_color_id()
    duration = get_duration()
    return description, color_id, duration

# Get Updated Event Data
def get_updated_event_data(event_name, field_choice):
    event = get_set_event(event_name)
    if not event:
        print(f"Event named '{event_name}' not found.")
        return None

    if field_choice == '1':  # Update Name
        new_name = input("Enter new name: ").strip()
        if event_exists(new_name):
            print(f"An event with the name '{new_name}' already exists.")
            return None
        event['name'] = new_name

    elif field_choice == '2':  # Update Description
        new_description = input("Enter new description: ").strip()
        event['description'] = new_description

    elif field_choice == '3':  # Update Color
        new_color_id = get_color_id()
        event['color_id'] = new_color_id

    elif field_choice == '4':  # Update Duration
        new_duration = get_duration()
        event['duration'] = new_duration

    return event

# Check if Event Exists
@handle_file_exceptions
def event_exists(event_name):
    try:
        with open(SET_EVENTS_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return any(row['name'].lower() == event_name.lower() for row in reader)
    except FileNotFoundError:
        return False

# List Set Events
@handle_file_exceptions
def list_set_events():
    events = read_csv(SET_EVENTS_FILE)
    if not events:
        print("No set events to display.")
        return False
    else:
        table_data = [[event['name'], event['description'], COLORS_REVERSE.get(event['color_id'], 'Unknown'), event['duration']] for event in events]
        print(f"\n{tabulate(table_data, headers=['Name', 'Description', 'Color', 'Duration'])}\n")
        return True

# CSV Utility Functions
def read_csv(file_name):
    try:
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return []

def write_csv(file_name, data, fieldnames):
    try:
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


# Input Validation Functions
def get_input(prompt, validation=None):
    while True:
        user_input = input(prompt).strip()
        if validation and not validation(user_input):
            print("Invalid input. Please try again.")
            continue
        return user_input

def validate_color(color):
    return color.lower() in COLORS

# Color Mapping Function
def get_color_id():
    color_name = get_input(f"Enter color name ({', '.join(COLORS.keys()).title()}): ", validate_color)
    return COLORS[color_name.lower()]

if __name__ == "__main__":
    main()
