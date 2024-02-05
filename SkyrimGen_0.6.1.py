### TalkingRevolver's Skyrim Character Generator ###
### ver 1.0.0 ###
import random
import os
import listModule
import funcModule

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
        self.wPref = None # Weapon preference
        self.ePref = None # Element preference
        self.traits = [] # Character traits
        self.looks = [] # Character appearance

    # setRace
    # Randomly gets string from raceList, sets to self.race
    def setRace(self):
        num = random.randint(0, len(listModule.raceList) - 1)

        self.race = listModule.raceList[num]

    # setGender
    # Randomly gets string from list, sets to self.gender
    def setGender(self):
        # List of genders
        gList = ['Male', 'Female', 'Other']

        num = random.randint(0, len(gList) - 1)

        self.gender = gList[num]

    # setSkills
    # Randomly gets a given number of strings from skillsListV,
    #   appends to self.skills
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
            if skill in listModule.prefSkills:
                self.setPref(skill)

    # setClass
    # Randomly gets a string from classList and associated description
    #   string and skill list
    # Sets self.class and self.cDesc
    # Appends skills to self.skills
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
            if i in listModule.prefSkills:
                self.setPref(i)

        # Set class description
        self.cDesc = listModule.cDesc.get(c)

    # setPref
    # Generates a weapon preference if 'One-handed' or 'Two-handed'
    #   is in self.skills, or element preference if 'Destrustion'
    #   is in self.skills
    # Randomly gets string from ohandList, thandList, or eList
    # Sets to self.wPref and/or self.ePref respectively
    def setPref(self, skill):
        match skill:
            case "One-handed":
                num = random.randint(0, len(listModule.ohandList)-1)
                self.wPref = listModule.ohandList[num]
            case "Two-handed":
                num = random.randint(0, len(listModule.thandList)-1)
                self.wPref = listModule.thandList[num]
            case "Destruction":
                num = random.randint(0, len(listModule.eList)-1)
                self.ePref = listModule.eList[num]

    # setAlign
    # Randomly gets string from alignList, sets to self.align
    def setAlign(self):
        num = random.randint(0, len(listModule.alignList) - 1)

        self.align = listModule.alignList[num]

    # setTraits
    # Recieves self.align
    # Randomly gets 3 strings from Traits lists,
    #   appends to self.traits
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

    # setAppearance
    # Recieves self.race
    # Randomly gets strings from Appearance lists, appends to self.looks
    def setAppearance(self, r):
        # Skin / Fur color
        if r == 'Argonian':
            sList = listModule.scalesList
        elif r == 'Khajiit':
            sList = listModule.furList
        else:
            sList = listModule.compList

        num = random.randint(0, len(sList) - 1)
        self.looks.append(sList[num])

        # If self.race == Khajiit OR Argonian
        # Hair color is None
        if r == 'Khajiit' or r == 'Argonian':
            self.looks.append(None)
        else:
            num = random.randint(0, len(listModule.hairList) - 1)
            self.looks.append(listModule.hairList[num])
        # Eye color
        num = random.randint(0, len(listModule.eyeList) - 1)
        self.looks.append(listModule.eyeList[num])
            

## MAIN ##
def main():
    # Create Character object
    char = Character()

    # Display menu and get user input
    num = 0
    num = funcModule.displayMenu()
    os.system('cls')

    match num:
        case '1':
            # Call setSkills
            char.setClass()
        case '2':
            # Call setClass
            char.setSkills()
                
    # Call setRace
    char.setRace()

    # Call setGender
    char.setGender()

    # Call setAppearance
    char.setAppearance(char.race)

    # Call setAlign
    char.setAlign()
    
    # Call setTraits
    char.setTraits(char.align)

    # Display
    print('Race: ' + char.race)
    print('Gender: ' + char.gender)

    if char.looks[0] in listModule.scalesList:
        print('\nSkin Color: ' + char.looks[0])
    elif char.looks[0] in listModule.furList:
        print('\nFur Color: ' + char.looks[0])
    else:
        print('\nComplexion: ' + char.looks[0])

    if char.looks[1] != None:
        print('Hair Color: ' + char.looks[1])
        
    print('Eye Color: ' + char.looks[2])

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
    
    if char.wPref != None:
        print('\n\tWeapon Preference: ' + char.wPref)
    if char.ePref != None:
        print('\n\tElement Preference: ' + char.ePref)

    print('\n')
    

if __name__ == '__main__':
    choice = ''
    while choice != '1':
        main()
        print('Press Enter to generate again, or type 1 to exit')
        choice = input()
        os.system('cls')    
