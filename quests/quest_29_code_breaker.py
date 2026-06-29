# Quest 29 - The Code Breaker
# Gives the user 3 attempts to guess a secret code, with feedback after each
# guess, and stops early if they get it right.

secret_code = "42"        # The code the user is trying to guess (kept as text)
max_attempts = 3          # Total number of tries allowed
attempts_used = 0         # Counter that tracks how many guesses have been made
guessed_correctly = False # Flag that remembers whether the user won

print("Crack the code! You have 3 attempts to guess the secret code.")

# Keep looping as long as the user still has attempts left
while attempts_used < max_attempts:
    guess = input("Enter your guess: ")
    attempts_used = attempts_used + 1  # Count this guess

    if guess == secret_code:
        print("Correct! You cracked the code!")
        guessed_correctly = True
        break  # Exit the loop immediately so we don't ask again
    else:
        # Work out how many tries remain after this wrong guess
        attempts_left = max_attempts - attempts_used
        if attempts_left > 0:
            print(f"Wrong! You have {attempts_left} attempt(s) left.")
        else:
            # Special wording for the final failed attempt
            print("Wrong! That was your last attempt.")

# Runs only if the loop ended without a correct guess
if not guessed_correctly:
    print("Game over. The code was 42.")
