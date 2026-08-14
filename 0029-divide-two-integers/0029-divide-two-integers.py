class Solution(object):
    def divide(self, dividend, divisor):

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        # Subtract divisor using powers of 2
        while dividend >= divisor:
            value = divisor
            multiple = 1

            while dividend >= value + value:
                value += value
                multiple += multiple

            dividend -= value
            result += multiple

        if negative:
            result = -result

        # 32-bit integer range
        if result < -(2**31):
            return -(2**31)

        if result > 2**31 - 1:
            return 2**31 - 1

        return result