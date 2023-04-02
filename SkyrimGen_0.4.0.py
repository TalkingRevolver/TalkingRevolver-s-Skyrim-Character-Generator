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
        self.align = None # Alignment
        self.skills = [] # Skills list
        self.traits = [] # Character traits

    # setRace
    # Generates a random number, gets string from raceList, sets to self.race
    def setRace(self):
        num = random.randint(0, len(listModule.raceList) - 1)

        self.race = listModule.raceList[num]

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

    # setAlign
    # Generates an alignment from alignList, sets to self.align
    def setAlign(self):
        num = random.randint(0, len(listModule.alignList) - 1)

        self.align = listModule.alignList[num]

    # setTraits
    # Recieves self.align
    # Generates a random number, gets string from trait lists,
    #   appends to self.traits
    # Generation is affected by self.align
    def setTraits(self, a):
        match a:
            case "Lawful Good":
                # 2 positive traits, 1 neutral trait
                tList = listModule.tListPos
                for i in range(1, 3):
                    num = random.randint(0, len(tList)-1)
                    t = tList[num]
                    # Check if trait is in self.traits
                    while t in self.traits:
                        num = random.randint(0, len(tList)-1)
                        t = tList[num]
                    self.traits.append(t)

                tList = listModule.tListNeu
                num = random.randint(0, len(tList)-1)
                t = tList[num]
                while t in self.traits:
                        num = random.randint(0, len(tList)-1)
                        t = tList[num]
                self.traits.append(t)

            case "Lawful Evil":
                # 2 negative traits, 1 neutral trait
                tList = listModule.tListNeg
                for i in range(1, 3):
                    num = random.randint(0, len(tList)-1)
                    t = tList[num]
                    # Check if trait is in self.traits
                    while t in self.traits:
                        num = random.randint(0, len(tList)-1)
                        t = tList[num]
                    self.traits.append(t)

                tList = listModule.tListNeu
                num = random.randint(0, len(tList)-1)
                t = tList[num]
                while t in self.traits:
                        num = random.randint(0, len(tList)-1)
                        t = tList[num]
                self.traits.append(t)

            case 'Lawful Neutral' | 'Chaotic Neutral':
                # 2 neutral, 1 positive OR 1 negative
                tList = listModule.tListNeu
                for i in range(1, 3):
                    num = random.randint(0, len(tList)-1)
                    t = tList[num]
                    # Check if trait is in self.traits
                    while t in self.traits:
                        num = random.randint(0, len(tList)-1)
                        t = tList[num]
                    self.traits.append(t)

                listNum = random.randint(1, 2)
                if listNum == 1:
                    tList = listModule.tListPos
                else:
                    tList = listModule.tListNeg
                num = random.randint(0, len(tList)-1)
                t = tList[num]
                self.traits.append(t)

            case 'Chaotic Good' | 'Chaotic Evil':
                # 1 from each list
                tList = listModule.tListPos
                tNum = random.randint(0, len(tList)-1)
                self.traits.append(tList[tNum])
                tList = listModule.tListNeg
                tNum = random.randint(0, len(tList)-1)
                self.traits.append(tList[tNum])
                tList = listModule.tListNeu
                tNum = random.randint(0, len(tList)-1)
                self.traits.append(tList[tNum])

            case _:
                # if self.align == None, generate randomly
                for i in range(1, 4):
                    listNum = random.randint(1, 3)
                    if listNum == 1:
                        tList = listModule.tListPos
                    elif listNum == 2:
                        tList = listModule.tListNeg
                    else:
                        tList = listModule.tListNeu

                    num = random.randint(0, len(tList)-1)
                    t = tList[num]
                    while t in self.traits:
                        num = random.randint(0, len(tList)-1)
                        t = tList[num]
                    self.traits.append(t)

## MAIN ##
def main():
    # Create Character object
    char = Character()

    # Call setRace
    char.setRace()

    # Call setGender
    char.setGender()

    # Call setAlign
    char.setAlign()
    
    
    # Call setTraits
    char.setTraits(char.align)
    
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

    if char.align != None:
        print('\nAlignment: ' + char.align)

    print('\nTraits: ')
    for i in char.traits:
        print('\t' + i)
    
    if char.clss != None:
        print('\nClass: ' + char.clss)
    if char.cDesc != None:
        print(char.cDesc)

    print('\nSkills:')
    for i in char.skills:
        print('\t' + i)
    print('\n')

    input('Press Enter to continue')

if __name__ == '__main__':
    main()
            
