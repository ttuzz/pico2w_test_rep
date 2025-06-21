import ntptime
ntptime.settime()

import time
print("Zaman:", time.localtime())

with open("veri.txt", "w") as f:
    f.write("Merhaba Raspberry Pi Pico!\n")
    f.write("Bu bir dosya yazma örneğidir.")

with open("veri.txt", "r") as f:
    icerik = f.read()
    print("Dosya İçeriği:\n", icerik)
    
    
print("-----------------------------------")

import gc

gc.collect()
free = gc.mem_free()
alloc = gc.mem_alloc()
total = free + alloc

print("Toplam RAM:", total, "bayt")
print("Kullanılan:", alloc, "bayt")
print("Boş:", free, "bayt")

import os

fs_stat = os.statvfs("/")

block_size = fs_stat[0]
total_blocks = fs_stat[2]
free_blocks = fs_stat[3]

total_bytes = block_size * total_blocks
free_bytes = block_size * free_blocks
used_bytes = total_bytes - free_bytes
print("-----------------------------------")
print("Toplam Flash:", total_bytes, "bayt")
print("Kullanılan:", used_bytes, "bayt")
print("Boş:", free_bytes, "bayt")


import time

start = time.ticks_ms()

# yoğun işlem
for _ in range(1000000):
    pass

elapsed = time.ticks_diff(time.ticks_ms(), start)
print("-----------------------------------")
print("Geçen süre (ms):", elapsed)

