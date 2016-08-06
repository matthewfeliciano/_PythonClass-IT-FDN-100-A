import pickle

intId = int(input("Enter an Id: "))
strName = str(input("Enter a Name: "))
lstCustomer = [intId, strName]
print(lstCustomer)

#Now we store the data with the pickle.dump method
objFile = open("Customers.dat", "ab")
pickle.dump(lstCustomer, objFile)
objFile.close()

#And, we read the data back with the same pickle.load method
objFile = open("Customers.dat", "rb")
objFileData = pickle.load(objFile) #Note that load() only load one row of data.
objFile.close()

print(objFileData)
