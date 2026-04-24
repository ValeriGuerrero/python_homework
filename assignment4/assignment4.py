import pandas as pd
import numpy as np
from datetime   import datetime

#Task 1
# Creating a DataFrame from a dict
data_frame = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data_frame)
print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age']+ 1
print(task1_older)

task1_older.to_csv('employees.csv', sep=',', index=False, header=True, encoding=None)

#Task 2

task2_employees = pd.read_csv('employees.csv')
print("Task 2", task2_employees.head()) #will display the first five rows of the DataFrame by default

json_employees = pd.read_json('additional_employees.json')
print(json_employees.head())

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

#Task 3
first_three = more_employees.head(3)
print("Task 3", first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()

#Task 4
read_dirty_data = pd.read_csv('dirty_data.csv')
dirty_data = pd.DataFrame(read_dirty_data)
print("Task 4", dirty_data)

clean_data = dirty_data.copy()

print(clean_data.duplicated())

#no_duplicate_rows = clean_data.drop_duplicates() creates new dataframe 
print(clean_data.drop_duplicates(inplace=True)) #changes the original dataframe

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
clean_data["Salary"] = clean_data["Salary"].replace("n/a", pd.NA)
print(clean_data)

clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())

clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

print(clean_data)

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")

print("Dates", clean_data)

clean_data[["Name", "Department"]] = clean_data[["Name", "Department"]].apply(lambda x : x.str.strip())

clean_data[["Name", "Department"]] = clean_data[["Name", "Department"]].apply(lambda x : x.str.upper())

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"].isna().sum(), errors="coerce")

print(clean_data)