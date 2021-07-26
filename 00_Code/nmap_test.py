#!/usr/bin/python3

import nmap3
import json

scan = nmap3.NmapScanTechniques()
result = scan.nmap_syn_scan("192.168.0.5")

print(result)
#print(result["192.168.0.5"])
#print(result["192.168.0.5"]["ports"][0]["protocol"])
#print(result["192.168.0.5"]["ports"][0]["portid"])
#print(result["192.168.0.5"]["ports"][0]["state"])

for i in result["192.168.0.5"]["ports"]:
	print(i["protocol"], i["portid"], i["state"])
