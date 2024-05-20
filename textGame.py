import json

inventory = []
currentArea = 0
currentRoom = ""

def interact():
    global currentArea, currentRoom, inventory
    print()
    playerIn = input().split()
    print()
    try:
        keyword = playerIn[0]
        if (keyword == "help"):
            print("here - observe your current surroundings\ngoto - go to a different room\ngrab - pickup an item that you find in a room\ntalkto - have a conversation with someone in a room\ninv - opens the inventory\nuse - use an item on an object")
        elif (keyword == "here"):
            print(currentArea[currentRoom]["room"][0])
            print("People:")
            for x in range(len(currentArea[currentRoom]["characters"])):
                print("--", currentArea[currentRoom]["characters"][x][0], currentArea[currentRoom]["characters"][x][1])
            print("Items:")
            for x in range(len(currentArea[currentRoom]["items"])):
                print("--", currentArea[currentRoom]["items"][x][0])
            print("Paths:")
            for x in range(len(currentArea[currentRoom]["room"][1])):
                print("--", currentArea[currentRoom]["room"][1][x])
            print("Structures:")
            for x in range(len(currentArea[currentRoom]["structures"])):
                print("--", currentArea[currentRoom]["structures"][x][0])
        elif (keyword == "goto"):
            try:
                location = playerIn[1]
                for x in range(len(currentArea[currentRoom]["room"][1])):
                    if (currentArea[currentRoom]["room"][1][x] == location):
                        currentRoom = currentArea[currentRoom]["room"][1][x]
                        print("You went to", currentRoom)
                        print(currentArea[currentRoom]["room"][0])
                        break
                    if (x == len(currentArea[currentRoom]["room"][1])-1):
                        print("You searched, but found no such place.")
            except(Exception):
                print("Go to where?")
        elif (keyword == "grab"):
            try:
                item = playerIn[1]
                for x in range(len(currentArea[currentRoom]["items"])):
                    if (currentArea[currentRoom]["items"][x][0] == item):
                        inventory.append(currentArea[currentRoom]["items"][x])
                        print(currentArea[currentRoom]["items"][x][0], "was added to your inventory!")
                        del(currentArea[currentRoom]["items"][x])
                        break
                    if (x == len(currentArea[currentRoom]["items"])-1):
                        print("You searched, but found no such item.")
            except(Exception):
                print("Grab what?")
        elif (keyword == "talkto"):
            try:
                person = playerIn[1]
                for x in range(len(currentArea[currentRoom]["characters"])):
                    if (currentArea[currentRoom]["characters"][x][0] == person):
                        print(currentArea[currentRoom]["characters"][x][0], ":", currentArea[currentRoom]["characters"][x][2])
                        try:
                            if (currentArea[currentRoom]["characters"][x][3] != None):
                                triggerEvent(currentArea[currentRoom]["characters"][x][3])
                        except(Exception):
                            pass
                        break
                    if (x == len(currentArea[currentRoom]["characters"])-1):
                        print("You searched, but were unable to find anyone by that name.")
            except(Exception):
                print("Talk to who?")
        elif (keyword == "inv"):
            print(inventory)
        elif (keyword == "inspect"):
            try:
                structure = playerIn[1]
                for x in range(len(currentArea[currentRoom]["structures"])):
                    if (currentArea[currentRoom]["structures"][x][0] == structure):
                        print(currentArea[currentRoom]["structures"][x][1])
                        break
                    if (x == len(currentArea[currentRoom]["structures"])-1):
                        print("You searched, but were unable to find anything by that name.")
            except(Exception):
                print("Inspect what?")
        elif (keyword == "use"):
            try:
                if (playerIn[2] == "on"):
                    if (0 == len(inventory)):
                        print("You couldn't find any items in your inventory.")
                    else:
                        item = playerIn[1]
                        event = playerIn[3]
                        for x in range(len(inventory)):
                            if (inventory[x][0] == item):
                                triggerEvent(inventory[x][2])
                                break
                            if (x == len(inventory)-1):
                                print("You couldn't find an item like that in your inventory.")
            except(Exception):
                print("Use what on what? That didn't seem to work...")         
        else:
            print("You were too lost in thought to do anything, you consider looking for \"help\" to remember what you were doing.")
    except(Exception):
        print("You were too lost in thought to do anything, you consider looking for \"help\" to remember what you were doing.")

def triggerEvent(eventKey):
    global currentArea, currentRoom, inventory
    for x in range(len(currentArea[currentRoom]["events"])):
        if (eventKey == currentArea[currentRoom]["events"][x][1]):
            print(currentArea[currentRoom]["events"][x][2])
            for y in range(len(currentArea[currentRoom]["events"][x][3])):
                action = currentArea[currentRoom]["events"][x][3][y][0]
                key = currentArea[currentRoom]["events"][x][3][y][1]
                effect = currentArea[currentRoom]["events"][x][3][y][2]
                if (action == "add"):
                    if (key == "room"):
                        currentArea[currentRoom]["room"][1].append(effect)
                    elif (key == "inventory"):
                        inventory.append(effect)
                    else:
                        currentArea[currentRoom][key].append(effect)
                elif (action == "del"):
                    if (key == "room"):
                        for z in range(len(currentArea[currentRoom]["room"][1])):
                            if (currentArea[currentRoom]["room"][1][z] == effect):
                                del(currentArea[currentRoom]["room"][1][z])
                    elif (key == "inventory"):
                        for z in range(len(inventory)):
                            if (inventory[z][0] == effect):
                                del(inventory[z])
                    else:
                        for z in range(len(currentArea[currentRoom][key])):
                            if (currentArea[currentRoom][key][z][0] == effect):
                                del(currentArea[currentRoom][key][z])

def start():
    global currentArea, currentRoom
    print("\nWelcome to Text Game, type \"help\" for usable commands.\n")
    file = open("area1.json")
    currentArea = json.load(file)
    currentRoom = currentArea["area"][2]
    print("You have entered:", currentArea["area"][0])
    print(currentArea[currentRoom]["room"][0])
    return(0)

def update():
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
