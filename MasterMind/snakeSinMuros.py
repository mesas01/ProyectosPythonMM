import os
import random
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 11

myPosition = [6, 3]
tailLength = 0
tail = []
mapObjects = []

endGame = False
died = False

# main loop
while not endGame:
    os.system("cls")
    # Generate objects on the map
    while len(mapObjects) < NUM_OF_MAP_OBJECTS:
        newPosition = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

        if newPosition not in mapObjects and newPosition != myPosition:
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
                    print("has muerto!")
                    endGame = True
                    died = True

            print(" {} ".format(charToDraw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    print("Tamaño de la serpiente {}".format(len(tail)+1))

    # ask user where he wants to move
    # direction = input("donde te quieres mover WASD")
    direction = readchar.readchar()

    if direction == "w":
        tail.insert(0, myPosition.copy())
        tail = tail[:tailLength]
        myPosition[POS_Y] -= 1
        myPosition[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, myPosition.copy())
        tail = tail[:tailLength]
        myPosition[POS_Y] += 1
        myPosition[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, myPosition.copy())
        tail = tail[:tailLength]
        myPosition[POS_X] -= 1
        myPosition[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, myPosition.copy())
        tail = tail[:tailLength]
        myPosition[POS_X] += 1
        myPosition[POS_X] %= MAP_WIDTH
    elif direction == "q":
        endGame = True

    os.system("cls")

if died:
    print("HAS MUERTO....")
