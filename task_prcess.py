from machine import Timer, Pin
import uasyncio as asyncio

led = Pin("LED", Pin.OUT)
durum = False

# Timer callback - LED toggle
def görev(timer):
    global durum
    durum = not durum
    led.value(durum)

# Timer başlat
t = Timer()
t.init(period=1000, mode=Timer.PERIODIC, callback=görev)

# Asenkron görevler
async def görev1():
    while True:
        print("Görev 1")
        await asyncio.sleep(1)

async def görev2():
    while True:
        print("Görev 2")
        await asyncio.sleep(2)

# asyncio.run kullanımı
async def main():
    await asyncio.gather(
        görev1(),
        görev2()
    )

asyncio.run(main())

