'''---------------------------------------------------------------------------------
Dev:MFeliciano
LAB 5-1: Working with Lists
1)	Create an application that uses a list to hold the following data:

Id	Name	Email
1	Bob Smith	BSmith@Hotmail.com
2	Sue Jones	SueJ@Yahoo.com
3	Joe James	JoeJames@Gmail.com

2)	Add code that lets users appends a new row of data.
3)	Add a loop that lets the user keep adding rows.
4)	Ask the user if they want to save the data to a file when they exit the loop.
5)	Save the data to a file if they say 'yes'
-------------------------------------------------------------------------------- '''
# 1) Create a list to hold data:
lstRow0 = ["ID","Name","Email"]
lstRow1 = [1,"Bob Smith","BSmith@Hotmail.com"]
lstRow2 = [2,"Sue Jones","SueJ@Yahoo.com"]
lstRow3 = [3,"Joe James","JoeJames@Gmail.com"]
lstTable = [lstRow0,lstRow1,lstRow2,lstRow3]
print(lstTable)
# 2) Add code that lets users appends a new row of data.
# 3) Add a loop that lets the user keep adding rows.
while(True):
    intID = int(input("Enter an ID: "))
    strName = input("Enter a Name: ")
    strEmail = input("Enter an Email: ")
    lstNewRow = [intID, strName, strEmail]
    lstTable.append(lstNewRow)
    if(input("Type 'exit' to end.").lower()=="exit"):break
# 4) Ask the user if they want to save the data to a file when they exit the loop.
strSave = input("\nWould you like to save data to a file? (y/n): ")
# 5)	Save the data to a file if they say 'yes'
if(strSave.lower() == "y"):
    objF = open("Lab5_1Table.txt", "a")
    objF.write(str(lstTable))
    objF.close()
    print("The following data was saved to a file:\n\r",lstTable)
else:
    print("Data not saved!")