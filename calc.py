def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2

def multiply(n1,n2):
    return n1*n2
operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

num1=int(input("first number"))
num2=int(input("second number"))
for i in operation:
    print(i)
a=(input("pick an operator from the line above"))
calculation_function=operation[a]
answer=calculation_function(num1,num2)
print(f"{num1}{a}{num2} = {answer}")

ye='yes'
while ye=='yes':
    ye=str(input("do you want to continue??????"))
    if ye.lower()=="yes":
        num3=int(input("next number-"))
        a=(input("pick an operator"))
        calculation_function=operation[a]
        answer=calculation_function(answer,num3)
        print(answer)
    elif ye.lower().strip()=="no":
        print("OK BYE, PRESS ENTER TO LEAVE")
        exit(0)
