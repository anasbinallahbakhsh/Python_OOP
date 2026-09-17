# w , a, r+

with open('file.txt,' 'r+') as f:
     f.seek(len(f.read()))
     f.write('\nanas this is compex coding')