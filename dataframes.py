import pandas as p

fruit_set = {'fruit': ["mangos", "banana", "watermalon", "kivi"], 'count': [10, 34, 78, 44]}
v = p.DataFrame(fruit_set)
print(v)

student_details = {'name': ["ajay", "priyanka", "renuka"], 'age': ["78", "89", "6"]}
v = p.DataFrame(student_details)
print(v)

# if u want to find out pertiular data from database.

student_details = {'name': ["ajay", "priyanka", "renuka"], 'age': ["78", "89", "6"]}
v = p.DataFrame(student_details)
print(v.loc[2])  # this will give only one data.
print(v.loc[[2,0]])  # this will filter multiple data.

#chnaging index giving our own indies

student_details={'name':["ajay","priyanka","renuka"],'age':["78","89","6"]}
v=p.DataFrame(student_details,index=["101","102","103"])
print(v)

#converting .csv file into dataframe

v=p.read_csv("G:/EmployeeData.csv")
print(v)

#coverting data frame into .csv(excel)

fruit_set = {'fruit': ["mangos", "banana", "watermalon", "kivi"], 'count': [10, 34, 78, 44]}
v = p.DataFrame(fruit_set)
print(v)
v.to_csv("G:/empdetails.csv")
