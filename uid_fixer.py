#!/usr/bin/env python3
"""
uid_fixer.py
============

Replace every VEVENT UID in an iCalendar (.ics) file with a new,
globally-unique value.  Line-folding is handled automatically by the
`icalendar` library.

Usage
-----

# rewrite in-place
python uid_fixer.py calendar.ics --in-place

# or write to a new file
python uid_fixer.py calendar.ics fixed.ics

Options
-------

--domain  Domain to append to the UUID part (default: 'modified.local')
"""

from __future__ import annotations
import argparse
import uuid
from pathlib import Path
from icalendar import Calendar

def _replace_uids(cal: Calendar, domain: str) -> Calendar:
    """Return *cal* with new UIDs for every VEVENT."""
    for component in cal.walk():
        if component.name == "VEVENT":
            component["UID"] = f"{uuid.uuid4()}@{domain}"
    return cal


def main() -> None:
    parser = argparse.ArgumentParser(description="Rewrite VEVENT UIDs")
    parser.add_argument("ics_file", help="Input .ics path")
    parser.add_argument(
        "output", nargs="?", help="Output path (omit for STDOUT)"
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the input file in place",
    )
    parser.add_argument(
        "--domain",
        default="modified.local",
        help="Domain suffix to append to each UID",
    )
    args = parser.parse_args()

    raw = Path(args.ics_file).read_bytes()
    cal = Calendar.from_ical(raw)
    cal = _replace_uids(cal, args.domain)
    serialized = cal.to_ical()

    if args.in_place:
        Path(args.ics_file).write_bytes(serialized)
    elif args.output:
        Path(args.output).write_bytes(serialized)
    else:
        # Allow piping to another process
        print(serialized.decode())


if __name__ == "__main__":
    main()
