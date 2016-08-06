'''---------------------------------------------------------------------------
Dev:MFeliciano
 1) Create a new program that asks the user to input 2 numbers then prints out
 the sum, difference, product, and quotient.
---------------------------------------------------------------------------'''

#User input first value
strN1 = float(input('Enter the first number: '))

#User input second value
strN2 = float(input('Enter the second number: '))

'''
070616 MF - Changed to handle the math in the print statements.

#Convert to float and sum
#fltSum = float(strN1) + float(strN2)

#Convert to float and subtract
#fltDif = float(strN1) - float(strN2)

#Convert to float and multiply
#fltPrd = float(strN1) * float(strN2)

#Convert to float and divide
#fltQuo = float(strN1) / float(strN2)
'''

#Print results
print('The sum of', strN1, 'and', strN2, 'is:', float(strN1) + float(strN2));
print('The difference between', strN1, 'and', strN2, 'is:', float(strN1) - float(strN2))
print('The product of', strN1, 'and', strN2, 'is:', float(strN1) * float(strN2))
print('The quotient of', strN1, 'and', strN2, 'is:', float(strN1) / float(strN2))

input("\n\nPress the Enter key to exit")

