# Largest of three numbers - input 3 numbers and find the largest using nested if.
numA = int(input("Enter the 1st number : "))
numB = int(input("Enter the 2nd number : "))
numC = int(input("Enter the 3rd number : "))

if numA < numB:
    if numB < numC:
        print("3rd Number is bigger ")
    else:
        print("2nd Number is Bigger ")
elif numC < numA:
    if numB < numA:
        print("1rd Number is bigger ")
    else:
        print("2rd Number is Bigger ")
else:
    print("3rd Number is Bigger ")
