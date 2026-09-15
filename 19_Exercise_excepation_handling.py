while True:

    try:
        age = int(input("Enter your age:"))
        break

    except ValueError:
        print("Invalid input")
        print('maybe you entered the string input insted input, Try again')

if age < 18:
    print("You can't play this game")
else:
    print("You can play this game") 