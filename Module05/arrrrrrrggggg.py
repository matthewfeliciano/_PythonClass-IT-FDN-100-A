#-------------------------------------------------#
# Title: To Do List
# Dev:   mfeliciano
# Date:  07/24/2016
# Desc: This script will open the ToDo.txt file into a python dictionary
#       and allow the user to add or remove items as needed. When finished
#       the user can exit and save the file.
# ChangeLog: mfeliciano, 07/31/16, adding functions and class.
#
#1)	Make a function for the code that loads each row of data you have from the
# ToDo.txt text file into a Python Dictionary and then adds the rows of data to a Python List.

#2)	Make a function for the code that displays the contents of the Python List object to the user.

#3)	Make a function for the code that allows the user to Add or Remove tasks from the list,
#  plus save the tasks in the List tasks-priorities using numbered choices.

#4)	Make a function for the code that saves the data
#  from the table into the Todo.txt file when the program exits.

#5)	Make a Class to hold the functions.
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
gStrFileName = "C:\\Users\\feliciam\\Documents\\_PythonClass\\Module06\\ToDo.txt" # Path of file location  for todo file
gTodoItems= {} # Dictionary of To Do items

#-- Processing --#
def LoadExistingList(FileName):# Task 1
    """When the program starts, load the any data you have
    in a text file called ToDo.txt into a python Dictionary"""
    lstData = [] # A row of data separated into elements of a list
    dicTable = {} # A dictionary that acts as a 'table' of rows

    objFile = open(FileName, "r")
    for line in objFile:
        strData = line # reading data
        lstData = strData.split(",") # divide the data into 2 elements
        dicTable[lstData[0].strip()] = lstData[1].strip()  # loading into Dictionary
    objFile.close()
    return dicTable

def DisplayCurrentTodoList(ToDoItems): # Task 2
    """ Make a function for the code that displays
    the contents of the Python List object to the user. """
    print("Need to get DONE!: ")  # I wanted a header in my initial display
    print("------------------")  # Decided to break it up with some dashes
    for strKey, strValue in dicTable.items():
        print(strKey + " (" + strValue + ") ")

def ShowMenuOptions(): # Task 3
    """Make a function for the code that allows the user to
    Add or Remove tasks from the list, plus save the tasks in the
    List tasks-priorities using numbered choices"""
    print("""
        Please Select an option
        1) Add task
        2) Remove task
        3) Save all tasks to the Todo.txt file and exit!
        """)
def AddTask(ToDoItems, NewTask, Priority): # Task 4
    """ Add a new item to the todo list """
    ToDoItems[NewTask] = Priority

def RemoveTask(ToDoItems,Task): # Task 5
    """ Remove a new item to the todo list """
    if(Task in ToDoItems):
        del ToDoItems[Task]

def SaveToFile(ToDoItems, FileName): # Task 6
    """Saves todo list data to a file"""
    objFile = open(FileName, "w")
    for strKey, strValue in ToDoItems.items():
        objFile.write(strKey + "," + strValue + "\n")
    objFile.close()

#-- Input/Output --#

def Main():
    """ Coordinates I/O and actions for this script """
    global gStrFileName
    global gTodoItems
    try:
        # When the program starts, load the any data you have
        # in a text file called ToDo.txt into a python Dictionary.
        gTodoItems = LoadExistingList(gStrFileName)

        # Display all todo items to user
        DisplayCurrentTodoList(gTodoItems)

        # Display a menu of choices to the user
        # and Process user I/0
        while(True):
            ShowUserMenuOptions()
            strChoice = str(input("Which option would you like to perform? [1 to 3]"))
            if (strChoice == '1'):    # 1) Add a new item.
                strTask = str(input("What is the task?"))
                strPriority = str(input("What is the priority? [high|low]"))
                AddTask(gTodoItems, strTask, strPriority)
                DisplayCurrentTodoList(gTodoItems)
                continue
            elif(strChoice == '2'):    # 2) Remove an existing item.
                for strKey, strValue in gTodoItems.items():
                    print(strKey)
                strKeyToRemove = input("Which item would you like removed?")
                RemoveTask(gTodoItems, strKeyToRemove)
                DisplayCurrentTodoList(gTodoItems)
            elif(strChoice == '3'):    # 3) Save and Exit.
                SaveTodoListToFile(gTodoItems, gStrFileName)
                print("Your To Do list has been updated.")
                break
            else:
                print("Please select either 1, 2, or 3")
                DisplayCurrentTodoList(gTodoItems)
                continue
    except Exception as e:
        print("There was a unexpected error!")
        print("pythons error info: ")
        print(e)


#----- Start of actions within this script ---------#
Main() # Call the Main function at the start of the script
