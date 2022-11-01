from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
k = 1
for x in range(5):
    for i in range(k):
        robotArm.moveRight()
    robotArm.grab()
    k = k + 1
    for j in range(1):
        robotArm.moveLeft()
    robotArm.drop()
        
  



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()