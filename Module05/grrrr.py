#-------------------------------------------------#
# Title: Working with Functions
# Dev:   RRoot
# Date:  July 18, 2012
# ChangeLog: (Who, When, What)
#   none yet
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
gStrFileName = "C:\\Users\\feliciam\\Documents\\_PythonClass\\Module05\\ToDo.txt" # The name and path of the todo file
gTodoItems= {} # A dictionary of todo items

#-- Processing --#
def LoadExistingList(FileName):# Task 1
    """When the program starts, load the any data you have
    in a text file called ToDo.txt into a python Dictionary"""
    lstData = [] # A row of data separated into elements of a list
    dicTable = {} # A dictionary that acts as a 'table' of rows

    objFile = open(FileName, "r")
    for line in objFile:
        strData = line # readline() reads a line of the data
        lstData = strData.split(",") # divide the data into 2 elements
        dicTable[lstData[0].strip()] = lstData[1].strip()
    objFile.close()
    return dicTable

def DisplayCurrentTodoList(ToDoItems): # Task 2
    """ Display all todo items to user """
    print("******* Current Todo items ********")
    for strKey, strValue in ToDoItems.items():
        print(strKey + " (" + strValue + ")")
    print("***********************************")

def ShowUserMenuOptions(): # Task 3
    """returns: <string> as a menu choice
    Display a menu of choices to the user"""
    print ("""
    Menu of Options
    1) Add a new item.
    2) Remove an existing item.
    3) Save and Exit.
    """)

def AddToDoItem(ToDoItems, NewTask, Priority): # Task 4
    """ Add a new item to the todo list """
    ToDoItems[NewTask] = Priority

def RemoveTodoItem(ToDoItems,Task): # Task 5
    """ Remove a new item to the todo list """
    if(Task in ToDoItems):
        del ToDoItems[Task]

def SaveTodoListToFile(ToDoItems, FileName): # Task 6
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
                AddToDoItem(gTodoItems, strTask, strPriority)
                DisplayCurrentTodoList(gTodoItems)
                continue
            elif(strChoice == '2'):    # 2) Remove an existing item.
                for strKey, strValue in gTodoItems.items():
                    print(strKey)
                strKeyToRemove = input("Which item would you like removed?")
                RemoveTodoItem(gTodoItems, strKeyToRemove)
                DisplayCurrentTodoList(gTodoItems)
            elif(strChoice == '3'):    # 3) Save and Exit.
                SaveTodoListToFile(gTodoItems, gStrFileName)
                print("File Saved and script ended!")
                break
            else:
                print("I'm sorry, but your choice must be 1, 2, or 3")
                DisplayCurrentTodoList(gTodoItems)
                continue
    except Exception as e:
        print("There was a unexpected error!")
        print("pythons error info: ")
        print(e)


#----- Start of actions within this script ---------#
Main() # Call the Main function at the start of the script

