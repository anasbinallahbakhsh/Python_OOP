from csv import reader
with open('file3.csv', 'r') as f:
    csv_reader= reader(f)
    #itera 
    next (csv_reader)
    for rows in csv_reader:
                print(rows)