import json

#Add method that checks for the existence of files later 

file = json.load(open("loader.json"))

print("\nEnter command or type anything for help")

spin = True
areas = file["areas"]
start = file["start"]

while(spin):
    print("\nCurrent Loader:\nAreas:", areas, "\nStart:", start, "\n")
    try:
        userIn = input().split()
        if (userIn[0] == "add"):
            areas.append(userIn[1])
            print("Added", userIn[1])
        elif (userIn[0] == "del"):
            for x in range(len(areas)):
                if (areas[x] == userIn[1]):
                    del(areas[x])
                    print("Deleted", userIn[1])
                    break
                print("There was no file of that name")
        elif (userIn[0] == "start"):
            start = userIn[1]
            print("Start is now", userIn[1])
        elif (userIn[0] == "end"):
            toWrite = {
                "areas": areas,
                "start": start
            }
            file = open("loader.json", "w")
            json.dump(toWrite, file)
            file.close()
            spin = False
        else:
            print("add [FILENAME] - Add a file to the loader\ndel [FILENAME] - Delete a file from the loader\nstart [FILENAME] - Select a file to load on start\nend - Exit and Save the program")
    except(Exception):
        print("add [FILENAME] - Add a file to the loader\ndel [FILENAME] - Delete a file from the loader\nstart [FILENAME] - Select a file to load on start\nend - Exit and Save the program")

print("loaderConfig.py has completed operations successfully")
