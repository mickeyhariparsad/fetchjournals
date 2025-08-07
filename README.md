# Logseq Journal Fetcher

This script fetches Logseq journal entries from a specified directory within a given date range and prints the consolidated content to standard output.

## Description

The script iterates through all dates between a provided start and end date. For each date, it looks for a corresponding `.md` file in the format `YYYY_MM_DD.md` inside the specified journal directory.

The contents of all found journal files are then printed to the console.

## Usage

To use the script, you must provide a start and end date. You can then redirect the script's output to a file of your choice.

```bash
python fetch_journals.py <start_date> <end_date> [--journal-dir <directory>] > <output_file>
```

### Example

To fetch journals from January 1st, 2023 to January 31st, 2023, from a directory named `journals`, and save the result to `Output.txt`, you would run:

```bash
python fetch_journals.py 2023-01-01 2023-01-31 --journal-dir ./journals > Output.txt
```
