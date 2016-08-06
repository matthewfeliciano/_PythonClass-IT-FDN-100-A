def loadData(key, val):
    list = []
    dicTable = {}
    key = str
    val = str
    # Open file
    objFile = open("C:/Users/feliciam/Documents/_PythonClass/Module06/ToDo.txt", "r")

    # Iterate through file and add contents to a dictionary
    for line in objFile:
        (key, val) = line.split(",")
        dicTable = {"Task": key.strip(","), "Priority": val.strip("\n")}

        # Add the dictionary elements to a list
        list.append(dicTable)
        return list

#print(loadData(list))
print("The contents of the folder are:\n", loadData(key, val))



'''
list = []
dictionary = {}

# Open file
objFile = open('C:/Users/feliciam/Documents/_PythonClass/Module06/ToDo.txt', 'r')

# Iterate through file and add contents to a dictionary
for line in objFile:
    (key, val) = line.split(",")
    dictionary = {"Task": key.strip(","), "Priority": val.strip("\n")}

    # Add the dictionary elements to a list
    list.append(dictionary)
objFile.close()
print("The contents of the folder are:\n", list)
'''