import csv
import traceback
import os 
import custom_module
from datetime import datetime

#Task 2
def read_employees():
    employees = { }
    rows = []

    try:
        with open('../csv/employees.csv') as file:
            reader = csv.reader(file, delimiter= ',')
        
            fields = next(reader)  # Read header
            employees['fields'] = fields #dict where we add the header named fields
            for row in reader:
                rows.append(row)
            employees['rows'] = rows #list of lists which key value is rows

        return employees #dict
                
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees() #global variable

print("task2", employees)

#Task 3

def column_index(employee_id):
    try:
        employee_id_index = employees["fields"].index(employee_id)
        return employee_id_index
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employee_id_column = column_index("last_name")

print("Task 3", employee_id_column)

#Task 4

def first_name(row_num):
    employee_id_column = column_index("first_name")
    try:
        employee_row = employees['rows']
        
        return employee_row[row_num][employee_id_column]
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

print("Task 4", first_name(3))

#Task 5
def employee_find(employee_id):
    employee_id_column = column_index("employee_id")
    try:
        def employee_match(row):
    
            return int(row[employee_id_column]) == employee_id 
    
        matches=list(filter(employee_match, employees["rows"])) #filter function 
        
        return matches
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

print("Task 5", employees["fields"])
print("Task 5", employee_find(3))

#Task 6
    
def employee_find_2(employee_id):
    employee_id_column = column_index("employee_id")
    
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    
    return matches
    
print("Task 6", employee_find_2(1))

#Task 7
def sort_by_last_name():
    employee_id_column = column_index("last_name")
    employees["rows"].sort(key = lambda row : row[employee_id_column])
    return employees["rows"]
   
print("Task 7", sort_by_last_name())

#Task 8 
def employee_dict(row):
        employee_column = employees['fields']
        
        return dict(zip(employee_column[1:], row[1:]))

print("Task 8", employee_dict(employees['rows'][0]))

#Task 9
def all_employees_dict():
    result = {}
    employee_row = employees['rows']    
    for row in employee_row:
        result[row[0]] = employee_dict(row)
    return result
print("Task 9", all_employees_dict())

#Task 10 
def get_this_value():
    key = os.environ.get("THISVALUE")
    return key
print(get_this_value())

#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
print(custom_module.secret)

#Task 12
def helper_function(read_file):
    
    minutes = {}
    rows = []
   
    with open(read_file) as file:
            reader = csv.reader(file, delimiter= ',')

            fields = next(reader)
            minutes['fields'] = fields 

            for row in reader:
                row_tuple = tuple(row)
                rows.append(row_tuple)
                
            minutes['rows'] = rows

    return minutes

def read_minutes():
    minutes1 = helper_function('../csv/minutes1.csv')
    minutes2 = helper_function('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

#Task 13
def create_minutes_set():
    minutes1, minutes2 = read_minutes()

    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])

    set_union = set1.union(set2)

    return set_union

minutes_set = create_minutes_set()

print('Task 13', create_minutes_set())

#Task 14
def create_minutes_list():
    minutes_set = create_minutes_set()
    
    minutes_map = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set) #map runs to each tuple and transform the date it's like a loop for x in minutes_list

    result = list(minutes_map)

    return result

minutes_list = create_minutes_list()

print(create_minutes_list())

#Task 15
def write_sorted_list():
    minutes_list = create_minutes_list()
    minutes1, _ = read_minutes()
    
    sort_date = sorted(minutes_list,key = lambda x: x[1])
    
    new_minutes_map = map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sort_date)

    turn_list = list(new_minutes_map)

    with open('./minutes.csv', 'w') as file:
        writer = csv.writer(file, delimiter= ',')
        print("Type111", type(minutes1))
        writer.writerow(minutes1['fields']) 
        writer.writerows(turn_list)   

    return turn_list

print("Task 15", write_sorted_list())