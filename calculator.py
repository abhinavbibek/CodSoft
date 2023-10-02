operand1 = int(input("enter the first operand:"))
print (operand1)
operator = input("enter your operator:")
print (operand1,'', operator)
operand2 = int(input("enter your second operand:"))
print (operand1,operator,operand2,'= ',end='')
if (operator == '+'):
    print(operand1+operand2)
elif (operator == '-'):
    print(operand1-operand2)
elif (operator == '*'):
    print(operand1*operand2)
elif (operator == '/'):
    print(operand1/operand2)
elif (operator == '%'):
    print(operand1%operand2)
else:
    print("\n")
    print("invalid choice of operand or operator")