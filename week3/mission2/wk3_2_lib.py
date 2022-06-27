from minecraft import enums
from minecraft.location import as_loc

def getCardinalDirection(direction: enums.Direction):
  if (direction == 'up'): 
    return as_loc(0, 1, 0)
  if (direction == 'down'): 
    return as_loc(0, -1, 0)

  actionDirection = 180 + agent.rotation
  if direction == 'forward':
    pass
  elif direction == 'back':
    actionDirection += 180
    pass
  elif direction == 'left':
    actionDirection += 270
    pass
  elif direction == 'right':
    actionDirection += 90
    pass
  
  actionDirection = (actionDirection % 360) - 180
  
  if actionDirection == -180.0:
    return as_loc(0, 0, -1)
  elif actionDirection == -90.0:
    return as_loc(1, 0, 0)
  elif actionDirection == 0.0:
    return as_loc(0, 0, 1)
  elif actionDirection == 90.0:
    return as_loc(-1, 0, 0)

def canPlaceBlock(loc, direction: enums.Direction):
  checkLoc = agent.position.__add__(getCardinalDirection(direction))
  return checkLoc == loc

def pickUpColour(direction: enums.Direction):
  colorDict = {
    "white_concrete": 0,
    "orange_concrete": 1,
    "magenta_concrete": 2,
    "light_blue_concrete": 3
    "yellow_concrete": 4,
    "lime_concrete": 5,
    "pink_concrete": 6,
    "gray_concrete": 7,
    "silver_concrete": 8,
    "cyan_concrete": 9,
    "purple_concrete": 10,
    "blue_concrete": 11,
    "brown_concrete": 12,
    "green_concrete": 13,
    "red_concrete": 14,
    "black_concrete": 15,
  }

  for key in colorDict:
    if checkBlockFromAgent(key, direction):
      agent.destroy(direction)
      count = 0
      if agent.get_item(1) == 'concrete':
        count = agent.get_item_count(1)
      
      agent.give(('concrete', colorDict[key], ""), count + 1, colorDict[key])
      break

def canPlaceColourBlock(slot: int, direction: enums.Direction):
  check = [as_loc(209, 10, -284), as_loc(214, 10, -284), as_loc(219, 10, -284)]
  canPlace = False

  for c in check:
    if (canPlaceBlock(c, direction)):
        canPlace = True
        break
  
  if (not canPlace):
    player.whisper('I can\'t place blocks here!')
    return False

  if (agent.get_item(slot) == 'concrete'):
    if (agent.get_item_count(slot) > 0):
      return True
    else:
      player.whisper('I don\'t have the block to place!')
      return False
  else:
    player.whisper('I don\'t have the right blocks to place!')
    return False

def placeColour(color: str, direction: enums.Direction):
  checkPosition = as_loc(2212, 45, -302)
  colorDict = {
    "white": 0,
    "orange": 1,
    "magenta": 2,
    "light_blue": 3
    "yellow": 4,
    "lime": 5,
    "pink": 6,
    "gray": 7,
    "light_gray": 8,
    "cyan": 9,
    "purple": 10,
    "blue": 11,
    "brown": 12,
    "green": 13,
    "red": 14,
    "black": 15,
  }

  slot = colorDict[color]
  if (slot is undefined):
    raise ValueError('Invalid color')

  if canPlaceReceiver(slot):
    agent.place(slot, direction)