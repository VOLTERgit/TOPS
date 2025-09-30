# Bank ATM - 
"""
Input balance and withdrawal amount. 
check if balance is sufficient and withdrawal < daily limit.
"""
balance = int(input("Enter the your balance : "))
daily_limit = 10000
for i in range(6):
    
    withdrawal = int(input("Enter the Withdrawal amount : "))
    if  balance > withdrawal >= 1 : # if 0 < balance < withdrawal:
        
        if withdrawal <= daily_limit:
            daily_limit -= withdrawal
            balance -= withdrawal
            print("Withdrawal amount is complited !!!")
        else:
            print(" You complited your daily limit ")
    else:
        print("You did not have sufficient balance for withdrawal amount !!!")
    print(f"--Now Your Balance is {balance} and your Daily limit is remind - {daily_limit} --")
