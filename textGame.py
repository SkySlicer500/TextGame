import json

inventory = []
currentArea = 0

def interact():
  playerIn = input().split()
  #Keywords for actions bellow
  if (playerIn[0] == "here"):
    print(currentArea["area"][1]) #Give information of the current location
  else:
    print("You were too lost in thought to do anything")

def start():
  global currentArea
  file = open("area1.json")
  currentArea = json.load(file)
  print("You have entered:", currentArea["area"][0])
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
