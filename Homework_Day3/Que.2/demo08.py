text = input("Enter a string: ")

print("1.first 5 character:")
print("2.last 5 character:")
print("3.reverse a string:")
print("4.character at even index:")
print("5.character at odd index:")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(text[:5])
elif choice == 2:
    print(text[-5:])
elif choice == 3:
    print(text[::-1])
elif choice == 4:
    print(text[::2])
elif choice == 5:
    print(text[1::2])
else:
    print("Invalid choice")
