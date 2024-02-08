# Simple TCP Port Scanner

A simple Python script for scanning TCP ports on a specified IP address within a given port range.

## Purpose

The purpose of this project is to provide a straightforward TCP port scanning tool. It allows users to specify an IP address and a range of ports to scan, providing information about open ports.

## Usage

```
python3 port_scanner.py -ip <ip_address> -p <port_range>
```
Example:
```
python3 port_scanner.py -ip 192.168.1.1 -p 1-1024
python3 port_scanner.py -ip 192.168.1.1 -p 443-443
```

## Command Line Arguments

The script accepts the following command-line arguments:

- `-ip` or `--ip_address`: Specify the target IP address.
- `-p` or `--port_range`: Provide the port range to scan. Use the format "start-end" (e.g., 1-1024).
