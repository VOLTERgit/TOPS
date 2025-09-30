# Leap Year Check - A year is a leap year if divisible by 4 but not 100 unless divisible by 400.

year = int(input("Enter the year : "))
if year %4 == 0:
    print("It's a leap year ")
else:
    print("it's not a leap year ")

