# Text Game
An rpg game experienced through only the text in your console.

# Creating JSON Areas
    {
        "area": [
            "NAME OF THE AREA",
            "DESCRIPTION OF THE AREA",
            "STARTING ROOM"
        ],
    
        "ROOM NAME": {
            "room": [
                "ROOM DESCRIPTION",
                [ARRAY OF ROOMS YOU CAN GO TO]
            ],
    
            "characters": [
                ["FIRST NAME", "LAST NAME", "DIALOGUE", (OPTIONAL EVENT KEY)],
                [SECOND CHARACTER]
            ],
    
            "items": [
                ["ITEM NAME", "ITEM DESCRIPTION", (OPTIONAL EVENT KEY)]
            ],
    
            "enemies": [],
    
            "structures": [
                ["STRUCTURE NAME", "STRUCTURE DESCRIPTION", (OPTIONAL EVENT KEY)]
            ],
    
            "events": [
                [EVENT KEY, "EVENT COMPLETE DIALOGUE", [["add/del", "ROOM NAME", "TYPE", "PAYLOAD"], [SECOND EVENT COMPLETE ACTION]]]
            ]
        },
    
        "SECOND ROOM": {SECOND ROOM}
    }
