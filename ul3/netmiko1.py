#!/usr/bin/env python
# Print the IP addresses of all interfaces
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Script to print IP addresses of all interfaces.")
parser.add_argument("hostname", help="Hostname or IP address of the device")
args = parser.parse_args()

# Get the password from the user
password = getpass()

# Define the device information
device = {
    "host": args.hostname,
    "username": "admin",
    "password": password,
    "device_type": "arista_eos",
    "command": "show ip interface brief",
}

# Connect to the device and execute the command
command = device.pop("command")
net_connect = Netmiko(**device)
output = net_connect.send_command(command)

# Print the output
print()
print("-" * 80)
print("{}: {}".format(device["host"], device["device_type"]))
print(output)
print("-" * 80)