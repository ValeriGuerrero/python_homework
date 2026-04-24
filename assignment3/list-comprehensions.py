import csv

# Reading CSV into list of lists
employees = []

with open('../csv/employees.csv', newline='') as file:
    reader = csv.reader(file)
    employees = list(reader)

# Create list of full names
names = [row[1] + " " + row[2] for row in employees[1:]]

print("List of Names:", names)

# Filtering names that contain the letter "e"
names_with_e = [name for name in names if "e" in name.lower()]

print("Filter: ", names_with_e)
