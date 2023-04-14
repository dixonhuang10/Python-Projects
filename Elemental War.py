import random

user_wins = 0
draws = 0
computer_wins = 0

options = ["earth", "fire", "metal", "water", "wood"]


while True: 

    
    user_input = input("Attack with Earth/Fire/Metal/Water/Wood or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options: 
        continue 

    random_number = random.randint(0, 4)
    # earth: 0, fire: 1, metal: 2, water: 3, wood:4
    computer_pick = options[random_number]
    print("Computer attacked with:", computer_pick + ".")

    if user_input == "water" and computer_pick == "metal":
        print("Victory!")
        user_wins += 1

    elif user_input == "metal" and computer_pick == "earth":
        print("Victory!")
        user_wins += 1

    elif user_input == "earth" and computer_pick == "fire":
        print("Victory!")
        user_wins += 1

    elif user_input == "fire" and computer_pick == "wood":
        print("Victory!")
        user_wins += 1

    elif user_input == "wood" and computer_pick == "water":
        print("Victory!")
        user_wins += 1

    elif user_input == "water" and computer_pick == "fire":
        print("Victory!")
        user_wins += 1

    elif user_input == "fire" and computer_pick == "metal":
        print("Victory!")
        user_wins += 1

    elif user_input == "metal" and computer_pick == "wood":
        print("Victory!")
        user_wins += 1

    elif user_input == "wood" and computer_pick == "earth":
        print("Victory!")
        user_wins += 1

    elif user_input == "earth" and computer_pick == "water":
        print("Victory!")
        user_wins += 1

    elif user_input == "water" and computer_pick == "water":
        print("Draw!")
        draws += 1

    elif user_input == "fire" and computer_pick == "fire":
        print("Draw!")
        draws += 1

    elif user_input == "metal" and computer_pick == "metal":
        print("Draw!")
        draws += 1

    elif user_input == "wood" and computer_pick == "wood":
        print("Draw!")
        draws += 1

    elif user_input == "earth" and computer_pick == "earth":
        print("Draw!")
        draws += 1

    else: 
        print("Defeated!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Draws", draws)
print("The computer won", computer_wins, "times.")
print("Goodbye!")



