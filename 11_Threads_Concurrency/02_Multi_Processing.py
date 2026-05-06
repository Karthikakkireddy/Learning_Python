from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing...")
    time.sleep(3)
    print(f"End of {name} chai brewing...")

if __name__ == "__main__":
    brew_chai_process = [
        Process(target=brew_chai, args=(f"Chai maker #{i+1}", ))
        for i in range(3)
    ]
    # Start all process
    for p in brew_chai_process:
        p.start()
    #Wait for all to complete
    for p in brew_chai_process:
        p.join()

    print("All chai servered")