my_phones = {"Samsung s9+", "Iphone 14+", "Iphone 13"}
frind_phones = {"Google pixel", "Iphone 13"}


all_phones = my_phones | frind_phones
print(all_phones)

common_phones = my_phones & frind_phones
print(common_phones)

only_my_phones_uncommon  = my_phones - frind_phones
print(only_my_phones_uncommon)

print(f"Is 'Iphone 14+' in friend phone ? {'Iphone 14+' in frind_phones}")

