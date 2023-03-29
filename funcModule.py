### funcModule ###

# displayMenu
# Displays main menu
def displayMenu():
    print('\tTalkingRevolver\'s Skyrim')
    print('\tCharacter Generator')
    print('\n\tType a number and press Enter to make a selection')
    print('\n\t1) Generate Class')
    print('\t2) Generate Random Skills')

    num = input()

    return num

# redunCheck
# Recieves a skill as a string from setSkills, and skills list
# Checks if a redundant skill is about to be added to self.skills
# A skill is redundant if it conflicts with another skill from a build
#   perspective; ie. Light Armor and Heavy Armor
# Returns a boolean; True if skill is redundant
def redunCheck(skill, sList):
    isRedun = False

    match skill:
        # Light Armor, Heavy Armor, Evasion
        case 'Light Armor' | 'Heavy Armor':
            if 'Heavy Armor' in sList:
                isRedun = True
                return isRedun
            elif 'Light Armor' in sList:
                isRedun = True
                return isRedun
        
        # One-handed, Two-handed, Light Weaponry, Heavy Weaponry
        case 'One-handed' | 'Two-handed':
            if 'One-handed' in sList:
                isRedun = True
                return isRedun
            elif 'Two-handed' in sList:
                isRedun = True
                return isRedun
        

    # If skill not redundant, return False
    return isRedun
