'''
LAB 6-1: Working with functions
1)	Create a function that prints the Sum, Difference, Product, and Quotient of two numbers.
'''


# Define the function
def DoMath(value1, value2):
    decSum = value1 + value2
    decDiff = value1 - value2
    decProd = value1 * value2
    decQuo = value1 / value2
    print("For the values", value1, "and", value2)
    print("The Sum of the values is: " + str(decSum))
    print("The Difference of the values is: " + str(decDiff))
    print("The Product of the values is: " + str(decProd))
    print("The Quotient of the values is: " + str(decQuo))


# Call the function
DoMath(6, 6)