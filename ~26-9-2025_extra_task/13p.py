# Ticket Booking -
"""
age < 5 -> Free Ticket
age 5-8 -> child ticket
age 18-60 -> Adult ticket
age > 60 -> sonior citizen ticket
"""
ticket_price = 100
age = int(input("Enter the your age - "))
if age <= 5:
   ticket_price = 0 
   print(f"Your ticket price is {int(ticket_price)} rs - it's Free Ticket ")
elif 5 < age <= 8:
   ticket_price /=3
   print(f"Your ticket price is {int(ticket_price)} rs for Child ticket ")
elif 8 < age <= 17:
   ticket_price /=2
   print(f"Your ticket price is {int(ticket_price)} rs for Adult ticket ")
elif age > 60:
   ticket_price /= 2
   print(f"Your ticket price is {int(ticket_price)} rs senior citizen ticket ")
# print(f"Your ticket price is {int(ticket_price)}")
