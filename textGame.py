import json

inventory = []
currentArea = 0
currentRoom = ""

def interact():
    global currentArea, currentRoom
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
                        break
                    if (x == len(currentArea[currentRoom]["characters"])-1):
                        print("You searched, but were unable to find anyone by that name.")
            except(Exception):
                print("Talk to who?")
        elif (keyword == "inv"):
            print(inventory)
        elif (keyword == "use"):
            try:
                if (playerIn[2] == "on"):
                    item = playerIn[1]
                    event = playerIn[3]
                    for x in range(len(inventory)):
                        if (inventory[x][0] == item):
                            for y in range(len(currentArea[currentRoom]["events"])):
                                if (currentArea[currentRoom]["events"][y][0] == event):
                                    if (inventory[x][2] == currentArea[currentRoom]["events"][y][1]):
                                        print(currentArea[currentRoom]["events"][y][2])
                                        type = currentArea[currentRoom]["events"][y][3]
                                        effect = currentArea[currentRoom]["events"][y][4]
                                        if (type == "room"):
                                            currentArea[currentRoom]["room"][1].append(effect)
                                        elif (type == "characters"):
                                            currentArea[currentRoom]["characters"].append(effect)
                                        elif (type == "items"):
                                            currentArea[currentRoom]["items"].append(effect)
                                        elif (type == "enemies"):
                                            currentArea[currentRoom]["enemies"].append(effect)
                                        elif (type == "events"):
                                            currentArea[currentRoom]["enemies"].append(effect)
                                    break
                                if (y == len(currentArea[currentRoom]["events"])-1):
                                    print("Such a thing was not found in the room.")
                            break
                        if (x == len(inventory)-1):
                            print("You couldn't find an item like that in your inventory.")
                    if (0 == len(inventory)):
                        print("You couldn't find any items in your inventory.")
            except(Exception):
                print("Use what on what? That didn't seem to work...")         
        else:
            print("You were too lost in thought to do anything, you consider looking for \"help\" to remember what you were doing.")
    except(Exception):
        print("You were too lost in thought to do anything, you consider looking for \"help\" to remember what you were doing.")

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
