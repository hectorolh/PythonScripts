#This script reads a log file line by line and uses a regular expression to extract the IP address and date from each entry. 
#It keeps track of the number of requests from each IP address for each day. If it finds an IP address that has made more than 
#100 requests in a single day, it prints out a message with the IP address and date.

import re
from collections import defaultdict

def analyze_logs(filename):
    with open(filename, 'r') as f:
        logs = f.readlines()

    ip_requests = defaultdict(int)
    current_date = None

    for log in logs:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+) - .+ \[(\d+/\w+/\d+):', log)
        if match:
            ip, date = match.groups()
            if date != current_date:
                ip_requests = defaultdict(int)
                current_date = date
            ip_requests[ip] += 1

            if ip_requests[ip] > 100:
                print(f"IP address {ip} has made more than 100 requests on {current_date}")

analyze_logs('logfile.txt')
