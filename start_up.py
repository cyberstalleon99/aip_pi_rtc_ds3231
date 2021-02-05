import SDL_DS3231
import subprocess

ds3231 = SDL_DS3231.SDL_DS3231(6, 0x68) 
hwclock_dttm = ds3231.read_datetime().strftime("%Y-%m-%d %H:%M:%S")
temp = subprocess.Popen(["sudo", "date", "-s", hwclock_dttm])

