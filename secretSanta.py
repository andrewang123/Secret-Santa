# Andrew Ang & Rafael Valdez & Henry Ang

# MAIN STARTS HERE
print("Welcome to the Secret Santa App!")
print("Please follow the steps to determine your secret santa!")
totalNumOfPeeps = int(input("How many participants are there? "));
print("What are the names of the participants?")
print("First and Last Name: ")
listOfNames = [] # list of names
dictOfNames = {} # dictionary
for x in range(1, totalNumOfPeeps + 1): #create the list and dictionary
    print(str(x) + ". ", end="")
    name = input()
    listOfNames.append(name)
    dictOfNames[name] = ""
# for x in listOfNames:
#     print(x)
# for i in dictOfNames:
#     print (i, dictOfNames[i])