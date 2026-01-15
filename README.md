# Text Game
An rpg game experienced through only the text in your console. Explore many different areas, with tons of stuff to explore in each one. If you want more to explore, you can download related projects or even create your own areas with the resources listed below.

# Running the Game
In order to run this game press the green "<> Code" button at the top of the page, at the bottom of the tab download the Zip folder. Extract the files from the zip folder and select which version of the game you want to play. Note that certain versions have requirements in order to use.
## Python Version
The python version of this game requires the python language to be installed in order to run. If you need to install python consult https://www.python.org/downloads/  
Open a terminal window and navigate to the folder containing the textGame.py file, then run "python textGame.py". If using windows, this can be done with the "cd" command.  
An easy way to navigate to the folder in the terminal is to first navigate to the folder in the file explorer and right click the folder and open a terminal. From here run "python textGame.py".
## Modified Content Disclaimer
When downloading content meant to be a modification to this game only download files with the .json suffix that are intended to be new areas for you to explore. Files of other types are not recommended as they are not designed to work with this game and can potentially contain malware. It is also important to remember that when downloading any files off of the internet, you do so at your own risk.

# Playing the Game
Once the game is up and running you have several commands that you can run, the full list can be found by using the "help" command in game.
## Main Game
Here you will use standard commands such as "here" and "use" to help you explore and interact with the world arround you. During exploration you can inspect structures, grab and use items, and talk to people. When you type the help command you will recieve the following help text:  
here - observe your current surroundings, goto [PATH] - take a path to a different room (only paths), grab [ITEM] - pickup an item that you find in a room (only items), talkto [PERSON] - have a conversation with someone in a room (only characters), inspect [STRUCTURE] - inspects a specified structure (only structures), inv [INVENTORY TYPE] - opens the specified inventory, use [INVENTORY ITEM] - use an item in your inventory, save [FILE NAME] - save to a save file, load [FILE NAME] - load from a save file
## Combat
When you enter a room with an enemy in it you will enter the combat state. If you are unprepared for combat, this can lead to devestating consequences. In the combat state you can either Attack or Block, when attacking you take the full force of the enemy's attack if they attack, but you also deal damage to the enemy. If you block, then you take reduced damage depending on the defense value of your shield. All items have an attack and defense value and you can use any item during combat. The attack stat is how much the item will deal when attacking your opponent and the defense stat is how much damage you repel when blocking an incoming attack. Every turn you have to select an item to use to either attack or block, to select an item, type the item's name as listed.
## Creating a Save File
Once you have made decent progress through the game, you may wish to leave and continue later. You are able to save your current progress to a file so that it can be loaded later. When you return to the program you can then use the load command in order to restore your game to where you left off. The relative commands are: save [FILE NAME] and load [FILE NAME], there is no limit to how many files you can save to  except for the available space on your hard drive.

# Modifying the Game
For those who wish to modify the content of the game, examples of how area files and the loader file should be organized are provided bellow. You can compare these templates to the already existing files in the areas folder above to help better understand how the files should be created. Since these files do not need to be compiled you do not need specialized software to edit them and they can be edited within a basic text editor such as notepad. For easier use though, an IDE is recommended to easily see any syntax errors you may have accidentally included.
## Creating Area Files
Once an Area file is created name it whatever you want followed by .json and put the file in the areas folder. In order to load the file into the game, add it to the loader.json file based on the example for Configuring loader.json.

        {
            "area": [
                "NAME OF THE AREA",
                "DESCRIPTION OF THE AREA",
                ["STARTING INVENTORY NAME", (OPTIONAL SECOND INVENTORY NAME)],
                ["ATTACKING INVENTORY NAME", "DEFENDING INVENTORY NAME"],
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
                        #Neither "on-grab" or "on-use" need to be implemented
                    ["ITEM NAME", "ITEM DESCRIPTION", "INVENTORY NAME", ATTACK VALUE, DEFENSE VALUE, {"on-grab": (OPTIONAL EVENT KEY), "on-use": (OPTIONAL EVENT KEY)}],
                    (SECOND ITEM)
                ],
        
                "enemies": [
                        ["ENEMY NAME", "ENEMY DESCRIPTION", HEALTH VALUE, ATTACK VALUE, DEFENSE VALUE, (OPTIONAL EVENT KEY)],
                        (SECOND ENEMY)
                ],
        
                "structures": [
                    ["STRUCTURE NAME", "STRUCTURE DESCRIPTION", (OPTIONAL EVENT KEY)],
                    (SECOND STRUCTURE)
                ],
        
                "events": [
                        #add/del event type ["add/del", "ROOM NAME", "TYPE", "PAYLOAD"]
                                #inventory Room Name ["add/del", "inventory", "INVENTORY TYPE", "PAYLOAD"]
                        #go event type ["go", "AREA NAME", "ROOM NAME"]
                        #mod event type ["mod", "INVENTORY TYPE", ["ITEM NAME", (OPTIONAL SECOND ITEM NAME)], ITEM VARIABLE INDEX, "pre/suf/alt", CHANGE/"CHANGE"]
                                #pre will add the change before the original
                                #suf will add the change after the original
                                #alt will completely replace the original
                                #If using numbers instead of strings pre or suf will add the numbers together and alt will replace it
                    [EVENT KEY, "EVENT COMPLETE DIALOGUE", [["add/del/go/mod", "ROOM NAME", "TYPE", "PAYLOAD"], [OPTIONAL SECOND EVENT COMPLETE ACTION]]],
                    (SECOND EVENT)
                ]
            },
        
            "SECOND ROOM": {SECOND ROOM}
        }
## Configuring loader.json
When you want to add more areas to your game than the ones initially provided, you will need to configure the loader to recognize the new packages.
In order to do this manually you will need to follow the bellow guidelines. You need to put a comma between list items, so one there is a next area file, you need to put a comma but when there is not another area file, put no comma.  
For an example check the default version of loader.json.

        {
                "areas": [
                    "AREA FILE NAME",
                    (OPTIONAL SECOND AREA FILE NAME)
                ],
                
                "start": "STARTING AREA FILE NAME"
        }  
If you want to easily modify the loader.json, run the loaderConfig.py file the same way you would run the game. The commands for it are, add [FILENAME] / del [FILENAME] / start [FILENAME] / end, for more details check loaderConfig.py
