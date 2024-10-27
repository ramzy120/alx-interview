#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

def generate_log_entry():
    """Generate a single log entry."""
    ip_parts = [
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
    ]
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    content_length = random.randint(1, 1024)
    current_time = datetime.datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")

    log_entry = (
        '{:d}.{:d}.{:d}.{:d} - [{}] "GET /projects/260 HTTP/1.1" {} {}'
    ).format(
        ip_parts[0],
        ip_parts[1],
        ip_parts[2],
        ip_parts[3],
        current_time,
        status_code,
        content_length,
    )
    
    return log_entry

if __name__ == "__main__":
    for _ in range(10000):  # Generate 10,000 log entries
        log_entry = generate_log_entry()
        print(log_entry)  # Use print instead of sys.stdout.write
        sleep(random.random())  # Sleep for a random time to simulate log generation speed