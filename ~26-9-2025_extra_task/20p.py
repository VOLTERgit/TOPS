"""
Student Scholarship Eligibility -

Marks > 90 -> Full scholarship
Marks > 70 -> Haif Scholarship if family incom < 5 LPA
Else -> No Scholarship
"""
family_incom = int(input("Enter your family incom per year : "))
marks = int(input("Enter Your marks : "))
if marks > 90:
    print("you are eligible for scholarships ")
elif marks > 70:
    if family_incom < 500000:
        print("You are eligible for scholarships")
    else: 
        print("sry, your family financial status is better ")
else:
    print("sry, You are not eligible for scholarship try harder ")
