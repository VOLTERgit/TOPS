# pass/fail - Take marks as input and determine if a student has passed (>40).
num1 = int(input("Enter your Marks "))
if num1 > 40:
    print(f"Your are pass the Exam ")
elif num1 <= 40:
    print(f"Your are fail in the Exam ")
else:
    print(f"Plz enter the proper marks(Number) ")
    
