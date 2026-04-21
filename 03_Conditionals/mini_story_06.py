seat_type = input("Seat type (sleeper/general/AC/luxury) - ").lower() 

match seat_type:
    case "sleeper" :
        print("Sleeper class booked")
    case "general" :
        print("General class booked")
    case "ac" :
        print("AC class booked")
    case "luxury":
        print("Luxury class booked")
    case _:
        print("Invalid seat type")
