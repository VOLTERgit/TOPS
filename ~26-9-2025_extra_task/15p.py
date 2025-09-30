# Electricity Bill Calculator - Units consumed:
"""
< 100 -> rs.5/unit
101 - 200 -> rs.7 / unit
201 - 500 -> rs.10 / unit
> 500 -> rs 15/unit
"""

price = 0
for i in range(1,6):
    unit_used = int(input("Enter your Electicity unit : "))
    if unit_used <= 100:
        price = unit_used * 5
    elif unit_used <= 200:
        price = unit_used * 7
    elif unit_used <= 500:
        price = unit_used * 10
    else:
        price = unit_used * 15
    print (f"you electicity bill amount '{price}'")
    