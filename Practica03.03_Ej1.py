# Pygame

import pygame  

pygame.init()  

ventana = pygame.display.set_mode((780, 700))  
pygame.display.set_caption("HaxBall San Francisco 5.1.99")  

jugando = True  
while jugando:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            jugando = False  

    ventana.fill((150, 255, 255))  
    pygame.display.flip()  
    pygame.time.Clock().tick(60)  

pygame.quit()