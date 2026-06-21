from datetime import datetime, timezone

from icalendar import Calendar

SEARCH_TERM = "your_search_term"
START_TIME = datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
END_TIME = datetime(2025, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
ROUNDTRIP = 31.4 * 2
DISTANCE_UNIT = "km"


def open_file():
    """Opens the file and returns the calendar object."""
    with open("calendar.ics", "rb") as f:
        return Calendar.from_ical(f.read())


def get_events(cal):
    """Returns a list of events that match the search term."""
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


def main():
    cal = open_file()
    matching_events = sorted(get_events(cal), key=lambda x: x.get("dtstart").dt)
    total_distance = len(matching_events) * ROUNDTRIP

    print(f"Total events found: {len(matching_events)}")
    print(f"Total distance: {total_distance} {DISTANCE_UNIT}")


if __name__ == "__main__":
    main()
