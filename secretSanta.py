# Andrew Ang & Rafael Valdez & Henry Ang
import random

# MAIN STARTS HERE
print("Welcome to the Secret Santa App!")
print("Please follow the steps to determine your secret santa!")
totalNumOfPeeps = int(input("How many participants are there? "));
print("What are the names of the participants?")
print("First and Last Name: ")
listOfNames = [] # list of names
dictOfNames = {} # dictionary


# Description: Takes in list of people and will randomize order and assign secret santa
# Parameters: List of people's names and dictionary
# Returns: Dictionary of people
def noIsland(nameList, assignDictionary):
    # Randomizing List
    random.shuffle(nameList)
    for x in range(0, len(nameList)):
        if x == len(nameList) - 1:
            assignDictionary[nameList[x]] = nameList[0]
            print(nameList[x] + " : " + nameList[0])
        else:
            assignDictionary[nameList[x]] = nameList[x+1]
            print(nameList[x] + " : " + nameList[x+1])

    # print(assignDictionary)

# EXAMPLE VALUES
myList = ["Naveen", "Courtney", "Robert", "Hector", "Andrew", "Henry", "Rafael"]
myDict = {
    "Naveen": "",
    "Courtney": "",
    "Robert": "",
    "Hector": "",
    "Andrew": "",
    "Henry": "",
    "Rafael": ""
}

noIsland(myList, myDict)

# END OF EXAMPLE VALUES

for x in range(1, totalNumOfPeeps + 1): #create the list and dictionary
    print(str(x) + ". ", end="")
    name = input()
    listOfNames.append(name)
    dictOfNames[name] = ""
# for x in listOfNames:
#     print(x)
# for i in dictOfNames:
#     print (i, dictOfNames[i])

