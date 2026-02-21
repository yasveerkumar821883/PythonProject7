try:
    num1=int(input("Enter the Number 1 : "))
    num2=int(input("Enter the Number 2 : "))
    div=num1/num2
    print(f"Division of {num1} and {num2} = {div}")
except ZeroDivisionError:
    print("Denominator should  not be zero ")
except ValueError:
    print("Value should be digit")