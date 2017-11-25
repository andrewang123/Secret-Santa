# Andrew Ang & Rafael Valdez & Henry Ang
import random


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
    # [Naveen , Courtney, Robert]

    # Naveen : Courtney