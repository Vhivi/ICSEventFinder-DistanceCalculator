# /usr/bin/python
# -*- coding: utf-8 -*-

# Project Description: This project consists of creating a Python program that
# allows you to search for events in a previously retrieved *.ics file.
# The *.ics file contains calendar data in iCalendar format, such as events
# with their title, description, start date and time, end date and time, etc.
# Then, the program will display the events found in the *.ics file, their
# number, and calculate the distance traveled during the period of the found
# events.
# Author:
# Creation Date (dd/mm/yyyy): 31/03/2024
# Version:
# Python 3.10.11

################################################################
# Module Imports
################################################################

from datetime import datetime, timezone

from icalendar import Calendar

################################################################
# Global Variable Declarations
################################################################

# Replace your_search_term with the term complete or not, you want to search
# for in the summary of the events
SEARCH_TERM = "your_search_term"
# Replace the dates (yyyy, mm, dd, hh, mm, ss) with the desired start and end
START_TIME = datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
END_TIME = datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
# Replace the number between the parentheses with the one-way distance for the
# roundtrip you want to calculate no matter the unit
ROUNDTRIP = (32.7) * 2
# Replace by the unit of the distance you want to calculate (km, miles, etc.)
DISTANCE_UNIT = "km"

################################################################
# Function Declarations
################################################################


def open_file():
    """
    Opens and reads the 'calendar.ics' file, and returns a calendar object.

    Returns:
        cal (Calendar): A calendar object representing the contents of the 'calendar.ics' file.
    """
    # Open the file
    with open("calendar.ics", "rb") as f:
        # Create a calendar object
        cal = Calendar.from_ical(f.read())

    return cal


def get_events(cal):
    """
    Retrieve a list of events from a calendar that match the specified criteria.

    Args:
        cal (Calendar): The calendar object to search for events.

    Returns:
        list: A list of matching events.

    """
    # Search for the events
    matching_events = []
    for component in cal.walk():
        if component.name == "VEVENT":
            dtstart = component.get("dtstart").dt
            dtend = component.get("dtend").dt
            summary = component.get("summary")
            try:
                if dtstart <= END_TIME and dtend >= START_TIME:
                    if SEARCH_TERM.lower() in summary.lower():
                        matching_events.append(component)
            except TypeError:
                pass

    return matching_events


def sort_events(matching_events):
    """
    Sorts a list of events based on their start date.

    Args:
        matching_events (list): A list of events to be sorted.

    Returns:
        list: The sorted list of events.
    """
    # Sort the events by start date
    matching_events.sort(key=lambda x: x.get("dtstart").dt)

    return matching_events


def main():
    """
    This is the main function that performs the following tasks:
    1. Opens a file.
    2. Retrieves events from the file.
    3. Sorts the events.
    4. Prints the sorted events.
    5. Calculates and prints the total number of events found. (Print only for testing purposes or verification)
    6. Calculates and prints the total distance based on the number of events.

    Parameters:
    None

    Returns:
    None
    """
    cal = open_file()

    matching_events = sort_events(get_events(cal))

    # Print the results for testing
    # for event in matching_events:
    #     print(f'{event.get("dtstart").dt} - {event.get("dtend").dt} - {event.get("summary")}')

    print(f"Total events found: {len(matching_events)}")

    # Multiple events by the round trip to obtain the total distance
    total_distance = len(matching_events) * ROUNDTRIP
    print(f"Total distance: {total_distance} {DISTANCE_UNIT}")


if __name__ == "__main__":
    main()
