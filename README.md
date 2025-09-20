# UID Fixer

A simple Python tool to fix UID conflicts in iCalendar (.ics) files by replacing all VEVENT UIDs with new, globally-unique values.

## Problem Solved

This tool addresses calendar import issues where duplicate or conflicting UIDs prevent successful calendar imports. Common scenarios include:

- **Nextcloud Calendar Import Errors**: When importing calendars into Nextcloud, duplicate UIDs can cause import failures
- **Google Calendar Import Issues**: Events with conflicting UIDs may fail to import with "insufficient access" errors
- **General Calendar Synchronization Problems**: UID conflicts between different calendar systems

## What It Does

The UID Fixer tool:

1. **Reads** iCalendar (.ics) files
2. **Identifies** all VEVENT components (calendar events)
3. **Replaces** each UID with a new UUID4-based globally unique identifier
4. **Preserves** all other event data and calendar structure
5. **Outputs** the fixed calendar file

## Installation

### Prerequisites
- Python 3.6 or higher
- `icalendar` library

### Install Dependencies
```bash
pip install icalendar
```

## Usage

### Basic Usage
```bash
# Fix UIDs and write to a new file
python uid_fixer.py input.ics output.ics

# Fix UIDs and output to STDOUT (for piping)
python uid_fixer.py input.ics

# Fix UIDs in-place (overwrites original file)
python uid_fixer.py input.ics --in-place
```

### Advanced Options
```bash
# Use custom domain suffix for UIDs (default: modified.local)
python uid_fixer.py input.ics output.ics --domain example.com
```

### Examples
```bash
# Fix a Google Calendar export before importing to Nextcloud
python uid_fixer.py google-calendar.ics fixed-calendar.ics

# Process multiple files with custom domain
python uid_fixer.py calendar1.ics fixed1.ics --domain mycompany.local
python uid_fixer.py calendar2.ics fixed2.ics --domain mycompany.local

# Pipeline processing
python uid_fixer.py input.ics | some-other-calendar-processor
```

## How It Works

The tool uses the `icalendar` library to:
1. Parse the input .ics file
2. Walk through all calendar components
3. For each VEVENT component, generate a new UID in the format: `{uuid4}@{domain}`
4. Serialize the modified calendar back to .ics format

Line-folding and other iCalendar formatting requirements are handled automatically by the `icalendar` library.

## Related Issues

This tool was created to solve the following documented problems:

- [Nextcloud Server Issue #53262](https://github.com/nextcloud/server/issues/53262) - Calendar import failures due to UID conflicts
- [Google Calendar Import Errors](https://martcj.wordpress.com/2014/02/27/error-importing-a-google-calendar-failed-to-import-events-could-not-upload-your-events-because-you-do-not-have-sufficient-access-on-the-target-calendar/) - "Insufficient access" errors during calendar imports

## License

This project is open source. Please check the repository for license details.
