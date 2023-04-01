import socket
import sys
import keyboard
import struct
import datetime

# Create a raw socket to receive all incoming packets
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
sniffer.bind(("0.0.0.0", 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# Open a log file for writing
log_file_path = "packet_log.txt"
try:
    log_file = open(log_file_path, "w")
except Exception as e:
    print("Error opening log file: {}".format(e))
    sys.exit()

# Open a binary file for writing packet data
pcap_file_path = "packet_capture.pcap"
try:
    pcap_file = open(pcap_file_path, "wb")
except Exception as e:
    print("Error opening pcap file: {}".format(e))
    sys.exit()

try:
    # Receive and display incoming packets
    while True:
        packet = sniffer.recvfrom(65565)
        packet = packet[0]
        
        # Extract the source and destination IP addresses
        iph = struct.unpack("!BBHHHBBH4s4s", packet[:20])
        source_ip = socket.inet_ntoa(iph[8])
        dest_ip = socket.inet_ntoa(iph[9])
        
        # Extract other packet information
        protocol = iph[6]
        packet_length = len(packet)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Print packet information to console and log file
        print("Timestamp: {}".format(timestamp))
        print("Source IP: {}".format(source_ip))
        print("Destination IP: {}".format(dest_ip))
        print("Protocol: {}".format(protocol))
        print("Packet Length: {}".format(packet_length))
        
        try:
            log_file.write("Timestamp: {}\n".format(timestamp))
            log_file.write("Source IP: {}\n".format(source_ip))
            log_file.write("Destination IP: {}\n".format(dest_ip))
            log_file.write("Protocol: {}\n".format(protocol))
            log_file.write("Packet Length: {}\n\n".format(packet_length))
            
            # Write packet data to pcap file
            pcap_file.write(packet)
        except Exception as e:
            print("Error writing to log or pcap file: {}".format(e))
    
    # Close the socket and log and pcap files
    sniffer.close()
    log_file.close()
    pcap_file.close()

except KeyboardInterrupt:
    # User pressed Ctrl + C
    print("\nStopping packet capture...")
    sniffer.close()
    log_file.close()
    pcap_file.close()
    sys.exit()
