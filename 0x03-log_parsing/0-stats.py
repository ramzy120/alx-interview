#!/usr/bin/python3
import sys
import signal

# Global variables to store metrics
total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0

def print_stats():
    """Prints the current statistics."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        if status_codes_count[status_code] > 0:
            print(f"{status_code}: {status_codes_count[status_code]}")

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            # Increment the line count
            line_count += 1

            # Parse the line
            parts = line.split()
            if len(parts) != 9:
                continue  # Skip lines that do not match the format

            # Extract the relevant parts
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
            except ValueError:
                continue  # Skip lines with invalid integers

            # Update the total file size
            total_file_size += file_size

            # Update the count for the status code
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)