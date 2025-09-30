
num = int(input("Enter your 1st Number :"))
num1 = int(input("Enter your 2nd Number :"))

enter = input("Enter the Arithmetic opreters e.g(+,-,*,/,%) ")

if enter == "+":

    num += num1
    print(f"you are selecting + so your answer is :{num}")
 
if enter == "-":

    num -= num1
    print(f"you are selecting - so your answer is :{num}")

if enter == "*":

    num *= num1
    print(f"you are selecting * so your answer is :{num}")

if enter == "/":

    num /= num1
    print(f"you are selecting / so your answer is :{num}")

if enter == "%":

    num %= num1
    print(f"you are selecting % so your answer is :{num}")

    
else:
    print()
