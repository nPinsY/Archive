# EasiCalendar

#### Video Demo: [https://youtu.be/hkp0Qy51uLY]

#### Description:
This application streamlines the process of scheduling recurring events on Google Calendar, such as workouts, study sessions, work commitments, meals, and more. These events often recur weekly or daily but may vary in their start times. For instance, a Yoga class might always last an hour and be associated with a specific color like green. This program enables users to efficiently manage such recurring events with minimal input.

The core functionality lies in its ability to set 'Set Events'. Users can define a recurring event by specifying its name, duration, color, and other attributes. Once a 'Set Event' is created, scheduling it on Google Calendar becomes a matter of providing just a keyword and a start time. The application then automatically populates the calendar with the event, applying the pre-defined duration and color.

This feature is particularly useful for activities that follow a regular pattern but may start at different times. By eliminating the need to input repetitive information for each occurrence, this application significantly reduces the time and effort involved in calendar management. It caters especially to those who have a routine but flexible schedule, making it an ideal tool for personal time management and organization.

## Overview
The application acts as an intermediary between the user and their Google Calendar, facilitating the addition of recurring events. It leverages the Google Calendar API for calendar interactions and offers an intuitive interface for various calendar operations.

## Features
- **Create Event**: Add new events directly to your Google Calendar.
- **Create Set Event**: Define and store event templates (Set Events) for quick access and reuse.
- **Update Set Event**: Modify existing Set Events.
- **Delete Set Event**: Remove Set Events from the local storage.

## Setup and Installation
To successfully set up and use this project, follow these steps:

1. **Clone the Repository**: Start by cloning the project repository to your local machine.

2. **Install Dependencies**: Install the necessary Python libraries listed in the `requirements.txt` file. You can do this by running `pip install -r requirements.txt` in your project directory.

3. **Google Calendar API Setup**:
    - Visit the [Google Developers Console](https://console.developers.google.com/).
    - Create a new project or select an existing one.
    - Navigate to the "Library" section and enable the Google Calendar API for your project.
    - In the "Credentials" section, create credentials for an OAuth 2.0 client ID. Select 'Desktop app' as the application type.
    - Once created, download the JSON file containing your credentials.
    
4. **Place Credentials File**: Rename the downloaded JSON file to `credentials.json` and place it in the root directory of the project. This file is essential for the application to authenticate with Google Calendar.

5. **Run the Application**: With the dependencies installed and the credentials file in place, you're ready to run the application. Execute it from your command line or terminal, and follow the on-screen prompts to manage your Google Calendar events.

### Requirements
- Python 3.x
- Google Calendar API
- Additional libraries as specified in `requirements.txt`.

Remember, the `credentials.json` file is crucial for the application to interact with Google Calendar. Ensure it's correctly placed in the project directory before running the application.

## Usage
Execute the application and follow the interactive prompts to manage events and Set Events on your Google Calendar.

## Design Choices
Emphasis is placed on simplicity and user-friendliness. Managing Set Events locally, as opposed to directly on Google Calendar, offers greater flexibility and control over frequently used event templates.

## Additional Notes
This application forms a part of a broader initiative aimed at enhancing productivity and efficiency in calendar management for users. Updates will come for this in the future.