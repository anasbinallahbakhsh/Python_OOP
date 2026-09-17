while True:
    try:
        number=int(input('Enter a number:')) 

        break
    except ValueError:
      print('plese tyoe an integer!!')
    except:
       print('unexpected error ')
    else:
        print(f'user input{number}')
    finally:
        print("finally block")
