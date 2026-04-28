# favourite_chais =[
#     "Masala Chai", "Green Tea", "Masala Chai",
#     "Lemon Tea", "Green Tea", "Elaichi Chai"
# ]

# # unique_chai = {chai for chai in favourite_chais if True} - This also works
# unique_chai = {chai for chai in favourite_chais }
# print(unique_chai)

recipies = {
    "Masala Chai" : ["ginger", "cardamom", "clove"],
    "Elaichi Chai" : ["cardamom", "milk", "clove"],
    "Spicy Chai" : ["ginger", "black pepper", "clove"]
}

# spices = [spice for spice in recipies] # Get all the Keys 
# print(spices)

# spices = [spice for spice in recipies.values()] # Get all the spices from each Chai (KEY) - 1st Way 
# print(spices)
# spices = [recipies.get(spice) for spice in recipies] # Get all the spices from each Chai (KEY) - 2nd Way
# print(spices)

unique_spices = {spice for ingridients in recipies.values() for spice in ingridients}
print(unique_spices)