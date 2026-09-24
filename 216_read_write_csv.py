# reader ,DR
# writer, Dictwriter
from csv import DictReader, DictWriter
with open('file.csv','r') as rf:
    with open('file2.csv','w',newline='') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['firat_name','last_name','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age= row['firstname'],row['last_name'],row['age']
            csv_writer.writerow({
                'first_name': fname.uper(),
                'last_name': lname(),
                'age':age()
            })