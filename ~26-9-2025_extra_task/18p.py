# Car rental charges - 
"""
sedan: rs. 1000/ day, SUV: rs 1500/day, Hatchback: rs.800/day
if rental days > 5-> 10% discount
"""
# sedan = 1000
# suv = 1500
# hatchback = 800
amount = 0
discount = 0 
cars = str(input(" Plz select which types of car you want a rent (sedan , suv , hatchback)"))
days = int(input("How many days you want to rental your car : "))
if days > 5 and cars == "sedan":
    amount = 1000*days
    discount = amount/10
    amount -= discount
    print(f"Your amount with the discount price {discount} & total price {amount}")
elif days > 5 and cars == "suv":
    amount = 1500*days
    discount = amount/10
    amount -= discount  
    print(f"Your amount with the discount price {discount} & total price {amount}")
elif days > 5 and cars == "hatchback":
    amount = 800*days
    discount = amount/10
    amount -= discount
    print(f"Your amount with the discount price {discount} & total price {amount}")
else:
    amount *= days
    print("Your amount is {amount}")



