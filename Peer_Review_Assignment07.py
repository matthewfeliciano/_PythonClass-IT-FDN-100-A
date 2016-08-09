"""-------------------------------------------------------------Title: Python Exceptions Calculator ProgramDev: Dan PageDate: 08/07/2016Description: This Program is a simple calculator that can add,subtract, multiply, or divide two numbers.--------------------------------------------------------------"""# Program Start
# Welcome Screen
print("Welcome to the Calculator Program\n")


# User Choices
print("Select 1 to add two numbers")
print("Select 2 to subtract two numbers")
print("Select 3 to multiply two numbers")
print("Select 4 to divide two numbers")
print("Select 5 to Exit\n")

# User Options Code
while True:
    user_choice = input("Which option would you like to do? \n")

    if user_choice == "1":
        num1 = float(input("Enter the 1st Number: "))
        num2 = float(input("Enter the 2nd Number: "))
        sum_nums = num1 + num2
        print("The Sum is: " + str(sum_nums))

    elif user_choice == "2":
        num1 = float(input("Enter the 1st Number: "))
        num2 = float(input("Enter the 2nd Number: "))
        diff_nums = num2 + num1
        print("The Difference is: " + str(diff_nums))

    elif user_choice == "3":
        num1 = float(input("Enter the 1st Number: "))
        num2 = float(input("Enter the 2nd Number: "))
        prod_nums = num2 * num1
        print("The Product is: " + str(prod_nums))

    elif user_choice == "4":
        num1 = float(input("Enter the 1st Number: "))
        num2 = float(input("Enter the 2nd Number: "))
        try:
            quot_nums = num2 / num1
            print("The Quotient is: " + str(quot_nums))
        except ZeroDivisionError as z:
            print("*****************************")
            print("The following error occurred:")
            print(str(z))
            print("*****************************")

    elif user_choice == "5":
        print("Now Exiting...")
        break
    else:
        print("You entered an invalid option. Please try again.")
        continue
# Program End