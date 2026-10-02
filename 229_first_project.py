import os, shutil

# NOTE: You can write every single extension inside tuples
dict_extensions = {
    'audio_extensions': ('.mp3', '.m4a', '.wav', '.flac'),
    'videos_extensions': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'documents_extensions': ('.doc', '.pdf', '.txt')
}

folderpath = input('Enter folder path: ')

def file_finder(folder_path, file_extensions):
    return [
        file for file in os.listdir(folder_path)
        for extension in file_extensions
        if file.endswith(extension)
    ]
for extension_type, extension_tuple in dict_extensions.items():

    folder_name = extension_type.split('_')[0] + 'Files'
    new_folder_path = os.path.join(folderpath, folder_name)

    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)

    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(new_folder_path, item)

        shutil.move(item_path, item_new_path)