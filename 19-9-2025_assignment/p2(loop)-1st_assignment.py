
num = int(input("Enter your 1st Number :"))
num1 = int(input("Enter your 2nd Number :"))
ans = 0
for i in range(5):
    enter = input("Enter The Arithmetic Opreters e.g(+,-,*,/,%) ")

    if enter == "+":

        ans = num + num1
        print(f"you are selecting + so your answer is :{ans}")
    
    elif enter == "-":

        ans = num - num1
        print(f"you are selecting - so your answer is :{ans}")

    elif enter == "*":

        
        ans = num * num1
        print(f"you are selecting * so your answer is :{ans}")


    elif enter == "/":

        ans = num / num1
        print(f"you are selecting / so your answer is :{ans}")
    
    elif enter == "%":
        
        ans = num %  num1
        print(f"you are selecting % so your answer is :{ans}")
        
    else:
        print(f"You are enter the wrong Arithmetic '{enter}' opreters e.g(+,-,*,/,%) ")

