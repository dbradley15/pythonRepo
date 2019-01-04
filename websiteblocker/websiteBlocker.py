# Author: Dan Bradley
# Description: This program will block you from using websites of your choosing during working hours of the day
# when you are using Windows
#
#									Instructions					
#					!--Add this program to your task scheduler in Windows
# 					!--This program must be run under Administrator/Highest Privileges Mode
#					!--Trigger this to program to run on start up
#					!--Add an action to start the program
# 
# Variables: You may adjust the websites you wish to block, the time you cannot access these websites.


import time
from datetime import datetime as dt

hosttemp = "hosts"
hostpath = r"C:\Windows\System32\drivers\etc\hosts"
redirectIP = "127.0.0.1"

# Add any website you wish to block here:
blocked_list = ["www.facebook.com", "facebook.com"]


while True:
	# Adjust the hours you wish to restrict access to webistes in the line below:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("Working Hours")
		with open(hostpath, 'r+') as file:
			contents = file.read()
			for website in blocked_list:
				if website in contents:
					pass
				else:
					file.write(redirectIP + "  " + website + "\n")
	else:
		# Unblock websites or permit access
		with open(hostpath, 'r+') as file:
			contents = file.readlines()
			file.seek(0)
			for line in contents:
				if not any(website in line for website in blocked_list):
					file.write(line)
			file.truncate()
		print("Ok to play")

	time.sleep(8)
	