def ask_for_age():
    age = int(input("How old are you? "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("Sorry, you are not old enough to vote yet.")

user_age = ask_for_age()
can_they_vote(user_age)
