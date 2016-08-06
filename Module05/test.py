'''
objFile = open("ToDo.txt", "r")
strData = objFile.readline()
tplRow = ((strData.split(",")[0]).strip(), (strData.split(",")[1]).strip())  # Split the row on the commas
tplTable = tplRow,
# Next we get the rest of the data rows from the file.
for line in objFile:
    strData = line
    tplRow = ((strData.split(",")[0]).strip(), (strData.split(",")[1]).strip())  # Split the row on the commas
    tplTable += tplRow,
print(tplTable)
'''

objFile = open("ToDo2.txt", "r")
print(objFile.read()

newFile = open("ToDo.txt", "w")
lstRow0 = ["Clean House", "Low"]
lstRow1 = ["Pay Bills", "High"]
lstTable = [lstRow0,lstRow1]
newFile.close
