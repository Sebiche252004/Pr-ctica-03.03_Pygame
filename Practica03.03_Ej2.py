import pygame  

pygame.init()  

# Creamos la ventana
ventana = pygame.display.set_mode((720, 640))  
pygame.display.set_caption("HaxBall miami 5.0")  

ball = pygame.image.load("ball.png")

ballrect = ball.get_rect()

speedball = [0, 0]


ballrect.move_ip((ventana.get_width()-(ball.get_width()))/2, (ventana.get_height())/2)


jugando = True  
while jugando:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            jugando = False  

    ballrect = ballrect.move(speedball)


    
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speedball[0] = -speedball[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speedball[1] = -speedball[1]

    ventana.fill((150, 255, 255))  
    ventana.blit(ball, ballrect) 
    pygame.display.flip()  
    pygame.time.Clock().tick(60)  


pygame.quit()