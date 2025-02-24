#!/bin/bash

# Check if the script is running on an Arista switch
if [[ ! -f /etc/Eos-release ]]; then
    echo "This script must be run on an Arista EOS device."
    exit 1
fi

echo "============================================="
echo "  Arista EOS Health Check Report"
echo "============================================="
echo ""

# Collect basic system information
echo "[+] System Information:"
hostname
uptime
echo ""

# CPU and Memory Usage
echo "[+] CPU and Memory Usage:"
top -b -n1 | head -n 10
echo ""

# Interface Status
echo "[+] Interface Status (Admin Down / Errors / Drops):"
FastCli -p 15 -c "show interfaces counters errors" | grep -E 'Port|Ethernet|Management'
echo ""

# Configured IP Addresses
echo "[+] Configured IP Addresses:"
FastCli -p 15 -c "show ip interface brief" | grep -E 'Ethernet|Vlan|Management'
echo ""

# BGP Summary (if BGP is configured)
echo "[+] BGP Summary (if configured):"
FastCli -p 15 -c "show ip bgp summary" 2>/dev/null || echo "BGP not configured."
echo ""

# OSPF Summary (if OSPF is configured)
echo "[+] OSPF Summary (if configured):"
FastCli -p 15 -c "show ip ospf neighbor" 2>/dev/null || echo "OSPF not configured."
echo ""

# Show recent logs
echo "[+] Recent System Logs:"
tail -n 10 /var/log/messages
echo ""

echo "============================================="
echo "  Health Check Complete!"
echo "============================================="
