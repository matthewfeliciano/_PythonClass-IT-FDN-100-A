#-------------------------------------------------#
# Title: To Do List
# Dev:   mfeliciano
# Date:  08/07/2016
# Desc: 2)	Create a simple example of how you
# would use Python Pickling. Make sure to comment your code.
# ChangeLog:
#-------------------------------------------------#

# 2) Create a simple example
# of how you would use Python Pickling.

#  This example shows how to use Pickling

import pickle


strItem = str(input("Enter an Item: "))
intPrice = int(input("Enter a Price: "))
lstForSale = [strItem, intPrice]
print(lstForSale)

#Now we store the data with the pickle.dump method
objFile = open("SaleItems.dat", "ab")
pickle.dump(lstForSale, objFile)
objFile.close()

#And, we read the data back with the same pickle.load method
objFile = open("SaleItems.dat", "rb")
objFileData = pickle.load(objFile) #Note that load() only load one row of data.
objFile.close()

print(objFileData)