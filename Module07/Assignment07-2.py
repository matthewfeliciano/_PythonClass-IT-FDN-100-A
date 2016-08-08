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
import os

sale_items_filename = 'high_scores.dat'

lstForSale = []

# First time you run this, "SaleItems.dat" won't exist
#   so we need to check for its existence before we load
#   our "database"
if os.path.exists(sale_items_filename):
    # "with" statements are very handy for opening files.
    with open(sale_items_filename, 'rb') as rfp:
        lstForSale = pickle.load(rfp)
    # Notice that there's no "rfp.close()"
    #   ... the "with" clause calls close() automatically!

#  Here we are asking the user to enter a item and a price
strItem = str(input("Enter an Item: "))
intPrice = int(input("Enter a Price: "))

things_to_sell = (strItem, intPrice)

lstForSale.append(things_to_sell)

#  Now we store the data with the pickle.dump method
with open(sale_items_filename, "wb")as wfp:  # Note the 'wb' = write to binary.
    pickle.dump(lstForSale, wfp)


#  Finally we read the data back with the same pickle.load method
with open(sale_items_filename, 'rb') as rfp:
    objFileData = pickle.load(rfp)

print(objFileData)