import pygame

pygame.init()
font = pygame.font.Font(None, 20)

def debig(info, y=10, x=10):
    display_surf = pygame.display.get_surface()
    debug_surf = pygame.render(str(info), True, 'white')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surf, 'black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)