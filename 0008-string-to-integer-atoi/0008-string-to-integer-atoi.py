class Solution(object):
    def myAtoi(self, s):

        s = s.strip()

        sign = 1
        i = 0
        result = 0

        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1

        elif i < len(s) and s[i] == "+":
            i += 1

        while i < len(s) and s[i].isdigit():

            result = result * 10 + int(s[i])

            i += 1

        result *= sign

        if result < -(2**31):
            return -(2**31)

        if result > (2**31) - 1:
            return (2**31) - 1

        return result