# For this challenge you will determine if numbers within an array follow an
# arithmetic or geometric sequence.

def arith_geo(ls):
    for i in range(0, len(ls)-3):

        if ((ls[i+1] - ls[i]) == (ls[i+2] - ls[i+1]) == (ls[i+3] - ls[i+2])):
            ans = 1
        else:
            ans = 0

        try:
            if ((ls[i+1]/ls[i]) == (ls[i+2]/ls[i+1]) == (ls[i+3]/ls[i+2])):
                if ans == 1:
                    ans = 3
                else:
                    ans = 2
            else:
                ans += 0

        except ZeroDivisionError:
            # print("Error! List consists of 0! Not a GP")
            ans += 0

    return ans


ls = [
    [1, 4, 7, 10, 13, 16, 19],
    [2, 4, 8, 16, 32, 64],
    [1, 2, 4, 8, 16, 32, 64],
    [-1, 2, -4, 8, -16, 32, -64],
    [1, 0, -1, -2, -3, -4, -5],
    [3, 3, 3, 3, 3]
]

for ls_ in ls:
    print(arith_geo(ls_))
