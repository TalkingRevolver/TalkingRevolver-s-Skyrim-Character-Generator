### TalkingRevolver's Skyrim Character Generator ###
### ver 0.2.0 ###
import logging
import random
import listModule
import funcModule

## Logging ##
logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s - %(message)s')

## Class - Character ##
class Character:
    # Constructor
    # Sets attributes to None, skills to []
    def __init__(self):
        self.race = None # Race
        self.gender = None # Gender
        self.clss = None # Class
        self.cDesc = None # Class description
        self.skills = [] # Skills list

    # setRace
    # Picks a string from a list via a random number, sets to self.race
    def setRace(self):
        # List of races
        rList = listModule.raceList

        num = random.randint(0, len(rList) - 1)

        self.race = rList[num]

       

    # setGender
    # Randomly picks a string from a liost of three, sets to self.gender
    def setGender(self):
        # List of genders
        gList = ['Male', 'Female', 'Other']

        num = random.randint(0, len(gList) - 1)

        self.gender = gList[num]



    # setSkills
    # Randomly chooses a number of strings (default 4), appends to
    #   self.skills
    def setSkills(self):
        # List of skills
        sList = listModule.skillListV

        # Get number of skills
        print('\tGenerate how many skills?')
        sNum = int(input())

        # Redundancy flag
        redun = False
        
        for i in range(sNum):
            num = random.randint(0, len(sList) - 1)
            skill = sList[num]

            # Check if skill is already in self.skills
            while skill in self.skills:
                num = random.randint(0, len(sList) - 1)
                skill = sList[num]

            # Check if skill is redundant
            redun = funcModule.redunCheck(skill, self.skills)
            while redun == True:
                num = random.randint(0, len(sList) - 1)
                skill = sList[num]
                redun = funcModule.redunCheck(skill, self.skills)
                
        
            self.skills.append(skill)

    # setClass
    # Generates a pre-defined class from classList
    # Sets self.class to 'c', self.skills to 'l' self.cDesc to 'desc'
    def setClass(self):
        c = ''
        l = []

        # Get class name
        cNum = random.randint(0, len(listModule.classList) - 1)
        c = listModule.classList[cNum]
        self.clss = c

        # Append class skills to self.skills
        l = listModule.skillListC.get(c)
        for i in l:
            self.skills.append(i)

        # Set class description
        self.cDesc = listModule.cDesc.get(c)

## MAIN ##
def main():
    # Create Character object
    char = Character()

    # Call setRace
    char.setRace()

    # Call setGender
    char.setGender()

    

    # Display menu and get user input
    num = 0
    num = funcModule.displayMenu()

    match num:
        case '1':
            # Call setSkills
            char.setClass()
        case '2':
            # Call setClass
            char.setSkills()

    

    # Display
    print('Race: ' + char.race)
    print('Gender: ' + char.gender)

    if char.clss != None:
        print('Class: ' + char.clss)
    if char.cDesc != None:
        print(char.cDesc)

    print('Skills:')
    for i in char.skills:
        print('\t' + i)

    input('Press Enter to continue')

if __name__ == '__main__':
    main()
            
