# voting Eligibility - Check if a person is eligible to vote (age > 18)
age = int(input("Enter Your Age : "))
if age > 18:
    print("Your are eligible for voting ")
elif age <= 18:
    print("Your are not eligible for voting ")
else:
    print("Your Input is wrong just write a number ")