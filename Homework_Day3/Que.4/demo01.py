def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "division by zero is not possible"
    return a/b
while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter a choice:"))
    if choice==5:
        print("Exit program")
        break
    a=int(input("Enter the number first:"))
    b=int(input("Enter the number second:"))
    if choice==1:
        print("Result:",add(a,b))
    elif choice==2:
        print("Result:",sub(a,b))
    elif choice==3:
        print("Result:",multiply(a,b))
    elif choice==4:
        print("Result:",division(a,b))
    else:
        print("Invalid choice")

