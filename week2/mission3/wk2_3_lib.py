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
  if checkBlockFromAgent('redstone_block', direction):
    agent.destroy(direction)
    
    count = 0
    if agent.get_item(1) == 'redstone_block':
      count = agent.get_item_count(1)
    
    agent.give(('redstone_block'), count + 1, 1)

  if checkBlockFromAgent('lapis_block', direction):
    agent.destroy(direction)
    
    count = 0
    if agent.get_item(2) == 'lapis_block':
      count = agent.get_item_count(2)
    
    agent.give(('lapis_block'), count + 1, 2)

  if checkBlockFromAgent('emerald_block', direction):
    agent.destroy(direction)
    
    count = 0
    if agent.get_item(3) == 'emerald_block':
      count = agent.get_item_count(3)
    
    agent.give(('emerald_block', 13, ""), count + 1, 3)

  if checkBlockFromAgent('gold_block', direction):
    agent.destroy(direction)
    
    count = 0
    if agent.get_item(4) == 'gold_block':
      count = agent.get_item_count(4)
    
    agent.give('gold_block', count + 1, 4)

def placeReceiver(color: str, direction: enums.Direction):
  if color == 'redstone_block':
    if agent.get_item(1) == 'redstone_block':
      agent.place(1, direction)
    else:
      player.whisper('I don\'t have red receiver to place!')
  elif color == 'lapis_block':
    if agent.get_item(2) == 'lapis_block':
      agent.place(2, direction)
    else:
      player.whisper('I don\'t have blue receiver to place!')
  elif color == 'emerald_block':
    if agent.get_item(3) == 'emerald_block':
      agent.place(3, direction)
    else:
      player.whisper('I don\'t have green receiver to place!')
  elif color == 'gold_block':
    if agent.get_item(4) == 'gold_block':
      agent.place(4, direction)
    else:
      player.whisper('I don\'t have yellow receiver to place!')
  else:
    raise ValueError('Invalid color')
  
