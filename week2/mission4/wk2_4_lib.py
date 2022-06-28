from minecraft import enums

def pickSignal(direction: enums.Direction):
  if (agent.inspect(direction) == 'end_rod'):
    agent.destroy(direction)

    count_1 = 0
    if (agent.get_item(1) == 'end_rod'):
      count_1 = agent.get_item_count(1)
    pass
    
    agent.give('end_rod', count_1 + 1, 1)
    pass

def placeSignal(direction: enums.Direction):
  count_1 = agent.get_item_count(1)
  count_2 = 0
  if (agent.get_item(1) == 'end rod'):
    if (agent.get_item_count(1) > 0):
      agent.place(1, direction)
      count_2 = count_1 -1
      agent.give('end_rod', count_2, 1)
      if (count_1 == 1):
        agent.give('air', 1, 1)
      pass
    else:
      player.whisper('I don\'t have signal transmitter to place!')
    pass
  else:
    player.whisper('I don\'t know how to place!')
    pass

