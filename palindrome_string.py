# To check if the given string is palindrome or not.
def palindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] == s[len(s)-i-1]:
            continue
        else:
            return False
    return True


# Test
s = 'abababa'
print(palindrome(s))
