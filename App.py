# App to run the actual program

import pygame
import math
import forest

class App:
    def __init__(self):
        self.numToLight = input("Enter the number of trees to start on fire!")
        self.numToLight = max(0, min(int(self.numToLight), 40000))
        self.burnChance = input("Enter a % chance for trees to burn! (Between 0% and 100%)")
        self.burnChance = max(0, min(float(self.burnChance), 100)) / 100
        self.forest = forest.forest(self.numToLight, self.burnChance)
        self.window = pygame.display.set_mode((1000,830))
        self.done = False

        # Background and images
        self.bg = pygame.image.load("GUI.png")
        self.buttonImage = pygame.image.load("button.png")
        self.buttonMDImage = pygame.image.load("buttonDown.png")
        self.buttonMOImage = pygame.image.load("buttonMouseOver.png")
        self.plateImage = pygame.image.load("plate.png")
        self.gridImage = pygame.image.load("grid.png")
        self.gridImage.set_colorkey((255,255,255))

        # Button attributes
        self.button1pos = (832, 472)
        self.button2pos = (832, 539)
        self.button3pos = (832, 605)
        self.buttonHeight = 51
        self.buttonWidth = 152

        # Font attributes
        self.genNumberPos = (848, 190)
        self.timePassedPos = (848, 285)
        self.stepPos = (870, 550)
        self.resetPos = (865, 618)
        self.pausedPos = (860, 485)
        self.playPos = (873, 485)

        # Grid attributes
        self.gridStart = (17, 16)
        self.gridSize = (800, 800)
        self.cellWidth = self.gridSize[0] / (self.forest.forestSize - 2)
        self.cellHeight = self.gridSize[1] / (self.forest.forestSize - 2)
        self.colors = [(100, 100, 100), (255, 255, 255), (0, 200, 0), (200, 0, 0)]

        # Extras variables
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.genNumber = 0
        self.timePassed = 0
        self.paused = True
        self.flag = False
        self.takestep = False
        self.timestep = 1000
        self.timeSinceLastUpdate = 0

        # Font initialization
        self.font = pygame.font.Font(None, 44)
        backFont = pygame.font.Font(None, 45)
        self.genNumberFont = self.font.render(str(self.genNumber), True, self.white)
        self.timePassedFont = self.font.render(str(self.timePassed), True, self.white)
        self.pauseButtonFont = self.font.render("Pause", True, self.white)
        self.playButtonFont = self.font.render("Play", True, self.white)
        self.stepButtonFont = self.font.render("Step", True, self.white)
        self.resetButtonFont = self.font.render("Reset", True, self.white)
        self.pauseButtonFont2 = backFont.render("Pause", True, self.black)
        self.playButtonFont2 = backFont.render("Play", True, self.black)
        self.stepButtonFont2 = backFont.render("Step", True, self.black)
        self.resetButtonFont2 = backFont.render("Reset", True, self.black)

        self.drawGraph()

    def forestReset(self):
        self.forest = forest.forest(self.numToLight, self.burnChance)
        self.genNumber = 0
        self.timePassed = 0
        self.paused = True
        self.drawGraph()

    def drawGraph(self):
        # Draw cells
        for y in range(1, len(self.forest.forest) - 1):
            for x in range(1, len(self.forest.forest[y]) - 1):
                pygame.draw.rect(self.window, self.colors[self.forest.forest[y][x] + 1], (self.gridStart[0] + self.cellWidth * (x-1), self.gridStart[1] + self.cellHeight * (y-1), self.cellWidth, self.cellHeight))
        # Draw grid
        self.window.blit(self.gridImage, self.gridStart)

    def update(self,dT):
        evtList = pygame.event.get()
        for evt in evtList:
            if evt.type == pygame.QUIT:
                self.done = True
            elif evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_ESCAPE:
                    self.done = True
                else:
                    key_pressed.append(evt.key)
            elif evt.type == pygame.KEYUP:
                key_pressed.remove(evt.key)

        # Tell the forest to update
        if not self.paused:
            self.timePassed += dT / 1000
            self.timePassed = round(self.timePassed, 2)
            self.timeSinceLastUpdate += dT
            if self.timeSinceLastUpdate > self.timestep:
                self.genNumber += 1
                self.timeSinceLastUpdate -= self.timestep
                self.forest.update()
                self.drawGraph()
        elif self.takestep == True:
            self.takestep = False
            self.genNumber += 1
            self.timePassed += 1
            self.forest.update()
            self.drawGraph()

        # Blit Images
        self.window.blit(self.bg, (0,0))
        self.window.blit(self.plateImage, (834, 179))
        self.window.blit(self.plateImage, (833, 273))
        self.window.blit(self.buttonImage, self.button1pos)
        self.window.blit(self.buttonImage, self.button2pos)
        self.window.blit(self.buttonImage, self.button3pos)

        # Button checks
        try:
            mx = evt.pos[0]
            my = evt.pos[1]

            if evt.type == pygame.MOUSEBUTTONUP:
                self.flag = False

            # Play Button
            if mx > self.button1pos[0] and mx < self.button1pos[0] + self.buttonWidth:
                if my > self.button1pos[1] and my < self.button1pos[1] + self.buttonHeight:
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        self.window.blit(self.buttonMDImage, self.button1pos)
                        if self.paused == False and self.flag == False:
                            self.paused = True
                            self.flag = True
                        elif self.paused == True and self.flag == False:
                            self.paused = False
                            self.flag = True
                    else:
                        self.window.blit(self.buttonMOImage, self.button1pos)
            else:
                self.window.blit(self.buttonImage, self.button1pos)

            # Step Button
            if mx > self.button2pos[0] and mx < self.button2pos[0] + self.buttonWidth:
                if my > self.button2pos[1] and my < self.button2pos[1] + self.buttonHeight:
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        self.window.blit(self.buttonMDImage, self.button2pos)
                        self.takestep = True
                    else:
                        self.window.blit(self.buttonMOImage, self.button2pos)
            else:
                self.window.blit(self.buttonImage, self.button2pos)

            # Reset Button
            if mx > self.button3pos[0] and mx < self.button3pos[0] + self.buttonWidth:
                if my > self.button3pos[1] and my < self.button3pos[1] + self.buttonHeight:
                    if evt.type == pygame.MOUSEBUTTONDOWN:
                        self.window.blit(self.buttonMDImage, self.button3pos)
                        self.forestReset()
                    else:
                        self.window.blit(self.buttonMOImage, self.button3pos)
            else:
                window.blit(self.buttonImage, self.button3pos)

        except:
            pass

        # Font Blits
        self.genNumberFont = self.font.render(str(self.genNumber), True, self.white)
        self.timePassedFont = self.font.render(str(self.timePassed), True, self.white)

        self.window.blit(self.genNumberFont, self.genNumberPos)
        self.window.blit(self.timePassedFont, self.timePassedPos)
        self.window.blit(self.stepButtonFont2, (self.stepPos[0] - 2, self.stepPos[1] - 2))
        self.window.blit(self.stepButtonFont, self.stepPos)
        self.window.blit(self.resetButtonFont2, (self.resetPos[0] - 2, self.resetPos[1] - 2))
        self.window.blit(self.resetButtonFont, self.resetPos)

        if self.paused == False:
            self.window.blit(self.pauseButtonFont2, (self.pausedPos[0] - 2, self.pausedPos[1] - 2))
            self.window.blit(self.pauseButtonFont, self.pausedPos)
        else:
            self.window.blit(self.playButtonFont2, (self.playPos[0] - 2, self.playPos[1] - 2))
            self.window.blit(self.playButtonFont, self.playPos)

        # Flip Display
        pygame.display.flip()

# Create an instance of App and run the program
pygame.init()
app = App()
clock = pygame.time.Clock()
while not app.done:
    app.update(clock.tick())
pygame.quit()