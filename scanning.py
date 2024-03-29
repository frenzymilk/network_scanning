import ipaddress
import argparse
from socket import socket, AF_INET, SOCK_STREAM

"""
    command line arguments
"""
parser = argparse.ArgumentParser(
    prog='Simple TCP port scanner'
    )
# port 
parser.add_argument(
    "-p",
    "--port_range",
    required=True,
    help="Provide the port range to scan: e.g. 1-5, 1-1 for only one port"
    )
# ip
parser.add_argument(
    "-ip",
    "--ip_address",
    required=True,
    help="Provide the ip address of the host to scan")

args = parser.parse_args()

port_range = args.port_range
ip = args.ip_address

def port_scanning(ip, ports):
    if ports[0] == ports[1]:
        port_range = [int(ports[0])] 
    else:
        port_range = range(int(ports[0]), int(ports[1])+1)
    print(f"Scanning ip {ip}, port range {str(port_range)}")
    for p in port_range:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, p))
        if result == 0:
            print(f"Port {p}: OPEN")
        s.close()

try:
    ipaddress.ip_address(ip)
except ValueError :
    print("Please provide a valid ip address")

port_range = port_range.split("-")
if 1<=int(port_range[0])<=65535 and 1<=int(port_range[1])<=65535 and int(port_range[0])<=int(port_range[1]):
    pass # valid port range
else:
    print("Please provide a valid port number or valid port range")
    exit()



port_scanning(ip, port_range)