# Quest 28 - The Adventure Begins
# A text-based "Choose Your Own Adventure" game.
# Each location is its own function, and functions call other functions
# to move the player through the story toward different endings.

# The starting location - every playthrough begins here
def start():
    print("You wake up at a crossroads in a dark forest.")
    # .lower() makes the input case-insensitive, so "Left" and "left" both work
    choice = input("Do you go 'left' or 'right'? ").lower()

    # Each choice calls a different location function
    if choice == "left":
        cave()
    elif choice == "right":
        river()
    else:
        # Handles any answer that isn't left or right
        print("You stand frozen with indecision until nightfall. Game over.")

# The "left" path - reached by calling cave() from start()
def cave():
    print("You enter a damp cave glittering with strange crystals.")
    choice = input("Do you 'touch' the crystals or 'leave'? ").lower()

    # This branch leads to two of the game's endings
    if choice == "touch":
        print("The crystals grant you ancient magic. You become the forest's guardian!")
        print("ENDING: The Crystal Guardian.")
    else:
        print("You leave quietly and find your way home by morning. Safe, but unchanged.")
        print("ENDING: The Cautious Wanderer.")

# The "right" path - reached by calling river() from start()
def river():
    print("You reach a rushing river with a small wooden boat.")
    choice = input("Do you 'sail' across or 'swim'? ").lower()

    # This branch leads to the other two endings
    if choice == "sail":
        print("The boat carries you to a hidden village that names you their hero!")
        print("ENDING: The Village Hero.")
    else:
        print("The current is too strong and sweeps you far downstream. You're lost.")
        print("ENDING: Lost to the River.")

# This line actually starts the game by calling the first function
start()
