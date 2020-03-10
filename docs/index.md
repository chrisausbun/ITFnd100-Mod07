# Error Handling & Pickling

**Dev:** 
*Chris Ausbun* 
**Date:** 
*03.09.2020*

## Introduction
The goal of this document and exercise is to add learn and understand how Error Handling is done by using Try Except blocks as well as Pickling and working with .dat files. I was able to create everything from following the “Intro to Python Mod07” video from the instructor (Root, R., Intro to Python Mod06, YouTube, 2019), as well as a few resources on the web (https://docs.python.org/3/library/exceptions.html,https://www.w3schools.com/python/python_try_except.asp, and https://realpython.com/python-exceptions/).

## Structured Error Handling (Try-Except)
Learned how to create a structured error handling by using the Try Except blocks. There were actually quite a few built-in functions that I found online but I decided to just use two in my script. I used the ValueError and FileNotFound built-in error functions. The ValueError evaulates whether or not a user is typing in a number or letters. The FileNotFound evaluates whether or not the file referenced in the script is there or missing. You can see how I used the Try Except block while evaluating the ValueError from Figure 1: Try Except ValueError Function.

## Pickling
Learned how to pickle data which is basically the concept of security by obscurity. Pickling data basically makes it not readable by text editors but can easily be de-obsecured by other means. Not sure if there’s a word for de-obsecured but hey, you get the idea. Oddly enough, the default text editor on Mac (TextEdit) does a very good job at reading the data. It pretty much makes out everything except for the carriage return. You can see my example of using Pickling in Figure 2: Pickling Data.

## Summary
After learning everything with Try Except blocks and Pickling, I was able to create an interactive python script file that asks the user for 2 numbers and adds does some simple math calculations while using both ValueError and FileNotFound error handling functions as well as pickles the two numbers selected in a .dat file that is obscured. I’ve added a few screenshots below of it working in PyCharm, Terminal, and shows the output of the .dat file. I've listed my code below, feel free to take a look at it.

Figure 1: https://raw.githubusercontent.com/chrisausbun/ITFnd100-Mod07/master/Screenshot%202020-03-10%2002.05.49.png

Figure 2: https://raw.githubusercontent.com/chrisausbun/ITFnd100-Mod07/master/Screenshot%202020-03-10%2002.02.24.png

```
# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with "Error Handling" and "Pickling .dat Files"
# ChangeLog (Who,When,What):
# Chris Ausbun,03.06.2020,Created script
# Chris Ausbun,03.06.2020,Added code to complete assignment 7
# Chris Ausbun,03.09.2020,Modified code to complete assignment 7
# ---------------------------------------------------------------------------- #
```
```
import pickle
import sys

# Declare variables and constants

objFile = 'AppData.dat'
lstNumbers = []
```
```
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
```
```
# Processing  --------------------------------------------------------------- #
                    print()
                    intSum = floatFirstNumber + floatSecondNumber
                    intDifference = floatFirstNumber - floatSecondNumber
                    intProduct = floatFirstNumber * floatSecondNumber
                    intQuotient = floatFirstNumber / floatSecondNumber
```
```
# Presentation (Input/Output)  -------------------------------------------- #
                    print("The sum of", floatFirstNumber, "and", floatSecondNumber, "is equal to:", intSum)
                    print("The difference of", floatFirstNumber, "and", floatSecondNumber, "is equal to:", intDifference)
                    print("The product of", floatFirstNumber, "and", floatSecondNumber, "is equal to:", intProduct)
                    print("The quotient of", floatFirstNumber, "and", floatSecondNumber, "is equal to:", intQuotient)

```
