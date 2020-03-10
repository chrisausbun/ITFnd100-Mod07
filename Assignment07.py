# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with "Error Handling" and "Pickling .dat Files"
# ChangeLog (Who,When,What):
# Chris Ausbun,03.06.2020,Created script
# Chris Ausbun,03.06.2020,Added code to complete assignment 7
# Chris Ausbun,03.09.2020,Modified code to complete assignment 7
# ---------------------------------------------------------------------------- #

import pickle
import sys

# Declare variables and constants

objFile = 'AppData.dat'
lstNumbers = []

# Data ----------------------------------------------------------------------- #
try:
    print("Please pick a number between 10 and 100")
    floatFirstNumber = float(input())
except ValueError:
    print("I'm sorry but that's not a number!!")
else:
    if floatFirstNumber < 10 or floatFirstNumber > 100:
        print("I'm sorry, value not accepted!")
        input("\nPress any key to exit and try again")
        sys.exit()
    else:
        try:
            print("Please pick a second number between 1 and 10")
            floatSecondNumber = float(input())
        except ValueError as v:
            print("I'm sorry but that's not a number!!")
            input("\nPress any key to exit and try again")
            sys.exit()
        else:
            if floatSecondNumber < 1 or floatSecondNumber > 10:
                print("I'm sorry, value not accepted!")
                sys.exit()
            else:
                print("Congratulations, values have been accepted!!")
                print()
                lstNumbers = ["First Number Selected is: " + floatFirstNumber.__str__() + ", " +
                              "Second Number Selected is: " + floatSecondNumber.__str__() + "\n"]
                print(lstNumbers)
                try:
                    f = open('AppData.dat', 'r+')
                except FileNotFoundError as e:
                    print("Text file must exist before running this script!!")
                    print("Please create AppData.dat file in same directory as script, then execute the script!")
                    print("Built-In Python error info: ")
                    print(e, e.__doc__, type(e), sep='\n')
                    sys.exit()
                else:
                    objFile = open("AppData.dat", "wb")
                    pickle.dump(lstNumbers, objFile)
                    objFile.close()

                    objFile = open("AppData.dat", "rb")
                    objFileData = pickle.load(objFile)
                    objFile.close()

# Processing  --------------------------------------------------------------- #
                    print()
                    intSum = floatFirstNumber + floatSecondNumber
                    intDifference = floatFirstNumber - floatSecondNumber
                    intProduct = floatFirstNumber * floatSecondNumber
                    intQuotient = floatFirstNumber / floatSecondNumber


# Presentation (Input/Output)  -------------------------------------------- #
                    print("The sum of", floatFirstNumber, "and", floatSecondNumber, "is equal to:", intSum)
                    print("The difference of", floatFirstNumber, "and", floatSecondNumber, "is equal to:", intDifference)
                    print("The product of", floatFirstNumber, "and", floatSecondNumber, "is equal to:", intProduct)
                    print("The quotient of", floatFirstNumber, "and", floatSecondNumber, "is equal to:", intQuotient)
