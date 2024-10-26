
#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics based on input.
It processes lines in the format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import sys

# Initialize counters
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    """Function to print the computed metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        try:
            # Split the line and extract required fields
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Increment line count and print every 10 lines
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()

        except (ValueError, IndexError):
            # Skip lines that don't match the format
            continue

except KeyboardInterrupt:
    # Print metrics when interrupted by CTRL + C
    print_metrics()
    raise

finally:
    # Ensure metrics are printed at the end
    print_metrics()
