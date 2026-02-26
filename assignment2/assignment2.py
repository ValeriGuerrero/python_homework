import csv
import traceback

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
            employees['rows'] = rows #list of lists ehich key value is rows

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
def employee_dict():
    