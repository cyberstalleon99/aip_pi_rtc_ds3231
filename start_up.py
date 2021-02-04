import SDL_DS3231
import subprocess

ds3231 = SDL_DS3231.SDL_DS3231(6, 0x68) 
hwclock_dttm = ds3231.read_datetime().strftime("%Y-%m-%d %H:%M:%S")
temp = subprocess.Popen(["sudo", "date", "-s", hwclock_dttm])

#set RTC time manually
# Format: SS(0-59),MM(0-59),HH(0-23),DAY(0-7),DATE(1-31),MM(1-12),YY(0-99)
#ds3231.write_all(0,10,2,2,2,2,28,True)
