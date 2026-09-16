# python custom exceptions
# Q - Why custom exceptions ?
# A - To increase the readability of code.

# example
class NameTOOShortError(ValueError): 
    pass
def validate(name):
    if len(name) < 8:
        raise NameTOOShortError('name is too short')

username = input('Enter your name : ')
validate(username)
print(f'hello {username}')

