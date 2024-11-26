string1 = input("enter the string1: ")
string2 = input("enter the string2: ")
if len(string1)!=len(string2):
    print("they are not anagram strings")
else:
    if sorted(string1)==sorted(string2):
        print("the strings are anagrams")
    else:
        print("the strings are not anagrams")    

