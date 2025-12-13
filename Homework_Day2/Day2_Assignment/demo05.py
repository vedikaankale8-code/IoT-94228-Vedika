def print_binary(n):
    if n>1:
        print_binary(n//2)
    print(n % 2,end="")
num=int(input("Enter a number:"))
print_binary(num)
    