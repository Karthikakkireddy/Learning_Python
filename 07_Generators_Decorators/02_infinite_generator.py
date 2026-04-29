def infinite_task():
    count =1 
    while True:
        yield f"Task : {count}"
        count+=1

refil = infinite_task()

for _ in range(3):
    print(next(refil))