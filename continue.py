#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program loops and adds multiple numbers


def main():
    # This function loops and adds multiple numbers
    # process
    while True:
        # Input
        input_amount_string = input("Enter how many numbers you "
                                    "want add together: ")
        try:
            input_amount = int(input_amount_string)
            break
        except Exception:
            print("This was not an integer")

    number_sum = 0
    loop_counter = 0

    while loop_counter < input_amount:
        loop_counter = loop_counter + 1

        # Input
        while True:
            chosen_number_string = input("Enter your chosen integer: ")

            try:
                chosen_number = int(chosen_number_string)
                assert chosen_number > 0
                break
            except AssertionError:
                print("Integer wasn't positive")
            except Exception:
                print("This was not an integer")

        number_sum = number_sum + chosen_number

        if loop_counter < input_amount:
            continue

        print("")
        print("The sum of all numbers are: {}".format(number_sum))


if __name__ == "__main__":
    main()
