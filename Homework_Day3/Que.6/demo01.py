def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        return"Division by zero"
    return a/b
def calculate(operand1, operand2, operation):
    return operation(operand1,operand2)
print("Addition:",calculate(2,3,add))
print("Substraction:",calculate(2,3,sub))
print("Multiplication:",calculate(2,3,multiply))
print("Division:",calculate(2,3,division))
print("Division by zero:",calculate(10,0,division))