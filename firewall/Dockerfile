FROM ubuntu:latest

# Install iptables
RUN apt-get update && apt-get install -y iptables

# Copy the firewall script
COPY firewall-rules.sh /usr/local/bin/firewall-rules.sh

# Make the script executable
RUN chmod +x /usr/local/bin/firewall-rules.sh

# Run the script
CMD ["/usr/local/bin/firewall-rules.sh"]
