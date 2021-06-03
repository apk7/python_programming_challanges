# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

def longestCommonPrefix(strs):
    reference_item = strs[0]
    s = ''
    i = 0
    flag = True
    while i < len(reference_item):
        reference = reference_item[i]
        for compare in strs[1:]:
            if i < len(compare) and reference == compare[i]:
                flag = True
            else:
                flag = False
                return s
        if flag:
            s += reference
        i += 1
    return s


strs_ = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["123dog", "123racecar", "1234car"],
    ["flower", "flower", "flower"],
    ["f", "f", "f"],
    ["f"],
    ["reflower", "flower", "flower"],
    ["ab"]
]

for strs in strs_:
    print(longestCommonPrefix(strs))
