#-------------------------------------------------#
# Title: To Do List
# Dev:   mfeliciano
# Date:  07/24/2016
# Desc: This script will open the ToDo.dat file into a python dictionary
#       and allow the user to add or remove items as needed. When finished
#       the user can exit and save the file.
# ChangeLog: (Who, When, What)
# None at this time
#-------------------------------------------------#

#-- Data
# First assign values to the variables
# objFile = "Variable for the file."
# strData = "Row of data from the text file"
# lstData = A row of data in a list
# strMenu = A menu of user options
# strOption = Option user selected

#--- User Input/Output to file
# Use a menu to get user input
# send output to a file

#--- Processing
# 1) When the program starts, load the each rows of data you have
#    in ToDo.dat text file into a python Dictionary.

# 2) Display all todo items

# 3) Display menu to user

# 4) Add item to list

# 5) Remove item from list

# 6) Save tasks to ToDo.dat file

#---------------------------------------

objFileName = "ToDo.dat"
strData = ""
dicTable = {}

# 1)
objFile = open(objFileName, "rb")
for line in objFile:
 strData = line # reading data
 lstData = strData.split(",") # splitting data into 2 elements
 dicTable[lstData[0].strip()] = lstData[1].strip() # loading into Dictionary
objFile.close()

# 2)
print("Need to get DONE!: ")  # I wanted a header in my initial display
print("------------------")  # Decided to break it up with some dashes
for strKey, strValue in dicTable.items():
    print(strKey + " (" + strValue +") ")

# 3)
while(True):
    print("""
        Please Select an option
        1) Add task
        2) Remove task
        3) Save all tasks to the Todo.txt file and exit!
        """)
    strOption = str(input("Which option would you like to perform? [1 to 3]"))

# 4)
    if (strOption == '1'):  # Add task option selected
            strTask = str(input("What is the task?"))
            strPriority = str(input("What is the priority? 'high or low'"))
            dicTable[strTask] = strPriority
            continue
# 5)
    elif (strOption == '2'):  # Remove a task option selected
        for strKey, strValue in dicTable.items():
            print(strKey)
        strKeyToRemove = input("Which task can be removed?")
        if (strKeyToRemove in dicTable):
            del dicTable[strKeyToRemove]
        else:
            print("Task not found.")
        continue

# 6)
    elif (strOption == '3'):  # Exit and save option selected
        objFile = open(objFileName, "w")
        for strKey, strValue in dicTable.items():
            objFile.write(strKey + "," + strValue + "\n")
        objFile.close()
        print("Your To Do list has been updated.")  # Message to let user know data has been saved
        break