#!/bin/bash

# Flush all current rules from iptables
iptables -F

# Set default policies for incoming, outgoing, and forwarding packets
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

# Example rule: allow HTTP and HTTPS traffic
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Allow all traffic on the loopback interface
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Allow incoming ICMP (ping)
iptables -A INPUT -p icmp -j ACCEPT

# Block outgoing ping
iptables -A OUTPUT -p icmp --icmp-type echo-request -j REJECT

# Log iptables denied calls (for debugging)
iptables -A INPUT -m limit --limit 5/min -j LOG --log-prefix "iptables denied: " --log-level 7

# Keep the process running
tail -f /dev/null
