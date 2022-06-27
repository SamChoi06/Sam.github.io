for i in range(3):
    agent.move('forward')
for i in range(4):
    agent.move('left')

pickSignal('left')
agent.move('right')
placeSignal('left')

agent.move('forward')
agent.move('left')
for i in range(4):
    agent.move('forward')

pickSignal('left')
agent.move('right')
placeSignal('left')

for i in range(7):
    agent.move('right')
pickSignal('right')
agent.move('left')
placeSignal('right')

agent.move('back')
agent.move('right')
for i in range(4):
    agent.move('back')
pickSignal('right')
agent.move('left')
placeSignal('right')