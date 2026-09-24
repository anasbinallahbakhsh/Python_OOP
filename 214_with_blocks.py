#f=open('file.txt')
# f.read
# f.close()
#with block
#contex manager
with open('file1.txt') as f:
    data=f.read()
print(data)
print(f.closed)