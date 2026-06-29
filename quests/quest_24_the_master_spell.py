#!/usr/bin/python3
def ask_for_age():
	age = int(input("What is your age:"))
	return age
your_age = ask_for_age()
def can_they_vote(age):
	if age >= 18:
		print("You can vote!")
	else:
		print("You can't vote!")
can_they_vote(your_age)
