=====================================================
Install RTC DS3231 for Pi
=====================================================

1. Install i2c tools
	sudo apt-get install python-smbus i2c-tools

2. Enable i2c6 pin
	sudo nano /boot/config.txt
	**then add lines to the end of file
	dtoverlay=i2c6
	**uncomment this line
	dtparam=i2c_arm=on

3. Check if RTC is detected at i2c6
	sudo i2cdetect -y 6

4. Sync time from Pi to RTC
	**run rtc_installer.py

5. Add the script to load at startup
	sudo crontab -e
	**add below lines
	@reboot python /home/pi/cak/test.py &



