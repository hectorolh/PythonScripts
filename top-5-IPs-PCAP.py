# This script reads a pcap file. If the packet is an IP packet, it increments a count for the source IP address of the packet.

from scapy.all import *
from collections import Counter

def analyze_pcap(filename):
    packets = rdpcap(filename)

    ip_counts = Counter()
    for packet in packets:
        if 'IP' in packet:
            ip_counts[packet['IP'].src] += 1

    for ip, count in ip_counts.most_common(5):
        print(f"IP address {ip} has sent {count} packets")

analyze_pcap('file.pcap')
