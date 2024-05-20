# Text Game
An rpg game experienced through only the text in your console.

# Creating Area Files
Once an Area file is created name it whatever you want followed by .json and put the file in the areas folder. In order to load the file into the game, put it into the loader.json file.

        {
            "area": [
                "NAME OF THE AREA",
                "DESCRIPTION OF THE AREA",
                "STARTING ROOM NAME"
            ],
    
        "ROOM NAME": {
            "room": [
                "ROOM DESCRIPTION",
                ["ROOM NAME", "SECOND ROOM YOU CAN GO TO"]
            ],
    
            "characters": [
                ["FIRST NAME", "LAST NAME", "DIALOGUE", (OPTIONAL EVENT KEY)],
                (SECOND CHARACTER)
            ],
    
            "items": [
                ["ITEM NAME", "ITEM DESCRIPTION", (OPTIONAL EVENT KEY)],
                (SECOND ITEM)
            ],
    
            "enemies": [],
    
            "structures": [
                ["STRUCTURE NAME", "STRUCTURE DESCRIPTION", (OPTIONAL EVENT KEY)],
                (SECOND STRUCTURE)
            ],
    
            "events": [
                [EVENT KEY, "EVENT COMPLETE DIALOGUE", [["add/del", "ROOM NAME", "TYPE", "PAYLOAD"], [SECOND EVENT COMPLETE ACTION]]]
            ]
        },
    
        "SECOND ROOM": {SECOND ROOM}
    }
# Configuring loader.json
When you want to add more areas to your game than the ones initially provided, you will need to configure the loader to recognize the new packages.
In order to do this manually you will need to follow the bellow guidelines.

    {
        "areas": [
            "AREA FILE",
            (SECOND AREA FILE)
        ],
    
        "start": "STARTING AREA FILE"
    }
