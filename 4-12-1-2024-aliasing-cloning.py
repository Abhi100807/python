#aliasing
x = eval(input("enter the list1: "))
y = x
y.append(4)
print(x)

#cloning

a = eval(input("enter the a list: "))
s = a.copy()
s.append(4)
print(a)
print(s)