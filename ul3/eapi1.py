#!/usr/bin/env python
import ssl
from getpass import getpass
import argparse
import requests.packages.urllib3
import jsonrpclib
from pprint import pprint as pp

# Disable SSL warnings
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

# Set up argument parser
parser = argparse.ArgumentParser(description="Script to print IP addresses of all interfaces.")
parser.add_argument("hostname", help="Hostname or IP address of the device")
args = parser.parse_args()

# Get the password from the user
password = getpass("Enter password: ")

# Define the device information
device = args.hostname
username = "admin"

# Create JSON-RPC server connection
sw = jsonrpclib.Server(f"https://Diogo.SerranoMendes:{password}@{device}/command-api")

# Execute the command and print the results
result = sw.runCmds(1, ["show ip interface brief"])
pp(result)