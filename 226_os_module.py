import os
# os.getcwd()
# print(os.getcwd())
# os.mkdir('movies')
# if(os.path.exists('movies')):
#     print('already exist')
#  movies')else:     os.mkdir('movies')


# open('file.txt','a').close()
# os.mkdir(r'E:\new_python1\
# print(os.listdir())

for item in os.listdir(r'E:\new_python1'):
    path=os.path.join(r'E:\new_python1',item)
    print(path)