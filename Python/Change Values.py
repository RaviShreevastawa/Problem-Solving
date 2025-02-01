a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

print(f"The values before exchange {a} and {b}")

# Exchange the values of a and b without using the third variable
a = a-b
b = a+b
a = b-a

print(f"The values after the exchange of {a} and {b} ")