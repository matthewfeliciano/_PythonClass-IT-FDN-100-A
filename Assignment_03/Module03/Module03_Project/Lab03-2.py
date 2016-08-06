import sys
'''
Write a script that lets a user select one of three options
by entering an argument when the script starts.
'''
if(len(sys.argv) >1):
    intChoice = int(sys.argv[1]) # Get the argument value
    # Execute if 1, 2, or 3 is selected
    if(intChoice == 1):print("You chose one") # Print "You chose one" only if option 1 is selected.
    elif(intChoice == 2):print("You chose two") # Print "You chose two" execute only if option 2 is selected.
    elif(intChoice == 3):print("You chose three") # Print "You chose three" execute only if option 3 is selected.
    else: print("Please choose 1, 2, or 3") # Print "Please choose 1, 2, or 3"
else:
    print("You need to pass in a single number of 1, 2, or 3")

