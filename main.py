import pygame, sys
from settings import *
from debug import debug

class Game:
    def __init__(self):
        
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill('black')
            debug('Hello World')
            pygame.display.update()
            self.clock.ticks(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()