import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    dp = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Hello world!')

    #Colores
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    
    dp.fill(WHITE)

    pygame.draw.rect(dp, BLUE, (100, 100, 20, 20))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__=='__main__':
    main()
