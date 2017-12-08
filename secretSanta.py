# Andrew Ang & Rafael Valdez & Henry Ang
# The purpose of this program is to decide the secret santa
# between a group of people.
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

# Description: Takes in list of people and will randomize order and assign secret santa
# in this function pairs are allowed to happen
# Parameters: List of people's names and dictionary
# Returns: Dictionary of people
def multIsland(nameList, assignDictionary, numOfPeeps):

    # if the total number of people is three, just call the other one
    print("hey")

    #otherwise do the algorithm thing





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
    print()
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


#USER GETS A CHOICE FOR TYPE OF PAIRING
choice = 0
print("Select the type of randomization for the secret santa.")
choice = int(input("Select (1) for anyone can get anyone.\n"
                   "Select (2) for no pairs can be formed.\n"
                   "\tex)Tom -> John and John -> Tom \n "
                   "\t   Is NOT allowed \n"))

while(choice != 1 and choice != 2):
        print("Please try again. Options are 1 or 2.") # MAKE A LOOP THAT KEEPS ASKING
        choice = int(input("Select (1) for anyone can get anyone.\n"
                           "Select (2) for no pairs can be formed.\n"
                           "\tex)Tom -> John and John -> Tom \n "
                           "\t   Is NOT allowed \n"))
if(choice == 1):
        multIsland(listOfNames, dictOfNames, numOfPeeps) # Generate pure random
elif(choice == 2):
        noIsland(listOfNames, dictOfNames)  # Generate the random selection w/ no pairs

# Generates outputfile for all secret santa particpants
# for key,val in dictOfNames.items():
#     outFile = key + ".txt"
#     try:
#         with open(str(outFile), 'w') as outputfile:  # create output file
#             # prints to output file
#             print(key, file=outputfile)
#             print("Your secret santa is " + val, file=outputfile)
#         outputfile.close()
#         print("Results in file " + outFile)
#     except(IndexError):
#         print("Error creating file")
#         quit()


#Test the output
# for x in listOfNames:
#     print("List values: ", end="")
#     print(x)
# for i in dictOfNames:
#     print("Dictionary values: ", end="")
#     print (i, dictOfNames[i])

