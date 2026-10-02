# writer #dictwriter
from csv import writer

with open('file4.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    # methods - writerow, writerows
    # csv_writer.writerow(['name', 'country'])
    # csv_writer.writerow(['Anas', 'Pakistan'])
    # csv_writer.writerow(['Zohaib', 'Pakistan'])
    csv_writer.writerows([['name', 'country'], ['Anas', 'Pakistan'], ['Zohaib', 'Pakistan']])