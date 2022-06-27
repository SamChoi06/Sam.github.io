from minecraft.location import as_loc
from minecraft import enums

def pickFuel(direction: enums.Direction):
  if (agent.inspect(direction) == 'magma'):
    agent.destroy(direction)

    count_1 = 0
    if (agent.get_item(1) == 'magma'):
      count_1 = agent.get_item_count(1)
    pass
    
    agent.give('magma', count_1 + 1, 1)
    pass
  pass

def placeFuel(direction: enums.Direction):
  checkPosition = as_loc(2212, 45, -302)

  if (canPlaceBlock(checkPosition, direction)):
      if (agent.get_item_count(1) > 0 and agent.get_item(1) == 'magma'):
          agent.place(1, direction)
      else:
          player.whisper('I don\'t have fuel to place!')
  else:
      player.whisper('I can\'t place fuel at this position!')

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