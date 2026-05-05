
# students = {6225:"Karthik", 6633:"Neeraj", 6628:"Aditya"}


def check_student_function(rollNumber):
    try:
        check_student = {6225:"Karthik", 6633:"Neeraj", 6628:"Aditya"}[rollNumber]
    except KeyError:
        print("This student does not exits")
    else:
        print(f"Hello {check_student}")

check_student_function(6225)
check_student_function(6285)