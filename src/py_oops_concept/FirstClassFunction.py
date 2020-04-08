def divides(dividend, divisor):
    return dividend/divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 5, operator=divides)
print(result)