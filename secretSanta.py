# Andrew Ang & Rafael Valdez & Henry Ang

def getInput():
    print("Welcome to the Secret Santa App!")
    print("Please follow the steps to determine your secret santa!")

    totalNumOfPeeps = int(input("How many participants are there? "));

    print(totalNumOfPeeps)
    print("What are the names of the participants?")
    listOfNames = [] # list of names
    dictOfNames = {} # dictionary
    print("First and Last Name: ")
    for x in range(1, totalNumOfPeeps + 1):

        print(str(x) + ". ", end="")
        name = input()
        listOfNames.append(name)
        dictOfNames[name] = 0
    for x in listOfNames:
        print(x)
    for i in dictOfNames:
        print (i, dictOfNames[i])