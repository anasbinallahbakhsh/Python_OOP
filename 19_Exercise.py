while True:
 try:
  number=int(input('Enter a number :'))
  break
 except ValueError:
  print('plese type an integer')
 except:
  print('unexpecte error !!')
 else:
        print(f"User input = {number}")
 finally:
         print('finally blocks ')
