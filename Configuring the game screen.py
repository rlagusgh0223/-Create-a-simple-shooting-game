import pygame

BLACK = (0,0,0)
pad_width = 480
pad_height =640

def runGame():
    global gamepad, clock

    doneFlag = False
    while not doneFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True

        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')
    clock = pygame.time.Clock()

initGame()
runGame()
