secret_number = 7
user_number = int(input("Enter one digit integer: "))
while user_number != secret_number:
    print ("Wrong number! Try again")
    user_number = int(input("Enter one digit integer: "))
print ("Congratulations. Correct number!")
