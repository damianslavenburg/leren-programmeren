from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
l = 10
v = 9
repeat = True
# Jouw python instructies zet je vanaf hier:
while v > 0:
    repeat = True
    robotArm.grab()
    if robotArm.scan() == "red":
        for x in range(l):
            robotArm.moveRight()
        robotArm.drop()
        v = v - 1
        for j in range(v):
            robotArm.moveLeft()
        l = l - 1
    else: 
        robotArm.drop()
        robotArm.moveRight()
        l = l - 1
        v = v - 1
else:
    repeat = False
        

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()