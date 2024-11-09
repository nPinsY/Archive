import project

# Test for calculate_event_times
def test_calculate_event_times_valid_input():
    set_event = {"duration": "01:00"}
    start_time, end_time = project.calculate_event_times("2023-01-01 10:00", set_event)

    # Assert start and end times are correctly calculated
    assert start_time == "2023-01-01T10:00:00"
    assert end_time == "2023-01-01T11:00:00"

# Test for calculate_event_times with invalid input
def date():
    set_event = {"duration": "01:00"}
    start_time, end_time = project.calculate_event_times("invalid date", set_event)

    # Assert that invalid time input returns None
    assert start_time is None and end_time is None

def test_get_credentials():
    creds = project.get_credentials()
    assert creds is not None, "Failed to retrieve credentials"

def test_save_set_event():
    test_event = {'name': 'Test Event', 'description': 'Test Description', 'color_id': '1', 'duration': '01:00'}
    project.save_set_event(test_event)

    # Check if the event is saved correctly
    events = project.read_csv(project.SET_EVENTS_FILE)
    assert any(event['name'] == 'Test Event' for event in events), "Event not saved correctly"

def test_delete_csv_set_event():
    test_event_name = 'Test Event'
    project.delete_csv_set_event(test_event_name)

    # Check if the event is deleted
    events = project.read_csv(project.SET_EVENTS_FILE)
    assert not any(event['name'] == test_event_name for event in events), "Event not deleted correctly"
