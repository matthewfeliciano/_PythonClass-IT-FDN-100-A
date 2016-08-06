'''
1)	Create a script that lets a user add two numbers together and saves
the answer to a file. Let the user continue adding
numbers together until they type in the word "exit"
'''

#Open the file
objFH = open("C:\\Users\\feliciam\\Documents\\_PythonClass\\Lab03-3Data.txt", "a") #Open the file
print("Enter 'Exit' to quit!") #Loop until user types 'exit'
while(True):
    #Get first number
    fltN1 = float(input("Enter the first number: "))
    #Get second number
    fltN2 = float(input("Enter the second number: "))
    #Add numbers together
    fltSum = fltN1 + fltN2
    #Write answer to file
    objFH.write(str(fltSum) + "\n")
    #Ask user if they want to continue
    if(input("Type 'Enter' to continue or 'exit' to quit this program. " )):break

objFH.close() #Close the file