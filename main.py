import pygame
import numpy as np
import cellular_automata as CA

pygame.init()

w, h = 1024,1024

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
tile_size = 4
map_size = (int(w/tile_size), int(h/tile_size))
map = CA.Simulation(map_size,6,.35,3)



running = True
while running:
    screen.fill((30,30,30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if pygame.K_SPACE == 1:
            map = CA.Simulation(map_size,6,.35,3)
    
    for x in range(map_size[0]):
        for y in range(map_size[1]):
            if map[x,y] == 1:
                pygame.draw.rect(screen,(230,230,230),(x*tile_size,y*tile_size,tile_size,tile_size),0)
    
    
    map = CA.Simulation(map_size,6,.35,3)
    clock.tick(60)
    
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
exit()
