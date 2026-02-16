import random

print("Welcome in Ludo!")

while True:
    choice = input("Press Enter to roll dice or 'q' to quit: ")

    if choice == "q":
        print("Exiting Game...")
        break

    elif choice == "":
        number = random.randint(1, 6)
        print("Your Number:", number)

    else:
        print("Invalid input!")
print("Game Over !")