### TalkingRevolver's Skyrim Character Generator ###
### ver 1.0.0 ###
import logging
import random

## Logging ##
logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s - %(message)s')

## Class - Character ##
class Character:
    # Constructor
    # Sets attributes to None, skills to []
    def __init__(self):
        self.race = None # Race
        self.gender = None # Gender
        self.skills = [] # Skills list

    # setRace
    # Picks a string from a list via a random number, sets to self.race
    def setRace(self):
        # List of races
        rList = ['Nord', 'Imperial', 'Redguard', 'Breton', 'Altmer', 'Bosmer',
                 'Dunmer', 'Orc', 'Khajiit', 'Argonian']

        num = random.randint(0, len(rList) - 1)

        self.race = rList[num]

        ### DEBUG ###
        logging.debug('race = ' + self.race)
        ### ----- ###

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
        sList = ['One-handed', 'Two-handed', 'Light Armor', 'Heavy Armor',
                 'Block', 'Archery', 'Smithing', 'Sneak', 'Alchemy',
                 'Lockpicking', 'Pickpocket', 'Speech', 'Destruction',
                 'Restoration', 'Alteration', 'Illusion', 'Conjuration',
                 'Enchanting']

        for i in range(4):
            num = random.randint(0, len(sList) - 1)

            # Check if skill is already in self.skills
            while sList[num] in self.skills:
                num = random.randint(0, len(sList) - 1)

            skill = sList[num]

            self.skills.append(skill)


## MAIN ##
def main():
    # Create Character object
    char = Character()

    # Call setRace
    char.setRace()

    # Call setGender
    char.setGender()

    # Call setSkills
    char.setSkills()

    # Display
    race = char.race
    gen = char.gender
    print(race)
    print(gen)

    for i in range(4):
        print(char.skills[i])

if __name__ == '__main__':
    main()
            
