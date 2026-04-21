student = dict(name = "Karthik", roll_no = 6225, department = "CSC")
print(student)


student = {6225:"Karthik", 6628:"Aditya", 6633:"Neeraj"}
print(student[6225])
# print(student[6285]) // KEY ERROR 

message = "Name not found"
check_name = student.get(6285, message)
print(check_name )  


print('Karthik' in student)

