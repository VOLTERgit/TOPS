#Grade calculator - Based on marks , print grades :
# >= 90 -> A
# >= 75 -> B
# >= 50 -> c
# < 50 -> f

marks = int(input("Enter the number : "))
if marks >= 90:
    print("A grade")
elif marks >= 75:
    print("B grade")
elif marks >= 50:
    print("C grade")
elif marks < 50:
    print("F grade")
