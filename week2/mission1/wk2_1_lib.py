from minecraft.location import as_loc

def pickUpFuel():
  agent.collect("bucket")
  pass

def placeFuel():
  check = [as_loc(1081, 45, -230), as_loc(1086, 45, -230), as_loc(1091, 45, -230)]
  canPlace = False

  for c in check:
      if (agent.position == c):
          canPlace = True
          break

  if (canPlace == True):
    count_1 = agent.get_item_count(1)
    count_2 = 0
    if (agent.get_item_count(1) > 0 and agent.get_item(1) == 'bucket'):
          agent.give('lava_bucket', 1, 2)
          agent.place(2, 'down')
          count_2 = count_1 - 1
          agent.give('bucket',count_2,1)
          if (count_1 == 1):
            agent.give('air', 1, 1)
    else:
        player.whisper('I don\'t have fuel bucket to place fuel!')
  else:
      player.whisper('I can\'t place fuel at this position!')


