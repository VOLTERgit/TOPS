"""
Restaurant Bill with GST and Service charge - 
calculate GST 5% + service chage 10% based on food type (veg/Non-Veg) and bill amount.
"""
amount = int(input("Enter the ammount : "))
chargice = 0
total = 0
gst = 0
food_type = input("Enter the food types Veg / Non-Veg / Vegon :")

if food_type == "Veg" or food_type == "veg":
   chargice = amount *0.10
   gst = amount * 0.05
   total = amount + chargice + gst
   print(f"your bill amount is  {amount}")
   print(f"Your service cost is {chargice}")
   print(f"Your GST is ........ {gst}")
   print(f"Your total is ..... '{total}'!!!")

elif food_type == "Non-Veg" or food_type == "non-veg":
   chargice = amount * 0.15 
   gst = amount * 0.05
   total = amount +  chargice + gst
   print(f"your bill amount is  {amount}")
   print(f"Your service cost is {chargice}")
   print(f"Your GST is ........ {gst}")
   print(f"Your total is ...... '{total}'!!!")

elif food_type == "Vegon" or food_type == "vegon":
   chargice = amount * 0.20
   gst = amount * 0.05
   total = amount + chargice + gst
   print(f"your bill amount is  {amount}")
   print(f"Your service cost is {chargice}")
   print(f"Your GST is ........ {gst}")
   print(f"Your total is ...... '{total}'!!!")
