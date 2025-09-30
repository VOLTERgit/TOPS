# Simple login system - 
"""
input username and password.
if correct, print"Login successful " ; else, check if 
username is correct but password wrong -> print
"incorrect password".
"""
true_username = "Dhaval"
true_password = 1234
for i in range(5):
    username = str(input("Enter username :"))
    password = int(input("Enter password :"))

    if username == true_username and password == true_password:
        print ("Your Login Successful !!!")
    else:
        if password == true_password:
            print("Your username is incorrect ")
        elif username == true_username:
            print("Your password is wrong ")
    
print(f" You've made to many faild attempts ")
