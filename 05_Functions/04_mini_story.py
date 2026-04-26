
bill = [5000, 330, 765]

def add_vat(price , vat_rate):
    return price * (100 + vat_rate)/100



for idx, bill in enumerate(bill, start = 1):
    total_bill = add_vat(bill, 10)


    print(f"Original: {bill}, Order number {idx} bill : {total_bill}")