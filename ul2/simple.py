import json
import subprocess

# Run the EOS command
command = "Cli -c 'show ip interface brief | json'"
output = subprocess.run(command, shell=True, capture_output=True, text=True)

# Parse JSON output
try:
    interfaces = json.loads(output.stdout)
    
    # Iterate over interfaces and check for missing IP addresses
    for iface, details in interfaces.get("interfaces", {}).items():
        ip_info = details.get("interfaceAddress", {}).get("ipAddr", {}).get("address")
        if not ip_info:
            print(f"⚠️ Warning: {iface} has no IP address assigned!")
        else:
            print(f"✅ {iface} has IP: {ip_info}/{details['interfaceAddress']['ipAddr']['maskLen']}")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON output: {e}")
except KeyError as e:
    print(f"Unexpected JSON structure, missing key: {e}")