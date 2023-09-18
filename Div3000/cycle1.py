# defining cycle1 function + creating max attempts
def cycle1_attempt(cycle_number):
    max_attempts = 3
    attempts = 0
    # comparing rt attempts with max attempts
    while attempts < max_attempts:
        try:  # trying input on being a number
            if cycle_number == 1:
                dividend = input("Welcome to Div3000. Enter a dividend or type 'exit' to exit: ")
            else:
                dividend = input("Enter a dividend or type 'exit' to exit: ")

            # if input is 'exit', cycle exits
            if dividend.lower() == "exit":
                return None, None
            # turning divisor into integer value
            dividend = int(dividend)

            while True:  # if dividend is a number, this loop gives 3 attempts at giving int divisor
                try:
                    divisor = int(input("Enter a number you want to divide by: "))
                    break
                except ValueError:
                    if attempts == 0:
                        print("Nuh uh. A number. Right here: ")
                    elif attempts == 1:
                        print("Stop. Just give me a number.")
                    else:
                        print("Ok, enough.")
                        return None, None

                attempts += 1

            return dividend, divisor

        except ValueError:
            if attempts == 0:
                print("A N-U-M-B-E-R. Right. Here: ")
            elif attempts == 1:
                print("Don't.")
            else:
                print("Alright. Back to 1st grade, you, clown.")

        attempts += 1

    print("I don't have time for this.")
    return None, None
