# Text Game
An rpg game experienced through only the text in your console.

# Running the Game
In order to run this game press the green "<> Code" button at the top of the page, at the bottom of the tab download the Zip folder. Extract the files from the zip folder and select which version of the game you want to play
## Python Version
<sub>The python version of this game requires the python language to be installed in order to run. If you need to install python consult https://www.python.org/downloads/</sub>
## Modified Content Disclaimer
When downloading content meant to be a modification to this game only download files with the .json suffix that are intended to be new areas for you to explore. Files of other types are not recommended as they are not designed to work with this game and can potentially contain malware. It is also important to remember that when downloading any files off of the internet, you do so at your own risk.

# Modifying the Game
For those who wish to modify the content of the game, examples of how area files and the loader file should be organized are provided bellow. You can compare these templates to the already existing files in the areas folder above to help better understand how the files should be created. Since these files do not need to be compiled you do not need specialized software to edit them and they can be edited within a basic text editor such as notepad.
## Creating Area Files
Once an Area file is created name it whatever you want followed by .json and put the file in the areas folder. In order to load the file into the game, add it to the loader.json file in the bellow instructions.

        {
            "area": [
                "NAME OF THE AREA",
                "DESCRIPTION OF THE AREA",
                "STARTING ROOM NAME"
            ],
        
            "ROOM NAME": {
                "room": [
                    "ROOM DESCRIPTION",
                    ["ROOM NAME", "SECOND ROOM YOU CAN GO TO"],
                    (Optional Event Key)
                ],
        
                "characters": [
                    ["FIRST NAME", "LAST NAME", "DIALOGUE", (OPTIONAL EVENT KEY)],
                    (SECOND CHARACTER)
                ],
        
                "items": [
                    ["ITEM NAME", "ITEM DESCRIPTION", ATTACK VALUE, DEFENSE VALUE, (OPTIONAL EVENT KEY)],
                    (SECOND ITEM)
                ],
        
                "enemies": [],
        
                "structures": [
                    ["STRUCTURE NAME", "STRUCTURE DESCRIPTION", (OPTIONAL EVENT KEY)],
                    (SECOND STRUCTURE)
                ],
        
                "events": [
                        #go event type ["go", "AREA NAME", "ROOM NAME"]
                    [EVENT KEY, "EVENT COMPLETE DIALOGUE", [["add/del/go", "ROOM NAME", "TYPE", "PAYLOAD"], [SECOND EVENT COMPLETE ACTION]]]
                ]
            },
        
            "SECOND ROOM": {SECOND ROOM}
        }
## Configuring loader.json
When you want to add more areas to your game than the ones initially provided, you will need to configure the loader to recognize the new packages.
In order to do this manually you will need to follow the bellow guidelines.

        {
                "areas": [
                    "AREA FILE",
                    (SECOND AREA FILE)
                ],
                
                "start": "STARTING AREA FILE"
        }
