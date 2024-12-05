# Creating an original list
original_list = [1, 2, 3, 4, 5]

# Creating an alias of the original list
alias_list = original_list

# Creating a clone of the original list
cloned_list = original_list.copy()

# Display initial lists
print("Initial lists:")
print(f"Original List: {original_list}")
print(f"Alias List: {alias_list}")
print(f"Cloned List: {cloned_list}\n")

# Modify the alias list
alias_list[0] = 100

# Display lists after modifying alias list
print("After modifying alias list:")
print(f"Original List: {original_list}")
print(f"Alias List: {alias_list}")
print(f"Cloned List: {cloned_list}\n")

# Modify the cloned list
cloned_list[1] = 200

# Display lists after modifying cloned list
print("After modifying cloned list:")
print(f"Original List: {original_list}")
print(f"Alias List: {alias_list}")
print(f"Cloned List: {cloned_list}")
