#!/usr/bin/python
import requests
import netaddr
ip_ranges = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json").json()['prefixes']
srv = []
for i in ip_ranges:
	srv.append(i['service'])
srvs = set(srv)
for s in srvs:
	total = []
	for i in [item['ip_prefix'] for item in ip_ranges if item["service"] == s ]:
            ip = netaddr.IPNetwork(i)
            total.append((ip.size) - 2)
        print s,'-> ',sum(total)
        del total
