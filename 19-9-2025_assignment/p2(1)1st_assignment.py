num = int(input("Enter your 1st Number :"))
num1 = int(input("Enter your 2nd Number :"))

enter = input("Enter The Arithmetic Opreters e.g(+,-,*,/,%) ")

if enter == "+":

    num += num1
    print(f"you are selecting + so your answer is :{num}")
 
elif enter == "-":

    num -= num1
    print(f"you are selecting - so your answer is :{num}")

elif enter == "*":

    num *= num1
    print(f"you are selecting * so your answer is :{num}")

elif enter == "/":

    num /= num1
    print(f"you are selecting / so your answer is :{num}")
 
elif enter == "%":
    
    num %= num1
    print(f"you are selecting % so your answer is :{num}")
    
else:
    print(f"You are enter the wrong Arithmetic '{enter}' opreters e.g(+,-,*,/,%) ")
