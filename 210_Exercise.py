

def divide_number():
    try:
        num1=int(input("Enter a first number:"))
        num2=int(input("Enter a second number:"))
        print(num1/num2)
    except ValueError:
        print("type an integer ")
    except ZeroDivisionError:
        print(" Don't divide by zero")
    divide_number()
print(divide_number( ))