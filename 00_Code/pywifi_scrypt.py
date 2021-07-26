# -*- coding: utf-8 -*-

import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
print("Мой интерфейс:", iface.name())

iface.scan()
time.sleep(2)

result = iface.scan_results()

print("\nДоступные сети:")
for i in range(len(result)):
    print(result[i].ssid, result[i].bssid)


profile = pywifi.Profile()
profile.ssid = 'iphone'
profile.auth = pywifi.const.AUTH_ALG_OPEN
profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
profile.key = '1!234567'

profile = iface.add_network_profile(profile)
iface.connect(profile)

result = iface.status()

if result == pywifi.const.IFACE_CONNECTING:
    print("Пробуем присоединиться")

time.sleep(10)

result = iface.status()
if result == pywifi.const.IFACE_CONNECTED:
    print("Соединение установлено")
else:
    print("Статус соединения", result)

