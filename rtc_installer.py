import SDL_DS3231
import subprocess
import urllib.request

ds3231 = SDL_DS3231.SDL_DS3231(6, 0x68) 

def connect():
	try:
		urllib.request.urlopen('https://www.google.com/')
		return True
	except:
		return False

def set_time_rtc_from_pi():
	ds3231.write_now()
	
	
def set_time_pi_from_rtc():
	set_time_rtc_from_pi()
	hwclock_dttm = ds3231.read_datetime().strftime("%Y-%m-%d %H:%M:%S")
	temp = subprocess.Popen(["sudo", "date", "-s", hwclock_dttm])

def main():
	print("==========================")
	print("Choose action")
	print("1. Set RTC Time from Pi")
	print("2. Show RTC Time")
	print("==========================")
	choice = input("Apaymu?: ")
	if choice == '1':
		if connect():
			set_time_pi_from_rtc()
			print('Connected')
		else:
			print('No internet connection.')
		
	elif choice == '2':
		print(ds3231.read_datetime())
		print("")
		main()
	
main()

#set RTC time manually
# Format: SS(0-59),MM(0-59),HH(0-23),DAY(0-7),DATE(1-31),MM(1-12),YY(0-99)
#ds3231.write_all(0,10,2,2,2,2,28,True)



