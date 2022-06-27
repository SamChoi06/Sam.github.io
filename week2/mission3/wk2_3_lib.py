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

def checkBlockFromAgent(block, direction: enums.Direction):
  checkLoc = agent.position.__add__(getCardinalDirection(direction))
  return world.is_block(checkLoc, block)

def pickReceiver(direction: enums.Direction):
  if checkBlockFromAgent('red_concrete', direction):
    agent.destroy(direction)
    
    count = 0
    if agent.get_item(1) == 'concrete':
      count = agent.get_item_count(1)
    
    agent.give(('concrete', 14, ""), count + 1, 1)

  if checkBlockFromAgent('blue_concrete', direction):
    agent.destroy(direction)
    
    count = 0
    if agent.get_item(2) == 'concrete':
      count = agent.get_item_count(2)
    
    agent.give(('concrete', 11, ""), count + 1, 2)

  if checkBlockFromAgent('green_concrete', direction):
    agent.destroy(direction)
    
    count = 0
    if agent.get_item(3) == 'concrete':
      count = agent.get_item_count(3)
    
    agent.give(('concrete', 13, ""), count + 1, 3)

  if checkBlockFromAgent('yellow_concrete', direction):
    agent.destroy(direction)
    
    count = 0
    if agent.get_item(4) == 'concrete':
      count = agent.get_item_count(4)
    
    agent.give(('concrete', 4, ""), count + 1, 4)

def canPlaceReceiver(slot: int):
  if (agent.get_item(slot) == 'concrete'):
    if (agent.get_item_count(slot) > 0):
      return True
    else:
      return False
  else:
    return False

def placeReceiver(color: str, direction: enums.Direction):
  if color == 'red':
    if canPlaceReceiver(1):
      agent.place(1, direction)
    else:
      player.whisper('I don\'t have red receiver to place!')
  elif color == 'blue':
    if canPlaceReceiver(2):
      agent.place(2, direction)
    else:
      player.whisper('I don\'t have blue receiver to place!')
  elif color == 'green':
    if canPlaceReceiver(3):
      agent.place(3, direction)
    else:
      player.whisper('I don\'t have green receiver to place!')
  elif color == 'yellow':
    if canPlaceReceiver(4):
      agent.place(4, direction)
    else:
      player.whisper('I don\'t have yellow receiver to place!')
  else:
    raise ValueError('Invalid color')
