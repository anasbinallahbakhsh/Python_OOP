# print(f'cursor position - {f.tell()}')
# print('before seek method ')
# f.seek(0)
# print('after seek method')
# print(f'cursor position - {f.tell()}')
# print(f.read())

# lines = f.readlines()
# print(len(lines))
# for line in lines:
#     print(line, end='')

f = open('file1.txt')
for lines in f:
    print(lines, end='')
    f.close