class Calculator:
    def add(self, num1, num2):
        while num2 != 0:
            carry = num1 & num2
            num1 = num1 ^ num2
            num2 = carry << 1
        return num1

    def subtract(self, num1, num2):
        while num2 != 0:
            borrow = (~num1) & num2
            num1 = num1 ^ num2
            num2 = borrow << 1
        return num1

    def multiply(self, num1, num2):
        result = 0
        while num2 != 0:
            if num2 & 1:
                result = self.add(result, num1)
            num1 = num1 << 1
            num2 = num2 >> 1
        return result

    def divide(self, dividend, divisor):
        quotient = 0
        sign = 1 if (dividend >= 0) == (divisor >= 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            dividend = self.subtract(dividend, divisor)
            quotient = self.add(quotient, 1)

        return sign * quotient
