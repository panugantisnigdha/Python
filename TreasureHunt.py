
print("You are around a turn right now. Where do you want to go?")
direction = input("Enter L if you want to go left and R if you want to go right: ")

if direction == "L":
    print("You are now near a Lake.")
    lake = input("Enter S if you want to swim across the lake or enter W if you want to wait: ")

    if lake == "W":
        print("Which Door?")
        door = input("Enter R to choose the Red Door, B to enter the Blue Door, and Y to enter the Yellow Door: ")

        if door == "R":
            print("Burned by fire.")
        elif door == "B":
            print("Eaten by beasts.")
        elif door == "Y":
            print("You win!")
        else:
            print("You fell in a Hole")

    elif lake == "S":
        print("You were eaten by a Trot!")
    else:
        print(" Game Over.")

elif direction == "R":
    print("You fell into a hole. Game Over.")
else:
    print(" Game Over.")

