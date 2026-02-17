import random
Enter_number=int(input("Enter your Number : "))
secret_number=random.randint(1,10)
while True:
    if secret_number==Enter_number:
        break
