# -*- coding: utf-8 -*-

from scapy.all import *
from time import sleep
  
iface = "Realtek 8812AU Wireless LAN 802.11ac USB NIC"
devices = set()

# отбрасываем beacons, probe request и responses
def dump_packet(pkt):
    if not pkt.haslayer(Dot11Beacon) and not pkt.haslayer(Dot11ProbeReq) and not pkt.haslayer(Dot11ProbeResp):
        print(pkt.summary())

    if pkt.haslayer(Raw):
        print(hexdump(pkt.load), "\n")

print ("Прослушиваем интерфейс:" + iface)
while True:
    sleep(0.01)
    sniff(iface=iface, prn=dump_packet, count=10, timeout=3, store=0)    
