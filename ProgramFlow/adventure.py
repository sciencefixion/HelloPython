available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

print("aren't you glad you got out of there")

# for loops continue upon a predetermined number of loops
# while loops a useful when it is difficult to determine how many times the loop needs to run