### funcModule ###

# displayMenu
# Called by main()
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
# Called by self.setSkills()
# Recieves a skill as a string, and self.skills
# Checks if a redundant skill is about to be added to self.skills
# A skill is redundant if it conflicts with another skill from a build
#   perspective; ie. Light Armor and Heavy Armor
# Returns a boolean; True if skill is redundant
def redunCheck(skill, sList):
    isRedun = False

    match skill:
        # Light Armor, Heavy Armor, Evasion
        case 'Light Armor' | 'Heavy Armor' | 'Evasion':
            if 'Heavy Armor' in sList:
                isRedun = True
                return isRedun
            elif 'Light Armor' in sList:
                isRedun = True
                return isRedun
            elif 'Evasion' in sList:
                isRedun = True
                return isRedun
        
        # One-handed, Two-handed
        case 'One-handed' | 'Two-handed':
            if 'One-handed' in sList:
                isRedun = True
                return isRedun
            elif 'Two-handed' in sList:
                isRedun = True
                return isRedun
        

    # If skill not redundant, return False
    return isRedun

# chanceRoll
# Simulates percent chance rolls
# Recieves string (item), gets percent value associated with item from
#   percentLists (per)
# Generates a number, if given value > number, reroll == False
#   (item will not be re-generated within method)
# Else, reroll == True (item will be re-generated within method)
# Returns reroll
def chanceRoll(item, per):
    match item:
        case '':
            percent = percentLists.dic.get(c)

    
