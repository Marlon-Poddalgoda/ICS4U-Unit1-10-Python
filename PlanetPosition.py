#!/usr/bin/env python3

# Created by: Marlon Poddalgoda
# Created on: 2021-05-05
# This program finds the position of a planet using enumerated types.

# enum import statement
from enum import Enum


# enum function
def enumFunction(planet_position):
    # Assigns the planet number to a variable

    # assigning statement
    planet_num = planets[planet_position]

    # Return statement
    return planet_num.value


# enum class
class planets(Enum):
    # this contains all the planets as constants

    # mercury, the first planet
    MERCURY = 1

    # Venus, the second planet
    VENUS = 2

    # Earth, the third planet
    EARTH = 3

    # Mars, the fourth planet
    MARS = 4

    # Jupiter, the fifth planet
    JUPITER = 5

    # Saturn, the sixth planet
    SATURN = 6

    # Uranus, the seventh planet
    URANUS = 7

    # Neptune, the eighth planet
    NEPTUNE = 8

    # Pluto, the ninth "planet"
    PLUTO = 9


def main():
    # This program takes in user input
    try:
        # Asks user to input a planet name
        # input
        user_input = input("Enter the name of a planet in the solar system: ")

        # Capitalizes inputted string
        planet_position = user_input.upper()
        # Function call
        planet_output = enumFunction(planet_position)

        # Prints out the planet position to the console
        # output
        print("\n")
        print("The planet " + str(user_input) + " is number "
        + str(planet_output) + " in the solar system.")

    # Runs if someone enters something other than a planet
    except Exception:
        # output
        print("\n")
        print("Sorry, that's not a planet name. Try again.")

    # print done
    print("\n")
    print("Done.")


if __name__ == "__main__":
    main()
