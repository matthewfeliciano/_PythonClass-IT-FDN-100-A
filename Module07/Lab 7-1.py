'''
LAB 7-1: Working with text files
1)	Create a script that allows you to store product ids, names, and prices.
The code will be very similar to the last example.
'''

#  Data
objFile = None # File Handle
strUserInput = None # A string which holds user input

#  Processing
def WriteProductUserInput(File):
    print("Type in a Product ID, Name, and Price you want to add to the file")
    print("(Enter 'Exit' to quit!)")
    while (True):
        strUserInput = input("Enter the ID, Name, and Price (ex. 1,Desk,100)")
        if (strUserInput.lower() == "exit"): break
        else: File.write(strUserInput + "\n")

def ReadAllFileData(File, Messasge="Contents of Files:"):
    print(Messasge)
    print("----------------------------")
    File.seek(0)
    print(File.read())

# I/O

objFile = open("productFile.txt", "r+")
ReadAllFileData(objFile, "Here is the current data:")

WriteProductUserInput(objFile)

ReadAllFileData(objFile, "Here is the data we saved:")
objFile.close()
