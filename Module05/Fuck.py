objFileName = "C:\\Users\\feliciam\\Documents\\_PythonClass\\Module05\\ToDo.txt"
list = []
dicTable = {}

# 1)
def loadData():
    objFile = open(objFileName, "r")
    for line in objFile:
        (key, val) = line.split(",") # splitting data into 2 elements
        dicTable = {"Task": key.strip(","), "Priority": val.strip("\n")} # loading into Dictionary
        objFile.close()
        list.append(dicTable)
        return list
    print(list)



# 2)
stuff = loadData()
print("Need to get DONE!: ")  # I wanted a header in my initial display
print("------------------")  # Decided to break it up with some dashes
print(stuff)
'''
for list.strKey, list.strValue in dicTable.items():
    print(list.strKey + " (" + list.strKey +") ")
'''