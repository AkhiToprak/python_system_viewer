import psutil
import time 

def anzeige_gebrauch(cpu_usage, mem_usage, batterie, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars)) # - sind leere Felder die nicht benutzt wurden. 
     # zb. wenn wir 6% nutzung haben, wäre das █ mal (6% * 50)
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    batterie = (psutil.sensors_battery().percent)
   
   
    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%    ", end="")
    print(f"MEM Usage:|{mem_bar}| {mem_usage:.2f}%    ", end="")
    print(f"Batterie: {batterie}%   ", end="\r")
   


while True:
    anzeige_gebrauch(psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.sensors_battery(), 30)
    time.sleep(0.5)