# Generates a log file with 1000 entries and format: Date time src_ip dest_ip src_port dest_port protocol

import random
import time

# List of sample IP addresses
ip_addresses = ['192.168.1.' + str(i) for i in range(1, 101)]

with open('log_file.txt', 'w') as f:
    for _ in range(1000):
        src_ip = random.choice(ip_addresses)
        dest_ip = random.choice(ip_addresses)
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(random.randint(1609459200, 1640995200)))  # Random timestamp in 2021
        src_port = random.randint(1, 65535)
        dest_port = random.randint(1, 65535)
        protocol = random.choice(['TCP', 'UDP'])
        
        f.write(f"{timestamp} {src_ip} {dest_ip} {src_port} {dest_port} {protocol}\n")\
