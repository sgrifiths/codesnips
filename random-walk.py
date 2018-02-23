import random

def random_walk(n):
    """return the coordinates after n random steps"""

# setting up initial coordinates
    X, Y = 0, 0

    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        X += dx
        Y += dy
    return (X, Y)


number_of_walks = 10000

for walk_length in range(1, 31):
    no_transport = 0
    for i in range(number_of_walks):
        (X, Y) = random_walk(walk_length)
        distance = abs(X) + abs(Y)
        if distance <= 4:
            no_transport += 1
            # end if
    # end for
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk Size=", walk_length, " / % No Transport = ", 100 * no_transport_percentage)
