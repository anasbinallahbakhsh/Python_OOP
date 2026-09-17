# r+, a, w
with open('file.txt2', 'a') as f:
    f.seek(len(f.read()))
    f.write('anas\n focous in your work ')
