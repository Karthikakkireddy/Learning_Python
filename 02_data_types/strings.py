
# name = "Karthik"
# print(name)
# print("Name : name")
# print("Name : {name}")
# print(f"Name : {name}")

# Indexing and Slicing 
print("---------------------------------------")

name = "Karthik Akkireddy"
print(f"First Name : {name[0:7]}") 

print(f"First Name : {name[:]}") # All 
print(f"First Name : {name[::]}") # All (same)

print(f"First Name : {name[0:7:1]}") # Go on the every 1st index
print(f"First Name : {name[0:7:2]}") # Go on the every 2nd index


print(f"First Name : {name[::-1]}") # Reverse

print(f"First Name : {name[4:1]}") # IF start > end and the string is forward direction then empty string is result 
print(f"First Name : {name[4:1:-1]}") # Index order : 4 -> 3 -> 2 (htr)
print(f"First Name : {name[1:4:-1]}") #  IF start <  end and the string is backward direction then empty string is result 

print("---------------------------------------")

# Encoding and Decoding
text = "Hällo"
encoded_text = text.encode("utf-8")
print(f"Non encoded text : {text}")
print(f"Encoded text : {encoded_text}")

decoded_text = encoded_text.decode("utf-8") 
print(f"Decoded text : {decoded_text}")

