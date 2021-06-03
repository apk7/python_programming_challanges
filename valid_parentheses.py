# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def isValid(s):
    len_s = len(s)
    if len_s % 2 != 0:
        return False

    temp_length = 100
    counter = 0
    while len(s) > 0:
        s = s.split("()")
        s = ''.join(s)
        s = s.split("{}")
        s = ''.join(s)
        s = s.split("[]")
        s = ''.join(s)

        if temp_length > len(s):
            temp_length = len(s)
        elif temp_length == len(s):
            counter += 1
            if counter > 10 and len(s) != 0:
                return False
    return True


ss = [
    "()",
    "()[]{}",
    "({}[)](",
    "{()[[]{}]{{([])}}}",
]

for s in ss:
    print(isValid(s), '\t- ', s)
print("Complete")
