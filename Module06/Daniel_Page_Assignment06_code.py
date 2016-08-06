"""-------------------------------------------------------------
Title: To-Do List Functions Program
Dev: Dan Page
Date: 08/01/2016
Description: This program manages a To-Do list from a text file.
It allows the user to add and remove tasks using Classes and
Static Methods.
--------------------------------------------------------------"""

# PROGRAM START

# Open File and Define Variables (DATA)
todo_file = open("C:\\users\\feliciam\\documents\\_PythonClass\\Module06\\Todo.txt", "a")


# To-Do Class (PROCESSING)
class ToDo(object):
    """This class containts all functions to manage a simple To-Do list"""

    # Load current To-Do List into Python Program
    @staticmethod
    def load_data():
        """This function loads task: priority pairs in a dict and then multiple pairs into a list"""

        read_file = open("C:\\users\\feliciam\\documents\\_PythonClass\\Module06\\Todo.txt", "r")
        file_lst = []
        for line in read_file:
            current_task, current_priority = line.split(",")
            file_dict = {current_task: current_priority}
            file_lst.append(file_dict)
        return file_lst

    # Display To-Do List Function
    @staticmethod
    def display_lst(lst):
        """This function displays the current To-Do list to the user"""

        for item in lst:
            print(item)

    # User Modifications Function
    @staticmethod
    def user_mod(mod_lst, write_file, old_length):
        """This function allows the user to add and remove items, as well as save the updated list"""

        # While Loop for User input
        while True:
            user_choice = input("What would you like to do? ")
            # User adds a new task
            if user_choice == "1":
                task = input("Please enter the task: ")
                priority = input("What is its priority (high/low)? ")
                mod_dict = {task: priority}
                mod_lst.append(mod_dict)
            # User removes a task
            elif user_choice == "2":
                erase_task = input("Which task would you like to erase? ")
                try:
                    mod_lst.remove("Task: " + erase_task)
                except LookupError:
                    print("That Task does not exist in the list!")
            # User saves the updated To-Do List
            elif user_choice == "3":
                for mod_dict in mod_lst:
                    if mod_lst.index(mod_dict) > (old_length - 1):
                        for element in mod_dict:
                            write_file.write("Task: " + element + ", Priority: " + mod_dict.get(element) + "\n")
                break
            else:
                print("You did not choose a valid option. Please try again.")
                continue

# PRESENTATION

# Welcome and Display To-Do List
print("Welcome to your To-Do List!\n")
print("Current To-Do List")
print("***********************************************")
todo_lst = ToDo.load_data()
for dict_item in todo_lst:
    print(dict_item)
print("***********************************************")

# User Selection
print("Select 1 to Add a Task")
print("Select 2 to Remove a Task")
print("Select 3 to Save all tasks in the To-Do File and Exit")
lst_length = len(todo_lst)
ToDo.user_mod(todo_lst, todo_file, lst_length)


# Ending Message
print("Have a Great Day!")
todo_file.close()

# PROGRAM END

