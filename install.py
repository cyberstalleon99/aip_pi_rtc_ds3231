#!/usr/bin/env python

import subprocess
from crontab import CronTab

def replace_str(file_path, orig_str, new_str):
	f_in = open(file_path, "rt")
	data = f_in.read()
	data = data.replace(orig_str, new_str)
	f_in.close()
	f_in = open(file_path, "wt")
	f_in.write(data)
	f_in.close()

def install_i2c_tools():
	print('Installing i2ctools.....')
	subprocess.call(["sudo", "apt-get", "install", "python-smbus", "i2c-tools"])
	print('Done installing i2ctools')

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
	my_cron = CronTab(user='root')
	job = my_cron.new(command='python /home/pi/aip_pi_rtc_ds3231/start_up.py')
	job.every_reboot()
	my_cron.write()
	print('Start up script for the RTC was installed')

def main():
	install_i2c_tools()
	enable_i2c_arm()
	enable_i2c6_pin()
	run_at_startup()
	
	print('======================================================================')
	print('Shutdown your pi then connect RTC to i2c6 pins')
	print('======================================================================')
	
main()


