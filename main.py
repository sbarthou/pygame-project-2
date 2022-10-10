import pygame
from sys import exit


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space-Miner')
bg = pygame.image.load('assets/background/Starfields/Starfield_02-1024x1024.png')
bg = pygame.transform.scale(bg, (size))
clock = pygame.time.Clock()


planet0_surf = pygame.image.load('assets/planets/planet_0.png').convert_alpha()
planet0_surf = pygame.transform.scale(planet0_surf, (100, 100))
planet0_rect = planet0_surf.get_rect(bottomright = (600, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(bg, (0, 0))
    
    screen.blit(planet0_surf, planet0_rect)
            
    pygame.display.update()
    clock.tick(60)