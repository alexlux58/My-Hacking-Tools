'''
ICMP packets can be monitored or blocked as the target organization would 
not expect a regular user to “ping a server”. 
Using the ARP (Address Resolution Protocol) to identify targets on the local network is more effective.
'''

from scapy.all import scapy

interface = "eth0"
ip_range = "10.10.X.X/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = scapy.Ether(dst=broadcastMac)/scapy.ARP(pdst = ip_range) 

ans, unans = scapy.srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%")) 