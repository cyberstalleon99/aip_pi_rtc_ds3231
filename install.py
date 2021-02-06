#!/usr/bin/env python

import subprocess
import __init__
#from crontab import CronTab

# =============================================================
# ==========================Helpers============================

def replace_str(file_path, orig_str, new_str):
	f_in = open(file_path, "rt")
	data = f_in.read()
	data = data.replace(orig_str, new_str)
	f_in.close()
	
	f_in = open(file_path, "wt")
	f_in.write(data)
	f_in.close()
	
def get_cron_user(user):
	from crontab import CronTab
	my_cron = CronTab(user=user)
	return my_cron

# =============================================================

def install_dependencies():
	print('Installing dependencies.....')
	subprocess.call(["sudo", "apt-get", "install", "python-smbus", "i2c-tools"])
	
	try:
		from crontab import CronTab
		print('python3-crontab is already installed.')
	except ImportError as e :
		print('Installing python3-crontab package.....')
		subprocess.call(["sudo", "apt-get", "install", "python3-crontab",])
	print('Done installing dependencies.')

# Uncomment dtparam=i2c_arm=on
def enable_i2c_arm():
	replace_str("/boot/config.txt", '#dtparam=i2c_arm=on', 'dtparam=i2c_arm=on')
	print('i2c_arm enabled')

# Append dtoverlay=i2c6 at the end of file 
def enable_i2c6_pin():
	config_file = open("/boot/config.txt", "a+")
	
	if '#dtoverlay=i2c6' not in config_file.read() or 'dtoverlay=i2c6' not in config_file.read():
		config_file.write("dtoverlay=i2c6")
		config_file.close()
	print('i2c6 pin enabled')
		
# Enable script to run at startup		
def run_at_startup():
	my_cron = get_cron_user(user='root')
	job = my_cron.new(command='python /home/pi/aip_pi_rtc_ds3231/start_up.py')
	job.every_reboot()
	my_cron.write()
	print('Start up script for the RTC was installed')

def main():
	if __init__.installed:
		print('[INFO] Module is already installed')
	else:
		install_dependencies()
		enable_i2c_arm()
		run_at_startup()
	
		print('======================================================================')
		print('Shutdown your pi then connect RTC to i2c6 pins')
		print('======================================================================')
	
main()


