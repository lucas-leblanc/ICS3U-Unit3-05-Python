# Copyright (c) 2022 Lucas LeBlanc All rights reserved.
#
# Created by: Lucas LeBlanc
# Created on: Oct 2022
# ICS3U-Unit3-05.py File, learning select cases in python.


def main():

    # input and variables
    month_number = int(input("Enter the number of the month(ex: 11 for November): "))

    # process and output
    print("")
    match month_number:
        case 1:
            print("The {0}st month is January.".format(month_number))
        case 2:
            print("The {0}nd month is February.".format(month_number))
        case 3:
            print("The {0}rd month is March.".format(month_number))
        case 4:
            print("The {0}th month is April.".format(month_number))
        case 5:
            print("The {0}th month is May.".format(month_number))
        case 6:
            print("The {0}th month is June.".format(month_number))
        case 7:
            print("The {0}th month is July.".format(month_number))
        case 8:
            print("The {0}th month is August.".format(month_number))
        case 9:
            print("The {0}th month is September.".format(month_number))
        case 10:
            print("The {0}th month is October.".format(month_number))
        case 11:
            print("The {0}th month is November.".format(month_number))
        case 12:
            print("The {0}th month is December.".format(month_number))
        case _:
            print("The number has to be a natural number between 1 to 12.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
