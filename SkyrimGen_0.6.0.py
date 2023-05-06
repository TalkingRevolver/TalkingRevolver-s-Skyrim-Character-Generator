### listModule ###

## Vanilla Lists ##
raceList = ['Nord', 'Imperial', 'Redguard', 'Breton', 'Altmer', 'Bosmer',
                 'Dunmer', 'Orc', 'Khajiit', 'Argonian']

skillListV = ['One-handed', 'Two-handed', 'Light Armor', 'Heavy Armor',
                 'Block', 'Archery', 'Smithing', 'Sneak', 'Alchemy',
                 'Lockpicking', 'Pickpocket', 'Speech', 'Destruction',
                 'Restoration', 'Alteration', 'Illusion', 'Conjuration',
                 'Enchanting']


## Classes ##
classList = ['Agent', 'Assassin', 'Barbarian', 'Brigand', 'Cleric', 'Conjurer',
             'Craftsman', 'Knight', 'Nightblade', 'Paladin', 'Ranger',
             'Shaman', 'Skirmisher', 'Sorcerer', 'Spellsword', 'Theif']

skillListC = {'Agent':['Sneak', 'Speech',
                'Choose 2 from: One-handed, Illusion, Lockpicking'],
            'Assassin':['Sneak', 'One-handed',
                'Choose 2 from: Archery, Alchemy, Light Armor'],
            'Barbarian':['Two-handed', 'Light Armor',
                'Choose 2 from: Archery, Smithing, Alteration'],
             'Brigand':['Sneak', 'One-handed', '1 Warrior skill of your choice',
                        '1 Stealth skill of your choice'],
             'Cleric':['Restoration', 'Destruction',
                'Choose 2 from: One-handed, Alteration, Alchemy'],
             'Conjurer':['Conjuration', 'Destruction',
                'Choose 2 from: Alteration, Illusion, Sneak'],
             'Craftsman':['Smithing', 'Speech', '1 Warrior skill of your choice',
                '1 Stealth skill of your choice'],
             'Knight':['One-handed', 'Block', 'Heavy Armor',
                'Choose 1 from: Speech, Smithing, Archery'],
             'Nightblade':['Sneak', 'Illusion', 'One-handed',
                'Choose 1 from: Light Armor, Destruction, Lockpicking'],
             'Paladin':['Heavy Armor', 'Two-handed', 'Restoration',
                'Choose 1 from: Destruction, Enchanting, Speech'],
             'Ranger':['Sneak', 'Archery',
                'Choose 2 from: Light Armor, Alchemy, Smithing'],
             'Shaman':['Alchemy', 'Conjuration', 'Alteration',
                'Choose 1 from: Destruction, Restoration, Light Armor'],
             'Skirmisher':['Light Armor', 'One-handed',
                'Choose 2 from: Light Armor, Block, Sneak'],
             'Sorcerer':['Heavy Armor', 'Destruction', 'Enchanting',
                '1 Magic skill of your choice'],
             'Spellsword':['One-handed', 'Destruction', 'Light Armor',
                '1 Magic skill of your choice'],
             'Thief':['Sneak', 'Lockpicking',
                'Choose 2 from: Pickpocket, Light Armor, Speech']}

cDesc = {   'Agent':'Masters of espionage and trickery. They prefer to have\n\tothers do'+
            'their dirty work if they cannot talk their\n\tway out of it.',
            'Assassin':'Killers who prefer a more subtle approach.\n' +
            '/tMany make use of the deadliest of poisons.',
            'Barbarian': 'Terrifying warriors who fight with sheer ferocity.'+
            '\n\tThey sometimes employ old magics as a substitute for armor.',
            'Brigand':'Those who choose to live as an outcast, by force or by choice' +
            '\n\tThey come from many walks of life, and often resort to crime.',
            'Cleric':'Holy mages highly valued as healers. They also often '+
            '\n\ttake up the task of rooting out evil and the undead.',
            'Conjurer':'Mages who specialize in summoning and reanimation.\n\t'+
            'They often find themselves ostracized from society\n\tfor their interests.',
            'Craftsman':'Merchants trying to make an honest living. They may use\n' +
            '/teither word or weapon to aqcuire resources.',
            'Knight':'Knights prefer the tried and true sword and shield. Some serve\n' +
            '\tnobility, others live the life of a sword-for-hire.',
            'Nightblade':'Stealthy fighters who use magic to supplement/n' +
            'their own abilities. While they make great assassins, some\n' +
            'simply revel in trickery and chaos.',
            'Paladin':'Zealous warriors versed in combat and holy magic.\n\tWhether'+
            'they protect the weak or burn away evil,\n\tthey are considered paragons'+
            'of all that is good.',
            'Ranger':'Fighters who prefer to engage foes at a distance.\n\t'+
            'Some are archers in the military, while others are\n\thunters who live off the land.',
            'Shaman':'Mages with a connection to the spirits of nature.\n' +
            '\tThey have knowledge of flora, fauna, and old magics.',
            'Skirmisher':'Warriors who trade armor for mobility.'+
            '\n\tThey are adept at scouting and ambushing.',
            'Sorcerer':'Mages who protect themselves with steel instead of '+
            'enchanted robes.\n\tThey are masters of both offense and defense.',
            'Spellsword':'Warriors who wield both a weapon and magic. '+
            'They employ a\n\tvariety of magical skills and walk\n\ta variety of paths.',
            'Thief':'Rogues adept at taking what isn’t theirs.\n\t'+
            'Burglary, picking pockets, and mugging are among\n\ta thief’s skillsets.'}

## Weapon Preference ##

# List of skills that trigger preference generation
prefSkills = ['One-handed', 'Two-handed', 'Destruction']

ohandList = ['Long blade', 'Short blade', 'Axe', 'Blunt']
thandList = ['Greatsword', 'Battleaxe', 'Warhammer']
eList = ['Fire', 'Frost', 'Shock']

## Alignments ##
alignList = ['Chaotic Good', 'Chaotic Neutral', 'Chaotic Evil',
             'Lawful Good', 'Lawful Neutral', 'Lawful Evil']

## Traits ##
tListPos = ['Compassionate', 'Generous', 'Child at heart', 'Creative',
            'Inquisitive', 'Charming', 'Art Lover', 'Self-sacrificing',
            'Empathetic', 'Animal Lover', 'Passionate', 'Adventurous',
            'Food Lover']

tListNeg = ['Selfish', 'Quick to anger', 'Spiteful', 'Cynical', 'Abrasive',
            'Antisocial', 'Alcoholic', 'Inconsiderate', 'Bloodthirsty',
            'Destructive', 'Deceitful', 'Manipulative', 'Racist']

tListNeu = ['Impulsive', 'Melancholic', 'Slow-witted', 'Quiet',
            'Dislikes children', 'Dislikes animals', 'Dislikes alcohol',
            'Intelligent', 'Single-minded', 'Imposing', 'Awkward',
            'Rabble-rouser', 'Restless', 'Well-intentioned']

## Appearance ##
compList = ['Pale', 'Fair', 'Average', 'Dark']

scalesList = ['Green', 'Brown', 'Black', 'Red', 'Blue', 'Purple']

furList = ['Light Brown', 'Dark Brown', 'Black', 'White', 'Cream', 'Yellow',
           'Orange', 'Red']

hairList = ['Black', 'Grey', 'White', 'Light BLonde', 'Dirty Blonde',
            'Light Brown', 'Dark Brown', 'Auburn', 'Red']

eyeList = ['Brown', 'Green', 'Blue', 'Hazel', 'Grey', 'Exotic']
