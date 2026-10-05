def divide(dividend, divisor):
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    quotient = int(dividend / divisor)

    if quotient > INT_MAX:
        return INT_MAX
    if quotient < INT_MIN:
        return INT_MIN

    return quotient

dividend, divisor = map(int, input().split())
print(divide(dividend, divisor))
