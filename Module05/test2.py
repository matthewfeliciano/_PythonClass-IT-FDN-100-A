#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   none yet
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# lstData = A row of data separated into elements of a list
# dicTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# get user input with a Menu
# send program output to user and a file

#-- Processing --#
# Task 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Task 2
# Display all todo items to user

# Task 3
# Display a menu of choices to the user

# Task 4
# Add a new item to the todo list

# Task 5
# Remove a new item to the todo list

# Task 6
# Save tasks to the ToDo.txt file

#-------------------------------

objFileName = "C:\\Users\\feliciam\\Documents\\_PythonClass\\Module05\\ToDo.txt"
strData = ""
dicTable = {}

# Task 1
objFile = open(objFileName, "r")
for line in objFile:
 strData = line # readline() reads a line of the data
 lstData = strData.split(",") # divide the data into 2 elements
 dicTable[lstData[0].strip()] = lstData[1].strip()
objFile.close()

# Task 2
for strKey, strValue in dicTable.items():
    print(strKey + " (" + strValue + ")")


# Task 3
while(True):
    print ("""
    Menu of Options
    1) Add a new item.
    2) Remove an existing item.
    3) Save and Exit.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 3]"))

    # Task 4
    if (strChoice == '1'):
            strTask = str(input("What is the task?"))
            strPriority = str(input("What is the priority? 'High or Low'"))
            dicTable[strTask] = strPriority
            continue

    # Task 5
    elif(strChoice == '2'):
        for strKey, strValue in dicTable.items():
            print(strKey)
        strKeyToRemove = input("Which task would you like removed?")
        if(strKeyToRemove in dicTable):
            del dicTable[strKeyToRemove]
        else:
            print("Task not found.")
        continue

    # Task 6
    elif(strChoice == '3'):
        objFile = open(objFileName, "w")
        for strKey, strValue in dicTable.items():
            objFile.write(strKey + "," + strValue + "\n")
        objFile.close()
        break

