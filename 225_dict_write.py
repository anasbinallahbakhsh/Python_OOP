from csv import DictWriter

with open('final.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f, fieldnames=['first_name', 'last_name', 'age'])
    csv_writer.writeheader()
    csv_writer.writerow({
        "first_name": "Anas",
        "last_name": "malik",
        "age": "18"
    })
    csv_writer.writerow({
        "first_name": "zohaib",
        "last_name": "malik",
        "age": "18"
    })

    # write rows
    csv_writer.writerows([
        {'first_name': 'Anas', 'last_name': 'zohaib', 'age': '17'},
        {'first_name': 'Anas', 'last_name': 'zohaib', 'age': '18'},
        {'first_name': 'Anas', 'last_name': 'zohaib', 'age': '20'}
    ])