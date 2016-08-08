#-------------------------------------------------#
# Title: To Do List
# Dev:   mfeliciano
# Date:  08/07/2016
# Desc: 1)	Create a simple example of how you
# would use Python Exception Handling.
# ChangeLog:
#-------------------------------------------------#

#  1)	Create a simple example of how you
# would use Python Exception Handling.

#  This example shows how to handle the divide by zero exception

#-- Data --#
fltN1 = 0.0
fltN2 = 0.0

#-- Processing --#
def DivideValues():
    try:
        return (fltN1 / fltN2)  # Divide two numbers.
    except Exception as e:  # If the user divides by zero the Exception is thrown
        print("Error: ", e.__str__())

#-- I/O --#
#  Here we are asking the user to enter two numbers to divide.
#  Should the user try to divide a number by zero the code will throw an error.
fltN1 = float(input("Enter the first number: "))
fltN2 = float(input("Enter the second number: "))
print(DivideValues())