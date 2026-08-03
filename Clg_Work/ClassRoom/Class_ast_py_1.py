"""
Problem Statement:
You are given a list of employee
records, where each record is a dictionary with keys 'name', 'department', and
'salary'. Write a function department_summary(employees) that returns a
dictionary mapping each department name to a tuple (employee_count, average_salary,
top_earner_name). average_salary must be rounded to two decimal places. If two
employees in the same department are tied for the highest salary, report the
one that appears first in the input order.

Input Description:
A list of dictionaries with keys
'name' (str), 'department' (str), 'salary' (float), hard-coded or read from
standard input as one record per line in the format name,department,salary.
"""

employee = [
    {"Name": "Amit", "Dept": "Engineering", "Salary": 75000}, 
    {"Name": "Sneha", "Dept": "Engineering", "Salary": 82000},
    {"Name": "Rahul","Dept": "Sales", "Salary": 54000}, 
    {"Name": "Priya", "Dept": "Sales", "Salary": 61000},
    {"Name": "Karan", "Dept": "Engineering", "Salary": 69000}
]

def department_summary(employee:list):
    temp={}
    #this loop will create an dictionary where we will get the dept ,count of employee , total salary ,heigheset salary , Name of the emp with high salary
    for data in employee:
        name=data['Name']
        department=data['Dept']
        salary=data['Salary']
        
        # create an department in the temp dict if not there and if there then update the count and total_salary
        if department not in temp:
            # count,total_sal,high_sal,name
            temp[department]=[1,salary,salary,name]
        else:
            temp[department][0]+=1
            temp[department][1]+=salary
            
            # here we will record the name and salary of the highest employee in the department
            if salary > temp[department][2]:
                temp[department][2]=salary
                temp[department][3]=name
        
    result={}        
    # as for the final output in tuple like format 
    for dept,data in temp.items():
        count=data[0]
        total_sal=data[1]
        avg_sal=round(total_sal/count,2)
        top_emp=data[3]
        
        result[dept]=(count,avg_sal,top_emp)
        
    return result


print(department_summary(employee))
        
    
            