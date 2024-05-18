area = 0

inventory = []

class Area:
  def __innit__(self, characters, items, enemies, tileX, tileY):
    self.characters = characters #People you can find in the area (Array)
    self.items = items #Items that can be found in the area (Array)
    self.enemies = enemies #Enemies that you can encounter in the area (Array)
    self.tileX = tileX #Width of the area
    self.tileY = tileY #Length of the area

class Character:
  def __innit__(self, name, dialogue, items):
    self.name = name #The name of the character
    self.dialogue = dialogue #The dialogue they can give when you speak to them (Array)
    self.items = items #Items that they will give you when you speak to them (Array)

class Enemy:
  def __innit__(self, name, damage, defense):
    self.name = name #The name of the enemy
    self.damage = damage #The damage it can deal per turn
    self.defense = defense #How much damage it can prevent when attacked

class Item:
  def __innit__(self, name, type, stat, equipability):
    self.name = name #The name of the created item
    self.type = type #Whether the item is a weapon, piece of armor, food etc.
    self.stat = stat #In relation to the item type, how effective it is, ex: weapon stat would be damage, food stat would be saturation
    self.equipability = equipability #0 if it can't be equipped, otherwise to designate specific armor or accessory slot

def interact():
  playerIn = input().split()
  #Keywords for actions bellow
  if (playerIn[0] == "here"):
    print("You are here")
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
