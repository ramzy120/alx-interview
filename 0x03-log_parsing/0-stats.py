#!/usr/bin/python3
import sys

# Initialize variables to store total file size and status code counts
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the current statistics."""
    print("File size:", total_file_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    # Read each line from standard input
    for line in sys.stdin:
        line_count += 1

        # Split and parse each line according to the expected format
        parts = line.split()
        if len(parts) < 7:
            continue  # Skip lines not matching the format

        # Extract and update file size
        try:
            file_size = int(parts[-1])
            total_file_size += file_size
        except ValueError:
            continue  # Skip if file size is not an integer

        # Extract and update status code count
        try:
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except ValueError:
            continue  # Skip if status code is not an integer

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interruption
    print_stats()
    raise

# Print final stats after all lines are processed
print_stats()
