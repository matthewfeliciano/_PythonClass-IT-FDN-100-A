'''----------------------------------------------------------------
Dev:MFeliciano
Assignment03 :
1.	Create a new program that asks the user for the name of
a household item, and then asks for its estimated value.
Store, both pieces of data in a text file called, HomeInventory.txt
----------------------------------------------------------------'''

# Begin by opening and appending a file
objHI = open("C:\\Users\\feliciam\\Documents\\_PythonClass\\HomeInventory.txt", "a")
# Here we are giving the users some information on how to use the program.
print("Enter household items below.")
# Next create a loop that allows user to keep entering items and values until they are finished.
while (True):
    # First prompt the user for the name of household item.
    strI1 = input("Enter item: ")
    # Next prompt user for the value of item.
    strV1 = input("Enter estimated value: ")
    # Now we write answer to file and create a new line for more input.
    objHI.write("Item: " + strI1 + " " + "Value: $" + strV1 + "\n")
    # Finally give user an opportunity to continue entering items or exit the program.
    if input("Hit 'Enter' to continue or type 'exit' to quit this program. "): break
