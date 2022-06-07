#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: june.4.2022
# Program gets numbers from user
# then displays the product


import constants


def calc_product(list_of_num):

    # calculate the product in the list
    sum = 1

    # calculate product of the list
    for number in list_of_num:
        sum = sum * number
    try:
        product = sum
    except ZeroDivisionError:

        # sees if list is empty
        product = -1
    return product


def main():

    # declaring a list
    num_list = []

    # Show what program does
    print("This program that asks the user for 5 numbers.")
    print("Then writes the product")
    print("")

    # declare counter
    counter = 0

    # loop to get input
    while True:

        input_string = input("Enter your numbers: ")
        try:

            # user input into float
            input_float = float(input_string)

            # Append the user input to the list
            num_list.append(input_float)
            counter = counter + 1

        except Exception:

            print("Invalid input, try again.")
            continue

        # Allows user to enter a  cetain amout of numbers
        if counter >= constants.MAX_NUM:
            break

    # assigns variable to function call
    list_product = calc_product(num_list)

    # displays results to user
    print("")
    print("The product is {}" .format(list_product))


if __name__ == "__main__":
    main()
