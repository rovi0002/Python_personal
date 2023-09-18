# main.py

import cycle1
import division

def main():
    cycle = 1
    while cycle <= 2:
        dividend, divisor = cycle1.cycle1_attempt(cycle)

        if dividend is not None and divisor is not None:
            quotient, remainder = division.calculate_division_remainder(dividend, divisor)
            divisors_to_check = [2, 3, 4, 5, 6, 7, 8, 9]
            divisibility_results = division.is_divisible(dividend, divisors_to_check)

            print(f"The result of {dividend} divided by {divisor} is {quotient} with a remainder of {remainder}")

            divisible_by = [d for d in divisors_to_check if divisibility_results[d]]
            not_divisible_by = [d for d in divisors_to_check if not divisibility_results[d]]

            if divisible_by:
                divisible_str = ', '.join(map(str, divisible_by))
                if len(divisible_by) > 1:
                    divisible_str = ', and '.join([', '.join(map(str, divisible_by[:-1])), str(divisible_by[-1])])
                print(f"{dividend} is divisible by {divisible_str}.")
            if not_divisible_by:
                not_divisible_str = ', '.join(map(str, not_divisible_by))
                if len(not_divisible_by) > 1:
                    not_divisible_str = ', and '.join([', '.join(map(str, not_divisible_by[:-1])), str(not_divisible_by[-1])])
                print(f"{dividend} is not divisible by {not_divisible_str}.")

        else:
            break

        cycle += 1

if __name__ == "__main__":
    main()
