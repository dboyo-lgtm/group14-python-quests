#!/usr/bin/python3
pieces = 27
friends = 4
each_friend = pieces // friends
remainder = pieces % friends
print(f"Each friends gets: {each_friend}")
print(f"The goblin keeps: {remainder}")
