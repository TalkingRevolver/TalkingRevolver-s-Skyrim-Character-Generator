### TalkingRevolver's Skyrim Character Generator ###
### ver 1.0.0 ###
import random
import os
import listModule
import funcModule

## Class - Character ##
class Character:
    # Constructor
    # Sets attributes to None, skills to [], flags to False
    def __init__(self):
        # Attributes
        self.race = None # Race
        self.gender = None # Gender
        self.clss = None # Class
        self.cDesc = None # Class description
        self.align = None # Alignment
        
        self.wPref = None # Weapon preference
        self.ePref = None # Element preference
        self.traits = [] # Character traits
        self.looks = [] # Character appearance
        self.start = None # Starting location for alternate start mods
        # Flags
        self.reqFlag = False # Requiem
        self.sreFlag = False # Skyrim Redone
        self.altsFlag = False # Alternate Start - Live Another Life
        self.altpFlag = False # Alternate Perspective
        self.rolFlag = False # Realm of Lorkhan
        self.subFlag = False # Skyrim Unbound
        self.db = None # For Unbound, is player Dragonborn
        self.zebFlag = False # Zebsirious - Races of Tamriel

        self.session = False # Marks start of session to prevent start()
                             #  from running more than once

        self.skills = [] # Skills list

    # start
    # Recieves input from user and sets mod flags accordingly
    def startProgram(self):
        # Only run prompts if self.session != True
        if self.session != True:
            # Requiem
            print('Are you using Requiem - The Roleplaying Overhaul? Y or N')
            choice = input()
            if choice.upper() == 'Y':
                self.reqFlag = True
            #If not using Requiem, ask about Skyrim Redone
            if self.reqFlag != True:
                print("Are you using Tend0's Skyrim Redone? Y or N")
                choice = input()
                if choice.upper() == 'Y':
                    self.sreFlag = True

            # Alternate Starts
            print('Are you using Alternate Start - Live Another Life? Y or N')
            choice = input()
            if choice.upper() == 'Y':
                self.altsFlag = True
        
            if self.altsFlag != True:
                print('Are you using Alternate Perspective? Y or N')
                choice = input()
                if choice.upper() == 'Y':
                    self.altpFlag = True
                else:
                    print('Are you using Skyrim Unbound? Y or N')
                    choice = input()
                    if choice.upper() == 'Y':
                        self.subFlag = True
                    else:
                        print('Are you using Realm of Lorkhan? Y or N')
                        choice = input()
                        if choice.upper() == 'Y':
                            self.rolFlag = True

            # Zebsirious
            print('Are you using Zebsirious - Races of Tamriel? Y or N')
            choice = input()
            if choice.upper() == 'Y':
                self.zebFlag = True

    # resetChar
    # Resets all attributes and lists
    def resetChar(self):
        self.skills = [] 
        self.race = None
        self.gender = None 
        self.clss = None 
        self.cDesc = None
        self.align = None 
        self.wPref = None
        self.ePref = None
        self.traits = []
        self.looks = [] 
        self.start = None 
        
    # setRace
    # Randomly gets string from raceList, sets to self.race
    def setRace(self):
        rList = listModule.raceList
        if self.zebFlag == True:
            for i in listModule.raceListZ:
                rList.append(i)
                
        num = random.randint(0, len(rList) - 1)

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
        if self.reqFlag == True:
            sList = listModule.skillListR
        elif self.sreFlag == True:
            sList = listModule.skillListSR
        else:
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
        # If using Skyrim Redone, use expanded class list
        if self.sreFlag == True:
            cList = listModule.classList2
        else:
            cList = listModule.classList1
        cNum = random.randint(0, len(cList) - 1)
        c = cList[cNum]
        self.clss = c

        # Check for overhaul mods, use associated skill list
        if self.reqFlag == True:
            sList = listModule.skillListCR
        elif self.sreFlag == True:
            sList = listModule.skillListCSR
        else:
            sList = listModule.skillListCV

        # Append class skills to self.skills
        l = sList.get(c)
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

        # If self.race == Kothringi, skin color is Silver
        # Else, choose from compList
        if r == 'Kothringi':
            self.looks.append('Silver')
        else:
            num = random.randint(0, len(sList) - 1)
            self.looks.append(sList[num])

        # If self.race == Khajiit OR Argonian OR Lilmothiit
        # Hair color is None
        if r == 'Khajiit' or r == 'Argonian' or r == 'Lilmothiit':
            self.looks.append(None)
        else:
            num = random.randint(0, len(listModule.hairList) - 1)
            self.looks.append(listModule.hairList[num])
        # Eye color
        num = random.randint(0, len(listModule.eyeList) - 1)
        self.looks.append(listModule.eyeList[num])

    # setStart
    # Randomly gets string from one of the start lists in listModule
    def setStart(self):
        if self.altsFlag == True:
            sList = listModule.startListAS
        elif self.altpFlag == True:
            sList = listModule.startListAP
        elif self.rolFlag == True:
            sList = listModule.startListRL
        elif self.subFlag == True:
            sList = listModule.startListSU
            dList = listModule.suDB
        else:
            sList = None

        if sList != None:
            num = random.randint(0, len(sList) - 1)
            self.start = sList[num]
            if self.subFlag == True:
                num = random.randint(0, len(dList) - 1)
                self.db = dList[num]
        else:
            self.start = None
            
    # reroll
    # Recieves rNum, rerolls an item according ot rNum
    def reroll(self, num):
        match num:
            case 1:
                self.setRace()
            case 2:
                self.setGender()
            case 3:
                self.setAppearance()
            case 4:
                self.setAlign()
            case 5:
                self.traits = []
                self.setTraits(self.align)
            case 6:
                if self.clss != None:
                    self.skills = []
                    self.wPref = None
                    self.ePref = None
                    self.setClass()
                else:
                    self.skills = []
                    self.wPref = None
                    self.ePref = None
                    self.setSkills()
            case 7:
                self.setStart()


## MAIN ##
def main():
    # Create Character object
    char = Character()

    # Call start()
    char.startProgram()

    # If user does not enter '2' at the end of the program, repeat
    choice = None
    while choice != '2':
        # Display menu and get user input
        num = 0
        num = funcModule.displayMenu()
        os.system('cls')

        match num:
            case '1':
                # Call setClass
                # Make sure skills is empty
                if char.skills != []:
                    char.skills = []
                char.setClass()
            case '2':
                # Call setSkills
                if char.skills != []:
                    char.skills = []
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

        # Call setStart
        char.setStart()

        # Display
        while True:
            choice = None
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

            if char.start != None:
                print('\n\tStart: ' + char.start)

            if char.db != None:
                print('\n\tDragonborn Status: ' + char.db)

            print('\n')
            # Pause
            print('Press Enter to continue')
            input()
            # Re-generate, reroll, or exit
            print('Type 0 to generate again, 1 to reroll a stat, 2 to exit')
            choice = input()

            if choice == '0':
                os.system('cls')
                char.resetChar()
                break
            elif choice == '1':
                print('Which item would you like to reroll?' +
                  'Enter a number and press enter.')
                print('\n\t1. Race\n\t2. Gender\n\t3. Alignment\n\t4. Appearance'+
                  '\n\t5. Traits\n\t6. Class/Skills\n\t7. Start\n\t8. Exit')
                rNum = input()
                if rNum != '8':
                    char.reroll(int(rNum))
            elif choice == '2':
                break

if __name__ == '__main__':
        main()
            
