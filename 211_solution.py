def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err :
        # print('you canot divide a number by zero')
        print(err)
    except TypeError as err:
        print(" number must bhe int or flot ")
    except:
        print("unexpected error")
print(divide(10,0))