import socket
import sys
import keyboard
import struct

# Create a raw socket to receive all incoming packets
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
sniffer.bind(("0.0.0.0", 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# Receive and display incoming packets
while True:
    # Check if the Esc key is pressed
    if keyboard.is_pressed("esc"):
        break

    packet = sniffer.recvfrom(65565)
    packet = packet[0]
    
    # Extract the source and destination IP addresses
    iph = struct.unpack("!BBHHHBBH4s4s", packet[:20])
    source_ip = socket.inet_ntoa(iph[8])
    dest_ip = socket.inet_ntoa(iph[9])
    
    print("Source IP: {}".format(source_ip))
    print("Destination IP: {}".format(dest_ip))

# Close the socket
sniffer.close()


