num1 = int(input ("Enter the first number = "))
num2 = int(input ("Enter the second number = "))
op = input ("Enter the operator = ")

choice = int(input ("how would you like to continue this? we have 2 methode mentioned below. Choose!! \n 1. if else\n2. switch case"))
if choice == 1 :
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
elif choice == 2 or choice != 2 :
    print "Ha ha ha, we dont have switch case in python"
