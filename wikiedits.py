#/usr/bin/env python3
import ipaddress
import re

nets = open('nets.txt').read().strip().split()

nets = list(map(ipaddress.IPv4Network, nets))

for line in open('title_or_ip.txt'):
    line = line.strip()
    if 'title' in line:
        title = re.sub('.*<title>(.*)</title>.*', '\g<1>', line)
    else: #ip
        ip = re.sub('.*<ip>(.*)</ip>.*', '\g<1>', line)
        try:
            ip = ipaddress.IPv4Address(ip.strip())
        except ipaddress.AddressValueError:
            pass #ipv6 probably
        else:
            if any((ip in n) for n in nets):
                print('{0:<20}{1}'.format(str(ip), title))
