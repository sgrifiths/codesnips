import random

def random_walk(n):
    """return the coordinates after n random steps"""

# setting up initial coordinates
    X = 0
    Y = 0

    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])

        if step == 'N':
            Y = Y + 1
        elif step == 'E':
            X = X + 1
        elif step == 'S':
            Y = Y - 1
        else:
            X = X - 1
    return (X, Y)


for i in range(100):
    walk = random_walk(100000)
    print(walk)

