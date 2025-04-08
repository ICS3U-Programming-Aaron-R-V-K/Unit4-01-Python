# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: March 08, 2025
# Is a while true program
# It gets the number from the use and adds + 1 from 0 to the user number and adds them all


def main():

    # get user number as a string
    user_num = input("Enter any number: ")

    # Set the sum of the number to start from 0 and counter as well
    sum_num = 0
    counter = 0

    # Try catch statement
    try:
        # Validate the input from the user is an integer
        int_num = int(user_num)

        # Validate that the number is positive
        if int_num < 0:
            print("Enter a positive num")

        else:

            # While statement if counter is less than the input number from the user
            while counter < int_num:

                # Calculation to add all numbers inside the user number
                counter = counter + 1
                sum_num = sum_num + counter

            # Else statement so that the program strops and dose not add numbers above the user number
            else:
                print("sum: {}".format(sum_num))

    # Exception if the user input is not a number
    except Exception:
        print("{}, is not a number".format(user_num))


if __name__ == "__main__":
    main()
