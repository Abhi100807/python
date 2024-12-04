x = eval(input("enter the list: "))
y = x[:3]
z = x[-3:]
a = x[1::2]
print(f"first three number are: {y}")
print(f"last three numbers are: {z}")
print(f"every second number in list: {a}")