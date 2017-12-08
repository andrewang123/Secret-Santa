# Andrew Ang & Rafael Valdez & Henry Ang
# The purpose of this program is to decide the secret santa
# between a group of people.
#dksdflksjdlfk
import random

listOfNames = []  # list of names
dictOfNames = {}  # dictionary

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

# Description: Gets the total number of participants
# Parameters: N/A
# Returns: Number of people participating
def numberOfParticipants():
    countOfPeeps = 1
    print(str(countOfPeeps) + ". ", end="")
    name = str(input())
    if (name == "stop" or name == "Stop"):
        countOfPeeps = 0;
    while (name != "stop" and name != "Stop"):
        #add values to the list and dictionary
        listOfNames.append(name)
        dictOfNames[name] = ""
        if (name != "stop" and name != "Stop"):
            countOfPeeps += 1
        print(str(countOfPeeps) + ". ", end="")
        name = input()
        if (name == "stop" or name == "Stop"):
            countOfPeeps -= 1 #account for case when user enters stop at beginning
    print(str(countOfPeeps) + " people are participating in secret santa.")
    return countOfPeeps

# MAIN STARTS HERE
print("Welcome to the Secret Santa App!")
print("Please follow the steps below to determine your secret santa!")
print("What are the names of the participants?")
print("Names: (type \"stop\" to stop)")
numOfPeeps = numberOfParticipants()
#Force the user to enter values > than 2
while(numOfPeeps < 3):
    #Empty the lists
    listOfNames = []
    dictOfNames = {}
    if(numOfPeeps == 0):
        print("You need to have at least 3 members for secret santa.")
    elif(numOfPeeps == 1):
        print("It wouldn't be much of a suprise if you were your own secret santa.")
        print("You need at least 3 members for secret santa, please try again.")
    else: #other option is 2, not possible for neg values
        print("It wouldn't be much of suprise with two people exchanging gifts.")
        print("You need at least 3 members for secret santa, please try again.")
    print("(All previous entries will be erased)")
    numOfPeeps = numberOfParticipants()

noIsland(listOfNames, dictOfNames) # Generate the random selection

'''
PUT YOUR CODE HERE HENRY!!!
'''

#Test the output
# for x in listOfNames:
#     print("List values: ", end="")
#     print(x)
# for i in dictOfNames:
#     print("Dictionary values: ", end="")
#     print (i, dictOfNames[i])

