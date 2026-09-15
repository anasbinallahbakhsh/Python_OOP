while True:

    try:
        number = int(input("Enter a number: "))
        break

    except ValueError:
        print("Please type an integer!!")

    except:
        print("Unexpected error!!!")

    else:
        print(f"User input = {number}")
    finally:
        print('finally blocks ')