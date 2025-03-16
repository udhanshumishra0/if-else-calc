num1 = int(input ("Enter the first number = "))
num2 = int(input ("Enter the second number = "))
op = input ("Enter the operator = ")

if op == "+" :
    print ("addition of these 2 numbers is -> ", num1+num2)
elif op == "-":
        print ("subtraction of these 2 numbers is -> ", num1-num2)
elif op == "*":
            print ("multiplication of these 2 numbers is -> ", num1*num2)
elif op == "/":
                print ("division of these 2 numbers is -> ", num1/num2)
elif op == "%":
                    print ("modulus of these 2 numbers is -> ", num1%num2)
else : print("Please enter a valid operator")
