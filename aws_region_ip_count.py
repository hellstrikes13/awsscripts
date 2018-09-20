#!/usr/bin/python
import requests
import netaddr
ip_ranges = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json").json()['prefixes']
regions = []
for i in ip_ranges:
	regions.append(i['region'])
regs = set(regions)
for r in regs:
	total = []
	for i in [item['ip_prefix'] for item in ip_ranges if item["region"] == r ]:
            ip = netaddr.IPNetwork(i)
            total.append((ip.size) - 2)
        print r,'-> ',sum(total)
        del total
