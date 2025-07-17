from scapy.all import rdpcap, IP, ICMP

# Load the PCAP
packets = rdpcap("SilentSignal.pcap")

payloads = []

for pkt in packets:
    if IP in pkt and ICMP in pkt:
        icmp = pkt[ICMP]
        if icmp.type == 8:  # Echo Request
            data = bytes(icmp.payload)
            print(data)
            if data:
                payloads.append(data)

# Combine and try to decode
full_data = b''.join(payloads)

try:
    print(full_data.decode())
except UnicodeDecodeError:
    print(full_data.decode(errors="replace"))