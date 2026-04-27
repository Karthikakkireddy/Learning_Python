
def fun_a():
    name = "Karthik"
    def inner_fun_a():
        nonlocal name 
        name = "Aditya"
    inner_fun_a()
    print(f"Outer name : {name}")

fun_a()

roll_no = 6225
def fun_b():
    def inner_fun_b():
        global roll_no
        print(f"Before inner : {roll_no}")
        roll_no = 6633
        print(f"After inner : {roll_no}")
    inner_fun_b()

print(f"Outside before : {roll_no}")
fun_b()
print(f"Outside after : {roll_no}")