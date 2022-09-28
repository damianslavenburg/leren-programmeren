from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for i in range(2):
    robotArm.grab()
    robotArm.moveRight()
robotArm.drop()
for x in range(2):
    robotArm.moveLeft()
robotArm.grab()
for s in range(2): 
    robotArm.moveRight()
robotArm.drop()
for l in range(2):
    robotArm.moveLeft()
robotArm.grab()
for k in range(1):
    robotArm.moveRight()
robotArm.drop()
for p in range(2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

   








# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()