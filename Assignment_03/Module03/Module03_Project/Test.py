objFile = open("C:\\Users\\feliciam\\Documents\\_PythonClass\\TestData.txt", "a")
print("Type in a string to write (Enter 'Exit' to quit!)")
while(True):
  strUserInput = input("Enter your data: ")
  if(strUserInput.lower() == "exit"): break
  else: objFile.write(strUserInput + "\n")
objFile.close()
