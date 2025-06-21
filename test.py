#192.168.1.18/led/on
#192.168.1.18/led/off

import network
import socket
import time
from machine import Pin

# WLAN nesnesini oluştur ve STA_IF modunu ayarla
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = "zknHome2"
password = "home2021"
wlan.connect(ssid, password)

# HTML içeriği
html = """<!DOCTYPE html>
<html>
<head> <title>Pico W</title> </head>
<body> <h1>Pico 2W</h1>
<p>%s</p>
</body>
</html>
"""


# Bağlanmak için bekle veya başarısız ol
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Bağlantı hatasını işle
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])

# Soket aç
try:
    addr_info = socket.getaddrinfo('0.0.0.0', 80)
    addr = addr_info[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)
    led = machine.Pin("LED", machine.Pin.OUT)

    # Bağlantıları dinle
    while True:
        try:
            cl, addr = s.accept()
            print('client connected from', addr)
            request = cl.recv(1024)
            print(request)

            request = str(request)
            led_on = request.find('/led/on')
            led_off = request.find('/led/off')

            print(' led on = ' + str(led_on))
            print(' led off = ' + str(led_off))
            stateis = "LED unknown"

            if led_on != -1:
                print("led on")
                led.value(1)  # LED'i aç
                stateis = "LED is ON"

            if led_off != -1:
                print("led off")
                led.value(0)  # LED'i kapat
                stateis = "LED is OFF"

            response = html % stateis
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()

        except OSError as e:
            cl.close()
            print('connection closed')

except Exception as e:
    print("Error occurred:", e)
