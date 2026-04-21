device_status = input("Device status ? - ").lower() 


if device_status == 'active':
    temperature = int(input("Temperature ?  - "))
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Tempurature normal")
else:
    print("Device is offline")