import json

inventory = []
currentArea = 0
currentRoom = ""

def interact():
    global currentArea, currentRoom
    playerIn = input().split()
    try:
        #Keywords for actions bellow
        keyword = playerIn[0]
        if (keyword == "help"):
            print("here - observe your current surroundings\ngoto - go to a different room\ngrab - pickup an item that you find in a room\ntalkto - have a conversation with someone in a room\ninv - opens the inventory")
        elif (keyword == "here"):
            print("\n", currentArea[currentRoom]["room"][0], "\n")
            print("People:")
            for x in range(len(currentArea[currentRoom]["characters"])):
                print("--", currentArea[currentRoom]["characters"][x][0], currentArea[currentRoom]["characters"][x][1], "--")
            print("Items:")
            for x in range(len(currentArea[currentRoom]["items"])):
                print("--", currentArea[currentRoom]["items"][x][0], "--")
            print("Rooms:")
            for x in range(len(currentArea[currentRoom]["room"][1])):
                print("--", currentArea[currentRoom]["room"][1][x], "--")

        elif (keyword == "goto"):
            try:
                location = playerIn[1]
                for x in range(len(currentArea[currentRoom]["room"][1])):
                    if (currentArea[currentRoom]["room"][1][x] == location):
                        currentRoom = currentArea[currentRoom]["room"][1][x]
                        break
                print("You went to", currentRoom)
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
            except(Exception):
                print("Grab what?")
        elif (keyword == "talkto"):
            try:
                person = playerIn[1]
                for x in range(len(currentArea[currentRoom]["characters"])):
                    if (currentArea[currentRoom]["characters"][x][0] == person):
                        print(currentArea[currentRoom]["characters"][x][0], ":", currentArea[currentRoom]["characters"][x][2])
                        break
            except(Exception):
                print("Talk to who?")
        elif (keyword == "inv"):
            print(inventory)
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
