"""
In Python, float('inf') represents positive infinity as a floating-point number.
It signifies a value that is mathematically infinite and larger than any other number.
This representation is useful in various scenarios, including:

Initialization:
Setting a variable to infinity is useful when you need a starting value that is guaranteed
to be larger than any other value in a comparison or iterative process.
"""

positive_infinity = float("inf")
negative_infinity = float("-inf")

print(positive_infinity)  # Output: inf
print(negative_infinity)  # Output: -inf

# Comparison
print(1000 < positive_infinity)  # Output: True
print(-1000 > negative_infinity)  # Output: True
