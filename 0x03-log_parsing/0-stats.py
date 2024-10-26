#!/usr/bin/python3
"""Script to parse logs and compute metrics based on a specific format:

- Expected format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
- Every 10 lines or upon a keyboard interrupt (CTRL + C), prints:
    - Total file size across lines
    - Count of each valid status code (200, 301, 400, 401, 403, 404, 405, 500) in ascending order
"""

import sys

# Dictionary to count occurrences of each valid status code
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # Counts the number of lines processed in each batch

def print_stats():
    """Prints the accumulated file size and count of each status code."""
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes_dict.items()):
        if value > 0:
            print(f"{key}: {value}")

try:
    for line in sys.stdin:
        line_list = line.split()

        # Check if the line contains the expected number of elements
        if len(line_list) >= 7:
            try:
                # Parse status code and file size
                status_code = line_list[-2]
                file_size = int(line_list[-1])

                # Update status code count if it's a valid one
                if status_code in status_codes_dict:
                    status_codes_dict[status_code] += 1

                # Update total file size
                total_size += file_size
                count += 1

                # Print metrics every 10 lines
                if count == 10:
                    print_stats()
                    count = 0  # Reset line count for the next batch

            except (ValueError, IndexError):
                # Skip line if file_size or status_code is not as expected
                continue

except KeyboardInterrupt:
    # Print final stats upon keyboard interruption
    print_stats()
    raise

finally:
    # Ensure final stats are printed if loop ends normally
    print_stats()