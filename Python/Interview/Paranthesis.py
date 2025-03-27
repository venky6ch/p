def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            # Pop the top element from the stack if it's not empty; otherwise, use a dummy value
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            # Push the current character onto the stack
            stack.append(char)

    # If the stack is empty, the parentheses are balanced
    return not stack


# Example usage:
s = input("Enter a string of parentheses: ")
if is_valid_parentheses(s):
    print("The string has valid parentheses.")
else:
    print("The string has invalid parentheses.")
