import threading
import time

def boil_milk():
    print(f"Start Boiling milk {threading.current_thread().name}")
    time.sleep(2)
    print(f"End Boiling milk {threading.current_thread().name}")

def toast_bun():
    print(f"Start Toast bun {threading.current_thread().name}")
    time.sleep(4)
    print(f"End Toast bun {threading.current_thread().name}")

t1 = threading.Thread(target=boil_milk, name = "t1")
t2 = threading.Thread(target=toast_bun, name = "t2")

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"Total time taken {end-start:.2f}")