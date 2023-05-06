# TalkingRevolver's Skyrim Character Generator #
Current version: 0.6.0

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
