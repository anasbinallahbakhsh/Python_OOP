

import os
os.chdir(r'E:\Python_OOP')

# Pass os.walk() directly into the loop using the 'in' keyword
for current_path, folder_names, file_names in os.walk(r'E:\Python_OOP'):
    print(f'current_path: {current_path}')
    print(f'folder_names: {folder_names}')
    print(f'file_names: {file_names}')


    import os 
    os.chdir(r'E:\Python_OOP')
    for current_path, folder_names , file_names in os.walk(r'E:\Python_OOP'):
        print(f'current_path:{current_path}')
        print(f'')

  





import os
os.chdir(r'E:\Python_OOP')
for current_path, folder_names, files_names in os.walk(r'E:\Python_OOP'):
    print(f'currnt_path:{current_path}')
    print(f'folder_names:{folder_names}')
    print(f'files_names:{files_names}')