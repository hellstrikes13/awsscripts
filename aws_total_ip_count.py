#!/usr/bin/python
#author: sudi
import netaddr
import requests
ip_ranges = [] 
total= []
raw_ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
for i in raw_ip_ranges:
    ip_ranges.append(i['ip_prefix'])

for i in ip_ranges:
    ip = netaddr.IPNetwork(i)
    total.append((ip.size)-2)
print sum(total)

