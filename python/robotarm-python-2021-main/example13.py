from shutil import move
from timeit import repeat
from RobotArm import RobotArm
robotArm = RobotArm('exercise 13')
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 5

# Jouw python instructies zet je vanaf hier:
drop = True
l = 1
while robotArm.grab() == True:
        for x in range(l): 
            robotArm.moveRight()
        robotArm.drop()
        for x in range(l): 
            robotArm.moveLeft()
        l = l + 1
        
else:
    quit


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()