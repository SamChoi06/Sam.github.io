from minecraft import enums

def pickCoolant(direction: enums.Direction):
  if (agent.inspect(direction) == 'blue_ice'):
    agent.destroy(direction)

    count_1 = 0
    if (agent.get_item(1) == 'blue ice'):
      count_1 = agent.get_item_count(1)
    pass
    
    agent.give('blue_ice', count_1 + 1, 1)
    pass
  
  if (agent.inspect(direction) == 'packed_ice'):
    agent.destroy(direction)

    count_2 = 0
    if (agent.get_item(2) == 'packed ice'):
      count_2 = agent.get_item_count(2)
    pass
    
    agent.give('packed_ice', count_2 + 1, 2)
    pass
  pass

def placeBlueCoolant(direction: enums.Direction):
  if (agent.get_item(1) == 'blue ice'):
    if (agent.get_item_count(1) > 0):
      agent.place(1, direction)
      pass
    else:
      player.whisper('I don\'t have blue coolant to place!')
    pass
  else:
    player.whisper('I don\'t have blue coolant to place!')
    pass

def placePackedCoolant(direction: enums.Direction):
  if (agent.get_item(2) == 'packed ice'):
    if (agent.get_item_count(2) > 0):
        agent.place(2, direction)
        pass
    else:
        player.whisper('I don\'t have packed coolant to place!')
    pass
  else:
    player.whisper('I don\'t have packed coolant to place!')
    pass
