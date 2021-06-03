"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

Example 3:
Input: s = "IX"
Output: 9

Example 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


def rom_to_num(s):
    def rom_num(s_):
        if s_ == "I":
            ans_ = 1
            return ans_
        elif s_ == "V":
            return 5
        elif s_ == "X":
            return 10
        elif s_ == "L":
            return 50
        elif s_ == "C":
            return 100
        elif s_ == "D":
            return 500
        elif s_ == "M":
            return 1000
    num = 0
    i = 0
    while i < len(s):
        if s[i] == "I":
            if (i+1 < len(s)) and (s[i+1] == "X"):
                num += rom_num("X") - rom_num("I")
                i += 1
            elif (i+1 < len(s)) and (s[i+1] == "V"):
                num += rom_num("V") - rom_num("I")
                i += 1
            else:
                num += rom_num(s[i])
        elif s[i] == "V":
            num += rom_num(s[i])
        elif s[i] == "X":
            if (i+1 < len(s)) and (s[i+1] == "L"):
                num += rom_num("L") - rom_num("X")
                i += 1
            elif (i+1 < len(s)) and (s[i+1] == "C"):
                num += rom_num("C") - rom_num("X")
                i += 1
            else:
                num += rom_num("X")
        elif s[i] == "L":
            num += rom_num("L")
        elif s[i] == "C":
            if (i+1 < len(s)) and (s[i+1] == "D"):
                num += rom_num("D") - rom_num("C")
                i += 1
            elif (i+1 < len(s)) and (s[i+1] == "M"):
                num += rom_num("M") - rom_num("C")
                i += 1
            else:
                num += rom_num("C")
        elif s[i] == "D":
            num += rom_num("D")
        elif s[i] == "M":
            num += rom_num("M")
        i += 1
    return num


# s = 'XIX'
# s = 'XLIX'
# s = 'XCIV'
# s = 'CL'      # 150
# s = 'CD'      # 400
# s = 'CMXL'    # 940
# s = 'MIXIV'   # 1013
# s = "DCXXI"   # 621
print(rom_to_num(s))
