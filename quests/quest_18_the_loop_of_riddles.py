#!/usr/bin/python3
number = 9
guess = int(input("Guess a number between 1 to 20: "))
while guess != number:
	guess = int(input("Guess again: "))
