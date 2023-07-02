import os
import random
import readchar

POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJECTS = 11

obstacleDefinition = """\
#######  ###   ####  ##     ####
###  ##  #   #  ##  ###  ##   ##
##   ##         ##  ####   #   # 
## ####  # ####  #   ##   ###  #
           ###    #    #  ###   
   ###  ###     ##   #     ##  #
  ####  ######  ###   ##    #  #
     #  #   ##   ####   ## ###  
##  ##  ##  ###   ####  ####   #
##  ###  ############    ####  #
#  ####      ####       ########
##  #    #######  ##    ###   ##
##  ###    ####   ###        ###
##  ##       #     #####   #####
######   ######   #####       ##\
"""

myPosition = [0, 5]
tailLength = 0
tail = []
mapObjects = []

endGame = False
died = False

# create obstacle map
obstacleDefinition = [list(row) for row in obstacleDefinition.split("\n")]

MAP_WIDTH = len(obstacleDefinition[0])
MAP_HEIGHT = len(obstacleDefinition)

# main loop
while not endGame:
    os.system("cls")
    # Generate objects on the map
    while len(mapObjects) < NUM_OF_MAP_OBJECTS:
        newPosition = [random.randint(0, MAP_WIDTH-1), random.randint(0, MAP_HEIGHT-1)]

        if newPosition not in mapObjects and newPosition != myPosition and \
                obstacleDefinition[newPosition[POS_Y]][newPosition[POS_X]] != "#":
            mapObjects.append(newPosition)

    # draw map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinateY in range(MAP_HEIGHT):
        print("|", end="")

        for coordinateX in range(MAP_WIDTH):

            charToDraw = " "
            objectInCell = None
            tailInCell = None

            for mapObject in mapObjects:
                if mapObject[POS_X] == coordinateX and mapObject[POS_Y] == coordinateY:
                    charToDraw = "*"
                    objectInCell = mapObject

            for tailPiece in tail:
                if tailPiece[POS_X] == coordinateX and tailPiece[POS_Y] == coordinateY:
                    charToDraw = "@"
                    tailInCell = tailPiece

            if myPosition[POS_X] == coordinateX and myPosition[POS_Y] == coordinateY:
                charToDraw = "@"

                if objectInCell:
                    mapObjects.remove(objectInCell)
                    tailLength += 1

                if tailInCell:
                    endGame = True
                    died = True

            if obstacleDefinition[coordinateY][coordinateX] == "#":
                charToDraw = "#"

            print(" {} ".format(charToDraw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("Tamaño de la serpiente {}".format(len(tail)+1))

    # ask user where he wants to move
    # direction = input("donde te quieres mover WASD")
    direction = readchar.readchar()

    if direction == "w":
        newPosition = [myPosition[POS_X], (myPosition[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s":
        newPosition = [myPosition[POS_X], (myPosition[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        newPosition = [(myPosition[POS_X] - 1) % MAP_WIDTH, myPosition[POS_Y]]

    elif direction == "d":
        newPosition = [(myPosition[POS_X] + 1) % MAP_WIDTH, myPosition[POS_Y]]

    elif direction == "q":
        endGame = True

    if newPosition:
        if obstacleDefinition[newPosition[POS_Y]][newPosition[POS_X]] != "#":
            tail.insert(0, myPosition.copy())
            tail = tail[:tailLength]
            myPosition = newPosition

    os.system("cls")

if died:
    print("HAS MUERTO....")
