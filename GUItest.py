#-------------------------------------------------------------------------------
# Name:        AI Lab 1
#
#-------------------------------------------------------------------------------

import pygame

pygame.init()

window = pygame.display.set_mode((1000,830))

# Background and images
bg = pygame.image.load("GUI.png")
buttonImage = pygame.image.load("button.png")
buttonMDImage = pygame.image.load("buttonDown.png")
buttonMOImage = pygame.image.load("buttonMouseOver.png")
plateImage = pygame.image.load("plate.png")
textboxImage = pygame.image.load("textbox.png")

# Button attributes
button1pos = (832, 472)
button2pos = (832, 539)
button3pos = (832, 605)
buttonHeight = 51
buttonWidth = 152

# Font attributes
genNumberPos = (848, 190)
timePassedPos = (848, 285)
stepPos = (870, 550)
resetPos = (865, 618)
pausedPos = (855, 485)
playPos = (873, 485)

# Variables
white = (255,255,255)
black = (0,0,0)
genNumber = 0
timePassed = 0
paused = True
flag = False

done = False

key_pressed = []

while not done:
    evtList = pygame.event.get()
    for evt in evtList:
        if evt.type == pygame.QUIT:
            done = True
        elif evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_ESCAPE:
                done = True
            else:
                key_pressed.append(evt.key)
        elif evt.type == pygame.KEYUP:
            key_pressed.remove(evt.key)

    # Clear window
    window.fill((255,255,255))

    # Blit Images
    window.blit(bg, (0,0))
    window.blit(plateImage, (834, 179))
    window.blit(plateImage, (833, 273))
    window.blit(textboxImage, (833, 364))
    window.blit(buttonImage, button1pos)
    window.blit(buttonImage, button2pos)
    window.blit(buttonImage, button3pos)

    # Fonts
    font = pygame.font.Font(None, 44)
    backFont = pygame.font.Font(None, 45)
    genNumberFont = font.render(str(genNumber), True, white)
    timePassedFont = font.render(str(timePassed), True, white)
    pauseButtonFont = font.render("Paused", True, white)
    playButtonFont = font.render("Play", True, white)
    stepButtonFont = font.render("Step", True, white)
    resetButtonFont = font.render("Reset", True, white)
    pauseButtonFont2 = backFont.render("Paused", True, black)
    playButtonFont2 = backFont.render("Play", True, black)
    stepButtonFont2 = backFont.render("Step", True, black)
    resetButtonFont2 = backFont.render("Reset", True, black)

    # Button checks
    try:
        mx = evt.pos[0]
        my = evt.pos[1]

        if evt.type == pygame.MOUSEBUTTONUP:
            flag = False

        # Play Button
        if mx > button1pos[0] and mx < button1pos[0] + buttonWidth:
            if my > button1pos[1] and my < button1pos[1] + buttonHeight:
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    window.blit(buttonMDImage, button1pos)
                    if paused == False and flag == False:
                        paused = True
                        flag = True
                    elif paused == True and flag == False:
                        paused = False
                        flag = True
                else:
                    window.blit(buttonMOImage, button1pos)
        else:
            window.blit(buttonImage, button1pos)

        # Step Button
        if mx > button2pos[0] and mx < button2pos[0] + buttonWidth:
            if my > button2pos[1] and my < button2pos[1] + buttonHeight:
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    window.blit(buttonMDImage, button2pos)
                else:
                    window.blit(buttonMOImage, button2pos)
        else:
            window.blit(buttonImage, button2pos)

        # Reset Button
        if mx > button3pos[0] and mx < button3pos[0] + buttonWidth:
            if my > button3pos[1] and my < button3pos[1] + buttonHeight:
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    window.blit(buttonMDImage, button3pos)
                else:
                    window.blit(buttonMOImage, button3pos)
        else:
            window.blit(buttonImage, button3pos)

    except:
        pass

    # Font Blits
    window.blit(genNumberFont, genNumberPos)
    window.blit(timePassedFont, timePassedPos)
    window.blit(stepButtonFont2, (stepPos[0] - 2, stepPos[1] - 2))
    window.blit(stepButtonFont, stepPos)
    window.blit(resetButtonFont2, (resetPos[0] - 2, resetPos[1] - 2))
    window.blit(resetButtonFont, resetPos)

    if paused == False:
        window.blit(pauseButtonFont2, (pausedPos[0] - 2, pausedPos[1] - 2))
        window.blit(pauseButtonFont, pausedPos)
    else:
        window.blit(playButtonFont2, (playPos[0] - 2, playPos[1] - 2))
        window.blit(playButtonFont, playPos)

    # Flip Display
    pygame.display.flip()

# Close program
pygame.quit()