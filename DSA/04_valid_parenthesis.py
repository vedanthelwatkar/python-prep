"""
Valid Parenthesis Checker
Time Complexity: O(n)
Space Complexity: O(n)
"""

def valid_parenthesis(string):
    """
    Check if parenthesis/brackets are valid and balanced.
    Uses stack-based approach.
    """
    hashmap = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    stack = []

    for char in string:
        if char in hashmap:
            # If closing bracket
            if not stack or stack[-1] != hashmap[char]:
                return False
            stack.pop()
        else: 
            # If opening bracket
            stack.append(char)

    return len(stack) == 0

# Test cases
print("Valid Parenthesis '{}[]{':", valid_parenthesis("{}[]{"))
print("Valid Parenthesis '{}':", valid_parenthesis("{}"))
print("Valid Parenthesis '([{}])':", valid_parenthesis("([{}])"))
