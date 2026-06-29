#!/usr/bin/python3
def calculate_area(length, width):
	area = length * width
	return area
l = float(input("what is the length of the rectangle:"))
w = float(input("what is the width of the rectangle:"))
print(f"The area of your rectangle is: {calculate_area(l, w)}")
