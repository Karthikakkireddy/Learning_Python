import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2)
def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(4)

# Creating two threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

#Starting two threads
order_thread.start()
brew_thread.start()

#Joining the threads after finishing their tasks
order_thread.join()
brew_thread.join()

print("All orders taken and chai brewed")