# def serve_chai(flavour):
#     try:
#         print(f"Preparing {flavour} chai")
#         if flavour == "unknown":
#             raise ValueError("We do not have such flavour")
#         else:
#             print(f"Here is your {flavour} chai")
#     except ValueError as e:
#         print("Error : ", e)

# serve_chai("masala")
# serve_chai("unknown")

# def serve_chai2(flavour):
#     try:
#         print(f"Preparing {flavour} chai")
#         if flavour == "unknown":
#             raise ValueError("We do not have such flavour")
#         else:
#             print(f"Here is your {flavour} chai")
#     except ValueError as e:
#         print("Error : ", e)
#     finally:
#         print("Next Customer please\n")

# serve_chai2("masala")
# serve_chai2("unknown")


def serve_chai3(flavour):
    try:
        print(f"Preparing {flavour} chai")
        if flavour == "unknown":
            raise ValueError("We do not have such flavour")
    except ValueError as e:
        print("Error : ", e)
    else:
        print(f"Here is your {flavour} chai")
    finally:
        print("Next Customer please\n")

serve_chai3("masala")
serve_chai3("unknown")