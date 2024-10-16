import random
from capitals import states

print("Now playing: U.S. State Capitals Game Prototype")

correct = []
incorrect = []

random.shuffle(states)

for state in states:
    print(f"What is the capital of {state['name']}? press q to quit : )")
    print(state)
    userAnswer = input()
    print(userAnswer)
    if userAnswer.lower() == state['capital'].lower():
        correct.append(state)
        print("Great job you got it right!")
    elif userAnswer == 'q':
        break
    else:
        incorrect.append(state)
        print("Uh-oh lets try this one again later!")
