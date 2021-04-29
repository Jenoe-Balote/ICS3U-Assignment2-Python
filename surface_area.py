#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on April 2021
# This program calculates the surface area of a rectangular prism
#       with dimensions inputted from the user


def main():
    # this function calculates the surface area

    # input
    print("Welcome! Let's calculate the surface area of a rectangular prism!")
    print("Follow the prompts down below to get your answer.")
    print("")
    length = int(input("Enter the length of the rectangular prism (cm): "))
    width = int(input("Enter the width of the rectangular prism (cm): "))
    height = int(input("Enter the height of the rectangular prism (cm): "))

    # process
    area = 2 * ((length * width) + (height * length) + (height * width))

    # output
    print("")
    print("The surface area is {0} cm².".format(area))
    print("")
    print("Thanks for using this program, catch you later!")


if __name__ == "__main__":
    main()
