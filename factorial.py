print("Factorial Calculator : ")
num=int(input("Enter the number that you wanna factorial : "))#we calculate the factorial with the help of loop
def fact(num):

    if num==0:
        print(f"factorial is {num}")
    elif num==1:
        print(f"factorial is {num}")
    else:
        factorial=1
        for i in range(1,num+1):
            factorial=factorial*i
        print(f"factorial is  {factorial}")
fact(num)