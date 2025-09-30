# shopping cart -
"""
if total > 100 -> 15% discount
Else if total > 500 -> 10% discount
Else -> no discount
"""
discount = 0
for i in range(5):
    amount = int(input("Enter Your amount : "))
    if amount > 100:
        if amount > 500:
            discount = amount/10
            print(f"Your discounted amount is {int(amount-discount)}")
        else:
            discount  = amount/15
            print(f"Your discounted amount is {int(discount-amount)}")
    else:
        print(f"sry no discount | plz add at least 101 amount")
    