import os
import argparse
import sys
from datetime import datetime, timedelta

def fetch_journals(journal_dir, start_date_str, end_date_str):
    """
    Fetches Logseq journals for a particular time period and prints them to stdout.
    """
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(journal_dir):
        print(f"Error: Journal directory not found at '{journal_dir}'", file=sys.stderr)
        sys.exit(1)

    all_content = []
    current_date = start_date
    while current_date <= end_date:
        filename = current_date.strftime("%Y_%m_%d.md")
        filepath = os.path.join(journal_dir, filename)

        if os.path.exists(filepath):
            date_header = current_date.strftime("## %Y-%m-%d\n")
            all_content.append(date_header)
            with open(filepath, 'r', encoding='utf-8') as f:
                all_content.append(f.read())
            all_content.append("\n\n")

        current_date += timedelta(days=1)

    if not all_content:
        print("No journal entries found for the given date range.", file=sys.stderr)
        sys.exit(0)

    for content in all_content:
        print(content, end='')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch Logseq journals for a given period and print to stdout.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n  python fetch_journals.py 2023-01-01 2023-01-31 --journal-dir ./my-journals > Output.txt"
    )
    parser.add_argument("start_date", help="Start date in YYYY-MM-DD format.")
    parser.add_argument("end_date", help="End date in YYYY-MM-DD format.")
    parser.add_argument("--journal-dir", default="journals", help="Directory containing journal files. Defaults to './journals'.")

    args = parser.parse_args()

    fetch_journals(args.journal_dir, args.start_date, args.end_date)
