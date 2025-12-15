def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num =int(input("Enter a number:"))
print("Factorial=",factorial(num))

def power(b,e):
    if e==0:
        return 1
    else:
        return b*power(b,e-1)
a=int(input("Enter a base:"))
b=int(input("Enter a exponent:"))
print("Power=",power(a,b))