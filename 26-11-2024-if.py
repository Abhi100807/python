x = input("enter the char: ").lower()
if x in "aieou":
    print(f"{x} is the vowel")
elif x.isalpha():
    print(f"{x} is consonant")
else:
    print("pls enter only char")      
