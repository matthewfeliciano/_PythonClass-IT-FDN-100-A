"""-------------------------------------------------------------Title: Python Pickling ProgramDev: Dan PageDate: 08/07/2016Description: This Program takes in the user's favorite animal andthe sounds they make and stores it in a list.  It then saves toa .dat file and reads the loads the list back from the .dat file--------------------------------------------------------------"""# Program Start
import pickle

# Store Animal and their sound in a list
animal = str(input("Enter a your favorite animal: "))
animal_sound = str(input("What sound does your favorite animal make? "))
animal_lst = [animal, animal_sound]

print("From the User: ", animal_lst)

# Store Data with Pickle Method
objFile = open("AnimalSounds.dat", "wb")
pickle.dump(animal_lst, objFile)
objFile.close()

# Read Data with PickleMethod
objFile = open("AnimalSounds.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()

print("From the File: ", objFileData)

# Program End