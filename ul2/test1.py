import json
import requests
import argparse

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

def configure_ceos(device_ip, username="admin", password="admin"):
    """Configures loopback interfaces on a cEOS-lab device using eAPI."""
    
    # List of commands to configure loopback interfaces
    commands = [
        "configure terminal",
        "interface Loopback1",
        "ip address 1.1.1.1/32",
        "exit",
        "interface Loopback2",
        "ip address 1.1.1.2/32",
        "exit",
        "interface Loopback3",
        "ip address 1.1.1.3/32",
        "exit"
    ]

    # eAPI request payload
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "version": 1,
            "cmds": commands,
            "format": "json"
        },
        "id": 1
    }

    # eAPI URL
    url = f"https://{device_ip}/command-api"

    try:
        response = requests.post(
            url,
            auth=(username, password),
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            verify=False  # Disable SSL verification (not recommended for production)
        )
        response.raise_for_status()
        print("Configuration applied successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error configuring the device:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Configure loopback interfaces on cEOS-lab.")
    parser.add_argument("device_ip", help="IP address of the cEOS-lab device")

    args = parser.parse_args()
    configure_ceos(args.device_ip)