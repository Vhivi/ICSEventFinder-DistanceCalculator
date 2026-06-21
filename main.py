from datetime import date, datetime, time, timezone

from icalendar import Calendar

SEARCH_TERM = "your_search_term"
START_TIME = datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
END_TIME = datetime(2025, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
ROUNDTRIP = 31.4 * 2
DISTANCE_UNIT = "km"


def open_file():
    with open("calendar.ics", "rb") as f:
        return Calendar.from_ical(f.read())


def as_datetime(value):
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    if isinstance(value, date):
        return datetime.combine(value, time.min, tzinfo=timezone.utc)
    return None


def get_events(cal):
    matching_events = []
    for component in cal.walk():
        if component.name == "VEVENT":
            dtstart = as_datetime(component.get("dtstart").dt)
            dtend = as_datetime(component.get("dtend").dt)
            summary = str(component.get("summary") or "")
            if not dtstart or not dtend:
                continue
            if dtstart > END_TIME or dtend < START_TIME:
                continue
            if SEARCH_TERM.lower() not in summary.lower():
                continue
            matching_events.append((dtstart, component))

    return matching_events


def main():
    cal = open_file()
    matching_events = sorted(get_events(cal), key=lambda x: x[0])
    total_distance = len(matching_events) * ROUNDTRIP

    print(f"Total events found: {len(matching_events)}")
    print(f"Total distance: {total_distance} {DISTANCE_UNIT}")


if __name__ == "__main__":
    main()
