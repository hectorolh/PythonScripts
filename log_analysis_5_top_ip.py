"""
script that reads a log file and identifies the top 5 IP addresses with the
most connections. The script should also counts the number of unique destination 
IPs each source IP is connected to.
"""
from collections import defaultdict

# ask the user for the log file location.
log_file = input ("Please enter the path to your log file: ")


# create a function to analyze the log files.
def analyze_logs(log_file): #reading the log file and analyzing the data. It takes one argument.
    connections = defaultdict(lambda: defaultdict(set))  # create a nested dictionary named connections. This will store each source IP and its corresponding destination IPs.

    with open(log_file,'r') as file: #open the log file and read it line by line.
        for line in file:
            _, _, src_ip, dest_ip, _, _, _ = line.strip().split() # Parse,for each line, extract the source IP and destination IP.
            connections[src_ip][dest_ip].add(dest_ip) # update the connections dictionary with the information.

# sort the dictionary based on the number of destination IPs each source IP is connected to. 
     # Create a list of tuples where each tuple is (src_ip, number of unique dest_ips)
    ip_counts = [(src_ip, len(dest_ips)) for src_ip, dest_ips in connections.items()]
# Gets all the items in the dictionary, it loops through it and sets the src_ip as a source ip and dest_ips is a disctionary of destination IP.abs

    # Sort the list in descending order based on the number of unique dest_ips
    ip_counts.sort(key=lambda x: x[1], reverse=True)

    # Get the top 5
    top_ips = ip_counts[:5]

# Output the top 5 source IPs.
    for ip, dest_ips in top_ips:
        print(f"Source IP: {ip} has connections with {len(dest_ips)} unique destination IPs.")

# Execute the function
analyze_logs(log_file)
