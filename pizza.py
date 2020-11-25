#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program calculates the total cost for a given diameter pizza
import constants


def main():
    # this program calculates the total cost for a given diameter pizza

    # input
    diameter = int(input("Enter the diameter of the pizza you would " +
                         "like(inch):"))

    # process
    sub_total = (constants.LABOR + constants.RENT +
                 (diameter * constants.COST_PER_INCH))
    total = sub_total + (sub_total * constants.HST)

    # output
    print()
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
