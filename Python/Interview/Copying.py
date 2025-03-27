import copy  # Importing the copy module for deep copying

# Original list
l1 = ["Asif", "Basit", "Arun", "Sajad"]

# Shadow Copy (Shallow Copy)
l2 = l1  # l2 now refers to the same memory location as l1
print("Before modification (Shallow Copy):")
print("l1:", l1)
print("l2:", l2)

# Modifying l1
l1[0] = "John"
print("\nAfter modification (Shallow Copy):")
print("l1:", l1)
print(
    "l2:", l2
)  # l2 also changes, proving that it's a shallow copy (both reference the same object)

# Deep Copy
l3 = copy.deepcopy(l1)  # Creating a completely separate copy
print("\nBefore modification (Deep Copy):")
print("l1:", l1)
print("l3:", l3)

# Modifying l1
l1[1] = "Michael"
print("\nAfter modification (Deep Copy):")
print("l1:", l1)
print("l3:", l3)  # l3 remains unchanged, proving it's a deep copy
