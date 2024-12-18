x = eval(input("enter the set1: "))
y = eval(input("enter the set2: "))
common_elemnts = x & y
if common_elemnts:
    print(f"yes they common element:{x & y}")
else:
    print("no common elements are there")
