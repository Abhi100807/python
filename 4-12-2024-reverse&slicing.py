# Create a list of strings
string_list = input("Enter strings separated by commas: ").split(',')

# Reverse the list using reverse()
reverse_method_list = string_list.copy()  # Copy the list to preserve original
reverse_method_list.reverse()
print("Reversed using reverse():", reverse_method_list)

# Reverse the list using slicing
slicing_method_list = string_list[::-1]
print("Reversed using slicing [::-1]:", slicing_method_list)

# Compare the results
are_equal = reverse_method_list == slicing_method_list
print("Are the two methods' results equal?", are_equal)

