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

# Sync time from Pi to RTC
def init_rtc():
	ds3231.write_now()
	
# Set Pi time based from the RTC
def set_time_pi_from_rtc():
	init_rtc()
	rtc_time = ds3231.read_datetime().strftime("%Y-%m-%d %H:%M:%S")
	temp = subprocess.Popen(["sudo", "date", "-s", rtc_time])
	
def no_space_in(string):
	if ' ' in string:
		return False
	else:
		return True	

def ask_time():
	curr_time = input("Input Time and press Enter: ")
	if no_space_in(curr_time):
		return curr_time.split(':')
	else:
		print('!!!Invalid time: Must not contain white spaces')
		ask_time()
		
def ask_date():
	curr_date = input("Input Date and press Enter: ")
	if no_space_in(curr_date):
		return curr_date.split('-')
	else:
		print('!!!Invalid date: Must not contain white spaces')
		ask_date()
	
def set_time_manual():
	print("")
	print("=============================================")
	print("Set Date and Time Manually")
	print("Time Format: 	HH(0-23):MM(0-59)")
	print("Date Format: 	DAY(0-7)-DD(1-31)-MM(1-12)-YY(0-99)")
	print("=============================================")
	#curr_time = input("Input Time and press Enter: ")
	#curr_date = input("Input Date and press Enter: ")
	
	#curr_time_split = curr_time.split(':')
	#curr_date_split = curr_date.split('-')
	
	curr_time_split = ask_time()
	curr_date_split = ask_date()
	
	print('Written date and time')
	print(curr_time_split)
	print(curr_date_split)
	#ds3231.write_all(0, curr_time_split[1], curr_time_split[0], curr_date_split[0], curr_date_split[1], curr_date_split[2], curr_date_split[3])

def main():
	print("=============================================================")
	print("Choose option then press enter: ")
	print("1. Install RTC")
	print("2. Show RTC Time")
	print("3. Set Time Manually")
	print("=============================================================")
	
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
		
	elif choice == '3':
		# Format: SS(0-59),MM(0-59),HH(0-23),DAY(0-7),DATE(1-31),MM(1-12),YY(0-99)
		#                s, m,  h, d, D, M, Y       
		#ds3231.write_all(0, 10, 2, 2, 2, 2, 28, True)
		set_time_manual()
	
main()

#set RTC time manually

#ds3231.write_all(0,10,2,2,2,2,28,True)



