'''
LAB 6-2: Working with returned lists
1)	Create a function that returns a list of the Sum, Difference, Product, and Quotient of two numbers.
2)	Display the results to the user.
3)	Divide you program into data, processing, and presentation sections.
'''
#  -- data code -- ***This section is not needed in Python***
v1 = 10  # first argument
v2 = 5  # second argument
lstAns = [] # result of processing

#  --processing code--
# Define the function
def DoMath(value1, value2):
    decSum = value1 + value2
    decDiff = value1 - value2
    decProd = value1 * value2
    decQuo = value1 / value2
    return [decSum, decDiff, decProd, decQuo, value1, value2]

# --presentation (I/O) code--
# Call the function
v1 = 10
v2 = 5
lstAns = DoMath(v1, v2)
print("For the values " + str(lstAns[4]), "and", str(lstAns[5]))
print("The Sum of the values is: " + str(lstAns[0]))
print("The Difference of the values is: " + str(lstAns[1]))
print("The Product of the values is: " + str(lstAns[2]))
print("The Quotient of the values is: " + str(lstAns[3]))