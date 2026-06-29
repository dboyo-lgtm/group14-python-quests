#!/usr/bin/python3
direction = input("Do you go 'left' or 'right' ? ").strip().lower()
if direction == "left":
	action = input("You reached the river. Do you 'swim' or 'wait'? ").strip().lower()
	if action == "swim":
		print("You have been eaten by a monster of the river. Game Over!")
	else:
		print("You waited and a wanderer who was passing by gave you a treasure. You Win!")
elif direction == "right":
	print("You walked to the path of death. Game Over!")
else:
	print("Invalid choice. You tripped and fell of the mountain. Game Over!")
