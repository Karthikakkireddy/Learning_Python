def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except GeneratorExit:
        # When ever python finished the script it automatically uses .close() which 
        # Throws a special exception named "GeneratorExit" exception. 
        # This # next(stall) only "Stall closed, No more chai" gets printed
        print("Stall closed, No more chai")

stall = chai_stall()
# next(stall) only "Stall closed, No more chai" gets printed
print(next(stall)) # Both the lines get printed 

stall.close() # Clean up
