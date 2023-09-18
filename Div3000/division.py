def calculate_division(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "No dividing by 0, duh."


def calculate_division_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


def is_divisible(dividend, divisors):
    results = {}
    for divisor1 in divisors:
        results[divisor1] = dividend % divisor1 == 0
    return results
