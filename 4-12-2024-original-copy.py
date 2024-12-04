# Creating a list of numbers
original_list = [1, 2, 3, 4, 5]

# Assigning the list to another variable (aliasing)
second_list = original_list

# Modifying the original list
original_list.append(6)

# Checking if the second list also changes
print("Original List after modification:", original_list)  # Output: [1, 2, 3, 4, 5, 6]
print("Second List after modification:", second_list)    # Output: [1, 2, 3, 4, 5, 6]

# Creating a copy of the original list (cloning)
copied_list = original_list.copy()

# Modifying the copied list
copied_list.append(7)

# Checking that the copied list modification does not affect the original list
print("Original List after copying and modifying the copy:", original_list)  # Output: [1, 2, 3, 4, 5, 6]
print("Copied List after modification:", copied_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
