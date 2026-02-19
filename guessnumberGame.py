import random

print("""G 🇺 🇪 🇸 🇸
🇳 🇺 🇲 🅱️ 🇪 🇷 (1️⃣ to 🔟)
🎮 G 🅰️ 🇲 🇪""")
print("-" * 33)
print("Condition: You have 10 attempts!\n")

secret_number = random.randint(1, 10)
attempts = 10

for count in range(1, attempts + 1):
    user_number = int(input("Enter your number: "))

    if user_number == secret_number:
        print("🎉 You guessed the right number! Congrats 😎")
        break
    elif user_number > secret_number:
        print(f"📉 Too High! Attempts left: {attempts - count}")
    else:
        print(f"📈 Too Low! Attempts left: {attempts - count}")

else:
    print("😢 Game Over!")
    print("The secret number was : ", secret_number)

print("It's Over 🎮")
