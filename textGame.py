import json, random

inventory = []
allAreas = []
currentArea = 0
currentRoom = ""
maxHealth = 100

def interact():
    global allAreas, currentArea, currentRoom, inventory
    print()
    playerIn = input().split()
    print()
    try:
        keyword = playerIn[0]
        if (keyword == "help"):
            print("here - observe your current surroundings\ngoto - take a path to a different room (only paths)\ngrab - pickup an item that you find in a room (only items)\ntalkto - have a conversation with someone in a room (only characters)\ninspect - inspects a specified structure (only structures)\ninv - opens the inventory\nuse - use an item in your inventory\nsave - save to a save file\nload - load from a save file")
        elif (keyword == "here"):
            print(allAreas[currentArea][currentRoom]["room"][0])
            print("People:")
            for x in range(len(allAreas[currentArea][currentRoom]["characters"])):
                print("--", allAreas[currentArea][currentRoom]["characters"][x][0], allAreas[currentArea][currentRoom]["characters"][x][1])
            print("Items:")
            for x in range(len(allAreas[currentArea][currentRoom]["items"])):
                print("--", allAreas[currentArea][currentRoom]["items"][x][0])
            print("Paths:")
            for x in range(len(allAreas[currentArea][currentRoom]["room"][1])):
                print("--", allAreas[currentArea][currentRoom]["room"][1][x])
            print("Structures:")
            for x in range(len(allAreas[currentArea][currentRoom]["structures"])):
                print("--", allAreas[currentArea][currentRoom]["structures"][x][0])
        elif (keyword == "goto"):
            try:
                location = playerIn[1]
                for x in range(len(allAreas[currentArea][currentRoom]["room"][1])):
                    if (allAreas[currentArea][currentRoom]["room"][1][x] == location):
                        currentRoom = allAreas[currentArea][currentRoom]["room"][1][x]
                        print("You went to", currentRoom)
                        try:
                            if (allAreas[currentArea][currentRoom]["room"][2] != None):
                                triggerEvent(allAreas[currentArea][currentRoom]["room"][2])
                        except(Exception):
                            pass
                        break
                    if (x == len(allAreas[currentArea][currentRoom]["room"][1])-1):
                        print("You searched, but found no such place.")
            except(Exception):
                print("Go to where?")
        elif (keyword == "grab"):
            try:
                item = playerIn[1]
                for x in range(len(allAreas[currentArea][currentRoom]["items"])):
                    if (allAreas[currentArea][currentRoom]["items"][x][0] == item):
                        inventory.append(allAreas[currentArea][currentRoom]["items"][x])
                        print(allAreas[currentArea][currentRoom]["items"][x][0], "was added to your inventory!")
                        del(allAreas[currentArea][currentRoom]["items"][x])
                        break
                    if (x == len(allAreas[currentArea][currentRoom]["items"])-1):
                        print("You searched, but found no such item.")
            except(Exception):
                print("Grab what?")
        elif (keyword == "talkto"):
            try:
                person = playerIn[1]
                for x in range(len(allAreas[currentArea][currentRoom]["characters"])):
                    if (allAreas[currentArea][currentRoom]["characters"][x][0] == person):
                        print(allAreas[currentArea][currentRoom]["characters"][x][0], ":", allAreas[currentArea][currentRoom]["characters"][x][2])
                        try:
                            if (allAreas[currentArea][currentRoom]["characters"][x][3] != None):
                                triggerEvent(allAreas[currentArea][currentRoom]["characters"][x][3])
                        except(Exception):
                            pass
                        break
                    if (x == len(allAreas[currentArea][currentRoom]["characters"])-1):
                        print("You searched, but were unable to find anyone by that name.")
            except(Exception):
                print("Talk to who?")
        elif (keyword == "inv"):
            print(inventory)
        elif (keyword == "inspect"):
            try:
                structure = playerIn[1]
                for x in range(len(allAreas[currentArea][currentRoom]["structures"])):
                    if (allAreas[currentArea][currentRoom]["structures"][x][0] == structure):
                        print(allAreas[currentArea][currentRoom]["structures"][x][1])
                        try:
                            if (allAreas[currentArea][currentRoom]["structures"][x][2] != None):
                                triggerEvent(allAreas[currentArea][currentRoom]["structures"][x][2])
                        except(Exception):
                            pass
                        break
                    if (x == len(allAreas[currentArea][currentRoom]["structures"])-1):
                        print("You searched, but were unable to find anything by that name.")
            except(Exception):
                print("Inspect what?")
        elif (keyword == "use"):
            try:
                if (0 == len(inventory)):
                    print("You couldn't find any items in your inventory.")
                else:
                    item = playerIn[1]
                    for x in range(len(inventory)):
                        if (inventory[x][0] == item):
                            triggerEvent(inventory[x][4])
                            break
                        if (x == len(inventory)-1):
                            print("You couldn't find an item like that in your inventory.")
            except(Exception):
                print("Use what? That didn't seem to work...")         
        elif (keyword == "save"):
            try:
                name = playerIn[1]
                file = 0
                try:
                    file = open("saves/"+name + ".json", "w")
                except(Exception):
                    try:
                        file = open("saves\\"+name + ".json", "w")
                    except(Exception):
                        print("File failed to open")
                toWrite = {
                    "inventory": inventory,
                    "allAreas": allAreas,
                    "currentArea": currentArea,
                    "currentRoom": currentRoom
                }
                json.dump(toWrite, file)
                file.close()
                print("Save was successful")
            except(Exception):
                print("No name was provided for the save or the file failed to write")
        elif (keyword == "load"):
            try:
                name = playerIn[1]
                try:
                    file = json.load(open("saves\\"+name+".json"))
                    inventory = file["inventory"]
                    allAreas = file["allAreas"]
                    currentArea = file["currentArea"]
                    currentRoom = file["currentRoom"]
                    print("Load was successful")
                except(Exception):
                    try:
                        file = json.load(open("saves/"+name+".json"))
                        inventory = file["inventory"]
                        allAreas = file["allAreas"]
                        currentArea = file["currentArea"]
                        currentRoom = file["currentRoom"]
                        print("Load was successful")
                    except(Exception):
                        print("File failed to be read")
            except(Exception):
                print("No name was provided for the save or the file failed to be read")
        else:
            print("You were too lost in thought to do anything, you consider looking for \"help\" to remember what you were doing.")
    except(Exception):
        print("You were too lost in thought to do anything, you consider looking for \"help\" to remember what you were doing.")

def triggerEvent(eventKey):
    global allAreas, currentArea, currentRoom, inventory
    for x in range(len(allAreas[currentArea][currentRoom]["events"])):
        if (eventKey == allAreas[currentArea][currentRoom]["events"][x][0]):
            print(allAreas[currentArea][currentRoom]["events"][x][1])
            for y in range(len(allAreas[currentArea][currentRoom]["events"][x][2])):
                action = allAreas[currentArea][currentRoom]["events"][x][2][y][0]
                location = allAreas[currentArea][currentRoom]["events"][x][2][y][1]
                key = allAreas[currentArea][currentRoom]["events"][x][2][y][2]
                if (action == "add"):
                    if (location == "inventory"):
                        inventory.append(key)
                    else:
                        effect = allAreas[currentArea][currentRoom]["events"][x][2][y][3]
                        if (key == "room"):
                            allAreas[currentArea][location]["room"][1].append(effect)
                        else:
                            allAreas[currentArea][location][key].append(effect)
                elif (action == "del"):
                    if (location == "inventory"):
                        for z in range(len(inventory)):
                            if (inventory[z][0] == key):
                                del(inventory[z])
                    else:
                        effect = allAreas[currentArea][currentRoom]["events"][x][2][y][3]
                        if (key == "room"):
                            for z in range(len(allAreas[currentArea][location]["room"][1])):
                                if (allAreas[currentArea][location]["room"][1][z] == effect):
                                    del(allAreas[currentArea][location]["room"][1][z])
                        else:
                            for z in range(len(allAreas[currentArea][location][key])):
                                if (allAreas[currentArea][location][key][z][0] == effect):
                                    del(allAreas[currentArea][location][key][z])
                elif (action == "go"):
                    effect = allAreas[currentArea][currentRoom]["events"][x][2][y][1]
                    roomEffect = allAreas[currentArea][currentRoom]["events"][x][2][y][2]
                    try:
                        for x in range(len(allAreas)):
                            if (allAreas[x]["area"][0] == effect):
                                currentArea = x
                                break
                        try:
                            currentRoom = roomEffect
                            print("You have entered:", allAreas[currentArea]["area"][0])
                            print(allAreas[currentArea][currentRoom]["room"][0])
                        except(Exception):
                            print("No area files were found")
                    except(Exception):
                        print("Your loader.json file could not be found") 

def combat():
    enemy = allAreas[currentArea][currentRoom]["enemies"][0]
    health = maxHealth
    enemyHealth = enemy[2]
    while(enemyHealth > 0 and health > 0):
        enemyTempAttack = enemy[3]
        playerAttack = 0
        playerTempAttack = 0
        print("\nYou are being attacked by a " + enemy[0] + "!\nHealth: "+str(enemyHealth)+"\n\nHealth: " + str(health) + "\na - Attack\nb - Block")
        playerIn = input()
        mode = 0
        if (playerIn == "a" or playerIn == "Attack" or playerIn == "attack"):
            mode = 1
            print("What will you attack with? (Type Item Name)\n", inventory)
        elif (playerIn == "b" or playerIn == "Block" or playerIn == "block"):
            mode = 2
            print("What will you block with? (Type Item Name)\n", inventory)
        else:
            print("You were too confused to do anything!")
        playerIn = input()
        for x in range(len(inventory)):
            if (playerIn == inventory[x][0]):
                playerAttack = inventory[x][2]
                playerTempAttack = playerAttack
                if (playerTempAttack >= enemy[4]):
                    playerTempAttack -= enemy[4]
                else:
                    playerTempAttack = 0

                if (enemyTempAttack >= inventory[x][3]):
                    enemyTempAttack -= inventory[x][3]
                else:
                    enemyTempAttack = 0
            else:
                print("You fumbled your items!")

            enemyIn = random.randrange(0, 1)
            if (enemyIn == 0):
                if (mode == 1):
                    health -= enemy[3]
                    enemyHealth -= playerAttack
                    print("The", enemy[0], "did", enemy[3], "damage!")
                    print("You did", playerAttack, "damage!")
                elif (mode == 2):
                    health -= enemyTempAttack
                    print("You blocked! The", enemy[0], "only did", enemyTempAttack, "damage!")
            else:
                if (mode == 1):
                    enemyHealth -= playerTempAttack
                    print("The", enemy[0], "blocked! You only did", playerTempAttack, "damage!")
                elif (mode == 2):
                    print("Both sides blocked nothing!")
    if (enemyHealth <= 0):
        print("You destroyed the", enemy[0] + "!")
        try:
            if (allAreas[currentArea][currentRoom]["enemies"][0][5] != None):
                triggerEvent(allAreas[currentArea][currentRoom]["enemies"][0][5])
        except(Exception):
            pass
        del(allAreas[currentArea][currentRoom]["enemies"][0])
    else:
        print("Prepare yourself! The", enemy[0], "is coming again!")

def start():
    global currentArea, currentRoom, allAreas
    print("\nWelcome to Text Game, type \"help\" for usable commands.\n")
    try:
        loader = json.load(open("loader.json"))
        for x in range(len(loader["areas"])):
            try: #Try normal folder typing
                allAreas.append(json.load(open("areas\\" + loader["areas"][x])))
                if (loader["areas"][x] == loader["start"]):
                    currentArea = len(allAreas)-1
            except(Exception):
                try: #Try alt folder typing
                    allAreas.append(json.load(open("areas/" + loader["areas"][x])))
                    if (loader["areas"][x] == loader["start"]):
                        currentArea = x
                except(Exception):
                    print(loader["areas"][x], "in your loader.json was not added")
        try:
            currentRoom = allAreas[currentArea]["area"][2]
            print("You have entered:", allAreas[currentArea]["area"][0])
            print(allAreas[currentArea][currentRoom]["room"][0])
        except(Exception):
            print("No area files were found")
            return(1)
    except(Exception):
        print("Your loader.json file could not be found")
        return(1)
    return(0)

def update():
    if (len(allAreas[currentArea][currentRoom]["enemies"]) > 0):
        combat()
    else:
        interact()
    return(0)

def end(errorCode):
    print("Error:", errorCode)

def main():
    num = start()
    while(num == 0):
        num = update()
    end(num)

main()
