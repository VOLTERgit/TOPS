# Temperarute Advisor
"""
temp < 0 -> "Freezing" 
0 > temp < 10 -> "Cold"
10 < temp < 25 -> "Pleasant"
> 25 -> "Hot"
"""
temp = int(input("Enter your Temp : "))
if temp <= 0:
    print(f"Freezing")
elif 0 < temp <= 10:
    print(f"Cold") 
elif 10 < temp <= 25:
    print(f"Pleasant")
elif temp > 25:
    print(f"Hot")

