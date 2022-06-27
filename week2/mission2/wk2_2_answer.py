for i in range(4):
    agent.move('left')
for i in range(3):
    agent.move('forward')
    pickCoolant('left')
for i in range(8):
    agent.move('right')
for i in range(3):
    pickCoolant('right')
    agent.move('back')
for i in range(2):
    agent.move('left')
for i in range(3):
    agent.move('forward')

agent.move('up')
placePackedCoolant("forward")
agent.move('up')
placeBlueCoolant("forward")
agent.move('up')
placePackedCoolant("forward")
agent.move('up')
placeBlueCoolant("forward")
agent.move('up')
placeBlueCoolant("forward")

