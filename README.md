# TalkingRevolver's Skyrim Character Generator #
Current version: 0.9.0

Changelogs:



	03/22/2023 - ver 0.1.0
	- Initial commit

	03/26/2023 - ver 0.2.0
	- Implemented listModule
	- Added classic RPG class generation
		- Class titles, skill lists, and descriptions
	- Removed logging from release builds
	- Packaged executable in dist folder

	03/29/23 - ver 0.3.0
	- Implemented funcModule
	- Added redundancy checks to setSkills
	    - One-handed will not be in the list of skills at the same time as 
		Two-handed, and vice versa
	    - Light Armor will not be in the list of skills at the same time as
		Heavy Armor, and vice versa
	- Main menu is now handled by displayMenu function
	- Added ability to choose number of skills generated

	04/02/23 - ver 0.4.0
	- Added alignment and trait lists to listModule
	- Implemneted alignment and trait generation
	- Minor changes to display for readability

	05/02/2023 - ver 0.5.0
	- Added appearance lists to listModule
	- Implemented character appearance generation

	05/06/2023 - ver 0.6.0
	- Added weapon preference lists to listModule
	- Implemented weapon preference generation
		- 'Blade', 'blunt', or 'axe' for One-handed and Two-handed
		- 'Fire', 'frost', or 'shock' for Destruction'

	02/28/24 - ver 0.9.0
	- Added flags within Character class for mods
		- Requiem - The Roleplaying Overhaul
		- T3end0's Skyrim Redone
		- Alternate Start - Live Another Life	
		- Alternate Perspective
		- Realm of Lorkhan
		- Skyrim Unbound
		- Zebsirious - Races of Tamriel
	- Added initial prompts to set mod flags
	- Added separate skill lists for Requiem and Skyrim Redone to listModule
	- Added additional class and class skill lists for Skyrim Redone to listModule
	- Added additional race list for Zebsirious to listModule
	- Added starting location lists for Alt. Start, Alt. Perspective, Realm of Lorkhan
		and Skyrim Unbound to listModule
	- Added more functionality to end of generation
		- Added Prompts and reroll() function to facilitate re-generating
			specific items
		- Added resetChar() function to reset attributes when restarting 
			program
		- Modified checks and flags so everything runs smoothly when restarting
			program
	- Minor text edits for consistency, clarity, and readability
	- Added application icon

	06/01/24 - ver. 1.0.0
	- Added support for Wintersun - Faiths of Skyrim
	- Added 'Neutral Good' and 'Neutral Evil' to alignment generation
		- Added relevant generation options to traits
	- Added functionality for writing character info to text file for easy access later
