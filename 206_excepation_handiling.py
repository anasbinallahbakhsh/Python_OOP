#Exeception handiling
#try except else finally
while True:
    try:
        age = int(input('enter your age: ')) #seven
        break
    except ValueError:
        print('may be you entered string insted of number, try agin ')
    except:
        print('unexpected error')
if age < 18:
    print('you can \t play this game')
else:
    print('you can play this game')