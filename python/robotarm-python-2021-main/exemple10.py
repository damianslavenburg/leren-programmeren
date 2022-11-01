from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
l = 9
for i in range(5):
    for j in range(5):
        robotArm.grab()
        for x in range(l):
            robotArm.moveRight()
        l = l - 1
        robotArm.drop()
        for k in range(l):
            robotArm.moveLeft()
        l = l - 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()