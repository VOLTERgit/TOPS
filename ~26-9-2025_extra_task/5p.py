#Discount check - if purchase amount > 500, apply 10% discount; else, no discount.
purchase_amount = int(input("Enter the purchese amount : "))
discount = 0
if purchase_amount > 500:
    discount = purchase_amount / 10
    print("This is your amount ",purchase_amount-discount)
else:
    print("sorry you can not git discount becouse you need to have perchess more than 500rs ")

