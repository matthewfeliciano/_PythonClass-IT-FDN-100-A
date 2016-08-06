'''
LAB 7-2: Working with errors
Desc: Create a script that allows you to store product ids, names, and prices.
The code will be very similar to the last example.
Changelog:
    mfeliciano, 08/06/16, Add error handling code.
'''

#  Data
objFile = None # File Handle
strUserInput = None # A string which holds user input

#  Processing
def WriteProductUserInput(File):
    try:
        print("Type in a Product ID, Name, and Price you want to add to the file")
        print("(Enter 'Exit' to quit!)")
        while (True):
            strUserInput = input("Enter the ID, Name, and Price (ex. 1,Desk,100)")
            if (strUserInput.lower() == "exit"): break
            else: File.write(strUserInput + "\n")
    except Exception as e:
        print("Error: ", e.__str__())

def ReadAllFileData(File, Messasge="Contents of Files:"):
    try:
        print(Messasge)
        print("----------------------------")
        File.seek(0)
        print(File.read())
    except  Exception as e:
        print("Error: ", e.__str__)

# I/O
try:

    objFile = open("productFile.txt", "r+")
    ReadAllFileData(objFile, "Here is the current data:")

    WriteProductUserInput(objFile)

    ReadAllFileData(objFile, "Here is the data we saved:")
except Exception as e:
    print("Error: ", e.__str__())
finally:
    if(objFile != None):objFile.close()
