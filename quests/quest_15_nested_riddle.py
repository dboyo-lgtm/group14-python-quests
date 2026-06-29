direction = input("enter direction(left/right): ")
if direction == "left":
   ability = input("enter ability(swim/wait): ")
   if ability == "swim":
       print("you can find the treasure")
   else: 
       print("sorry! no treasure")
else:
    print("proceed and hit a dead end") 
