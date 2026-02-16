
correct_password="12345678"
while True:
    user_password=input("Enter your Password : ")
    if user_password==correct_password:
        print("📲" * 40, end="")
        print("\nYou Login Successfully! Congrats  🙏🙏🙏")
        print("This your Password : 💻1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣")
        break
    else:
        print("You Enter Wrong Password : Re-enter 👎😭")
