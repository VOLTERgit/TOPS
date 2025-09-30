# Body Mass index (BMI) Calculator -
bmi = float(input("Enter the your BMI : "))
if bmi < 18.5:
    print("Your are Underweight ")
elif 18.5<bmi<25:
    print("Your are Normal :) ")
elif 25 <= bmi <30:
    print("Your are Overweight ")
elif bmi >= 30:
    print("Your are obese ")

