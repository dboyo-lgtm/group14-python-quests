#!/usr/bin/python3
password = input("Enter a password:")
redopass = input("Re-enter the password:")
if redopass == password:
	print("Access Granted")
else:
	print("Access Denied")
