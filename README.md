# TalkingRevolver's Skyrim Character Generator #
Current version: 0.3.0

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
