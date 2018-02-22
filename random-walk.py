import random

def random_walk(n):
    """return the coordinates after n random steps"""

# setting up initial coordinates
 X=0
 Y=0

 for i in range(n:
     step=random.choice({'N','S','E','W'})

     if step == 'N':
        Y= Y+1
     elif step == 'E':
        x=x+1
     elif step == 'S':
        y=y-1
     else:
        x=x-1
 return(x,y)


for i in range(25):
    walk = random_walk(100)
    print(walk)

