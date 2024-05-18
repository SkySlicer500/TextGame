area = 0

class Item:
  def __innit__(self, name, type, stat, equipability):
    self.name = name #The name of the created item
    self.type = type #Whether the item is a weapon, piece of armor, food etc.
    self.stat = stat #In relation to the item type, how effective it is, ex: weapon stat would be damage, food stat would be saturation
    self.equipability = equipability #0 if it can't be equipped, otherwise to designate specific armor or accessory slot

def interact():
  playerIn = input().split()
  #Keywords for actions bellow
  if (playerIn[0] == ""):
    #action goes here
  else:
    print("You were too lost in thought to do anything")

def start():
  return(0)

def update():
  return(0)

def end(errorCode):
  print("Error:", errorCode)

def main():
  num = start()
  while(num == 0):
    num = update()
  end(num)

main()
