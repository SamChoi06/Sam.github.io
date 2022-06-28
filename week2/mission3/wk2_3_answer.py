pickReceiver('back')
for i in range(4):
    agent.move('forward')
pickReceiver('forward')
for i in range(2):
    agent.move('back')
for i in range(2):
    agent.move('left')
pickReceiver('left')
for i in range(4):
    agent.move('right')
pickReceiver('right')

agent.move('back')
placeReceiver('gold_block', 'back')
for i in range(2):
    agent.move('forward')
placeReceiver('emerald_block', 'forward')
for i in range(4):
    agent.move('left')
placeReceiver('lapis_block', 'forward')
for i in range(2):
    agent.move('back')
placeReceiver('redstone_block', 'back')