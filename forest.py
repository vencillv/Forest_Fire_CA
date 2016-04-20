import random

distanceOffset = .5

class forest:
    def __init__(self, *args):
        if len(args) == 2:
            self.numToLight = args[0]
            self.burnChance = args[1]
        else:
            self.numToLight = 30
            self.burnChance = .5
        self.startUp()

    def startUp(self):
        self.forest = []
        self.forestSize = 202
        #random.seed(2)
        for y in range(0,self.forestSize):
            self.forest.append([])
            toSetTo = 1
            if y == 0 or y == self.forestSize - 1:
                toSetTo = 0
            for x in range(0, self.forestSize):
                self.forest[y].append([])
                if x == 0 or x == self.forestSize - 1:
                    self.forest[y][x] = 0
                else:
                    self.forest[y][x] = toSetTo
        for i in range(0, self.numToLight):
            self.toLight = [random.randint(1,self.forestSize-1), random.randint(1,self.forestSize-1)]
            #print(toLight)
            self.forest[self.toLight[0]][self.toLight[1]] = 2


    def update(self):
        currentRow = list(self.forest[0])
        previousRow = 0

        for y in range(1,self.forestSize-1):
            previousRow = list(currentRow)
            currentRow = list(self.forest[y])
            for x in range(1,self.forestSize-1):
                if self.forest[y][x] == 2:
                    self.forest[y][x] = -1
                elif self.forest[y][x] == 1:
                    # Calculate the sum of trees next to current
                    sumClose = 0
                    sumFar = 0
                    for yPrime in range(y-1,y+2):
                        for xPrime in range(x-1,x+2):
                            # Row above
                            if yPrime == y-1:
                                if previousRow[xPrime] == 2:
                                    if xPrime != x:
                                        sumFar += 1
                                    else:
                                        sumClose += 1
                            # Same row
                            elif yPrime == y:
                                if currentRow[xPrime] == 2:
                                    sumClose += 1
                            # Row below
                            elif self.forest[yPrime][xPrime] == 2:
                                if xPrime == x:
                                    sumClose += 1
                                else:
                                    sumFar += 1
                    # Calculate if tree is burning
                    ran = random.random()
                    isBurn = (1-pow(1-self.burnChance, sumClose + distanceOffset * sumFar))
                    if ran <= isBurn:
                          self.forest[y][x] = 2



#OTHER OPTION
    ''' copyArray = []
            for y in range(0,self.forestSize):
                copyArray.append([])
                for x in range(0,self.forestSize):
                    copyArray[y].append(self.forest[y][x])

       # print(copyArray)

        for y in range(1,self.forestSize-1):
            for x in range(1, self.forestSize-1):
                if (copyArray[y][x] == 2):
                    self.forest[y][x] = -1
                elif (self.forest[y][x] == 1):
                    sumClose = 0
                    sumFar = 0
                    for yPrime in range (y-1, y+2):
                        for xPrime in range (x-1, x+2):
                           # print(xPrime)
                           # print(yPrime)
                           # print("")
                            if copyArray[yPrime][xPrime] == 2:
                                #if xPrime == x or yPrime == y:
                                if ((xPrime == x-1 and yPrime == y) or (xPrime == x and yPrime == y-1) or (xPrime == x and yPrime == y+1) or (xPrime == x + 1 and yPrime == y)):
                                    sumClose += 1
                                else:
                                    sumFar += 1'''