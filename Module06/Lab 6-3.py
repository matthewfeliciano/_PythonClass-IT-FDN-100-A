'''
________________________________________
LAB 6-3: Working with classes
1)	Create a class with (4) Methods, have them return
a Sum, Difference, Product, and Quotient of two numbers.
2)	Name the class MathProcessor
3)	Name the methods AddValues, SubtractValues, MultiplyValues, DivideValues.
4)	Display the results to the user by calling each method.
'''
#  -- data code -- ***This section is not needed in Python***
v1 = 15  # first argument
v2 = 5  # second argument
decAns = [] # result of processing

#  --processing code--
class MathProcessor(object):
# Define the function
    # Define the method
    @staticmethod
    def AddValues(value1, value2):
        return value1 + value2

    @staticmethod
    def SubtractValues(value1, value2):
        return value1 - value2

    @staticmethod
    def MultiplyValues(value1, value2):
        return value1 * value2

    @staticmethod
    def DivideValues(value1, value2):
        return value1 / value2

# --presentation (I/O) code--
# Call the function
v1 = 15
v2 = 5
decAns = MathProcessor.AddValues(v1, v2)
print("The Sum of the values " + str(v1) + " and " + str(v2) + " is: " + str(decAns))
decAns = MathProcessor.SubtractValues(v1, v2)
print("The Difference of the values " + str(v1) + " and " + str(v2) + " is: " + str(decAns))
decAns = MathProcessor.MultiplyValues(v1, v2)
print("The Product of the values " + str(v1) + " and " + str(v2) + " is: " + str(decAns))
decAns = MathProcessor.DivideValues(v1, v2)
print("The Quotient of the values " + str(v1) + " and " + str(v2) + " is: " + str(decAns))
