from scapy.all import *
from collections import defaultdict

scan_log = defaultdict(set)

THRESHOLD = 10

def detect_syn_scan(packet):
    if packet.haslayer(TCP) and packet[TCP].haslayer(IP):
        if packet[TCP].flags == 'S':
            srcIP = str(packet[IP].src)
            dst_port = packet[TCP].dport

        scan_log[srcIP].add(dst_port)

        if len(scan_log[srcIP]) > THRESHOLD:
            print(f"Possible port scan detected from {srcIP} at ports: {sorted(scan_log[srcIP])}")
            scan_log[srcIP].clear()

        
print('Starting IDS - monitoring for SYN Scans...')

sniff(filter = 'tcp', prn = detect_syn_scan, store = 0)
#detect_syn_scan('nagaraj')