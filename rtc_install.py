import SDL_DS3231
import subprocess
import urllib.request
from os import system, name
from time import sleep
import datetime

ds3231 = SDL_DS3231.SDL_DS3231(6, 0x68) 

# =============================================================
# ==========================Helpers============================

def connect():
	try:
		urllib.request.urlopen('https://www.google.com/')
		return True
	except:
		return False

def no_space_in(string):
	if ' ' in string:
		return False
	else:
		return True	
		
def list_str_to_int(string):
	return int(string)
	
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
		
	# for linux
	else:
		_ = system('clear')
		
def is_time_valid(string):
	timeformat = "%H:%M"
	try:
		validtime = datetime.datetime.strptime(string, timeformat)
		return True
	except:
		return False

# =============================================================


# Sync time from Pi to RTC
def init_rtc():
	ds3231.write_now()
	
# Set Pi time based from the RTC
def set_time_pi_from_rtc():
	init_rtc()
	rtc_time = ds3231.read_datetime().strftime("%Y-%m-%d %H:%M:%S")
	temp = subprocess.Popen(["sudo", "date", "-s", rtc_time])
	
def print_rtc_time():
	print("RTC Time: " + ds3231.read_datetime().strftime("%Y-%m-%d %H:%M:%S"))
	
def ask_time():
	curr_time = input("Input Time and press Enter: ")
	if is_time_valid(curr_time):
		return list(map(list_str_to_int, curr_time.split(':')))
	else:
		print('Error: Invalid time! Please check  time format.')
		print("")
		ask_time()
		
def ask_date():
	# TODO: Add date validation
	curr_date = input("Input Date and press Enter: ")
	if curr_date:
		if no_space_in(curr_date):
			return list(map(list_str_to_int, curr_date.split('-')))
		else:
			print('!!!Invalid date: Must not contain white spaces')
			ask_date()
	else:
		print('Error: Invalid date! Please check  date format.')
		print("")
		ask_date()
	
def set_time_manual():
	print("")
	print("======================================================")
	print("Set Date and Time Manually")
	print("Time Format: 	HH(0-23):MM(0-59)")
	print("Date Format: 	DAY(0-7)-DD(1-31)-MM(1-12)-YY(0-99)")
	print("======================================================")
	
	curr_time_split = ask_time()
	curr_date_split = ask_date()

	# Format: SS(0-59),MM(0-59),HH(0-23),DAY(0-7),DATE(1-31),MM(1-12),YY(0-99)
	#                s, m,  h, d, D, M, Y       
	#ds3231.write_all(0, 10, 2, 2, 2, 2, 28, True)
	ds3231.write_all(0, curr_time_split[1], curr_time_split[0], curr_date_split[0], curr_date_split[1], curr_date_split[2], curr_date_split[3])
	print_rtc_time()

def main():
	print("=============================================================")
	print("Choose option then press enter: ")
	print("1. Install RTC")
	print("2. Show RTC Time")
	print("3. Set Time Manually")
	print("4. Quit")
	print("=============================================================")
	
	choice = input("Apaymu?: ")
	if choice == '1':
		if connect():
			set_time_pi_from_rtc()
			print_rtc_time()
		else:
			print('No internet connection.')
		
	elif choice == '2':
		print_rtc_time()
		print("")
		main()
		
	elif choice == '3':
		clear()
		set_time_manual()
		
	elif choice == '4':
		#exit
		pass
		
	else:
		print("Invalid choice. Select from 1-4")
	
main()


