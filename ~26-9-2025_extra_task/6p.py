# Divisibility Test - Check if a number is divisible by 3, 5, or both.
num = int(input("Enter the number "))
if num %3 == 0:
    if num %5 == 0:
        print("Your number is divided by 3 and 5 ")
    else:
        print("Your number is divided by just 3 ")
else:
    if num %5 == 0:
        print("your number is divided by just 5 ")
    else:
        print("your number is not divisible by '3' and '5' ")
