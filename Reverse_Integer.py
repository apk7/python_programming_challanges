# reversing integer

def reverse_integer(digits):
    if digits >= 0:
        digits = list(str(digits))
        digits.reverse()
    else:
        digits = list(str(digits))
        digits = digits[1:]
        digits.reverse()
        digits = ['-', *digits]

    rev_digits = int(''.join(digits))

    if (rev_digits > 2**(31)-1) or (rev_digits < -2**(31)):
        return 0
    else:
        return rev_digits


digits = -2341219
digits = 2341219
print(reverse_integer(digits))
