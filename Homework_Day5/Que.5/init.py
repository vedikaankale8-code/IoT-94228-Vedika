from arithmetic import add, multiply
from string_ops import reverse_string, count_vowels

# Arithmetic operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))

# String operations
text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))
print("Vowel Count:", count_vowels(text))
