# San Francisco Jugable

import pygame  

pygame.init()  

ventana = pygame.display.set_mode((720, 640))  
pygame.display.set_caption("HaxBall San Francisco 7.1.1 Preium Edition")  

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speedball = [5, 5] 

ballrect.move_ip((ventana.get_width()-(ball.get_width()))/2, (ventana.get_height())/2)

player1 = pygame.image.load("player1.png") 
player1rect = player1.get_rect() 
player1rect.move_ip(300, 450) 

player2 = pygame.image.load("player2.png") 
player2rect = player2.get_rect() 
player2rect.move_ip(380, 400) 



jugando = True  
while jugando:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        player1rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        player1rect.move_ip(0,-5)
    if keys[pygame.K_DOWN]:
        player1rect.move_ip(0,5)

    if keys[pygame.K_a]:
        player2rect.move_ip(-5, 0)
    if keys[pygame.K_d]:
        player2rect.move_ip(5, 0)
    if keys[pygame.K_w]:
        player2rect.move_ip(0,-5)
    if keys[pygame.K_s]:
        player2rect.move_ip(0,5)

    if ballrect.colliderect(player1rect):
        speedball[0] = -speedball[0] 
        speedball[1] = -speedball[1] 

    if ballrect.colliderect(player2rect):
        speedball[0] = -speedball[0] 
        speedball[1] = -speedball[1] 

    ballrect = ballrect.move(speedball)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speedball[0] = -speedball[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speedball[1] = -speedball[1]

    ventana.fill((150, 255, 255)) 
    ventana.blit(ball, ballrect) 
    ventana.blit(player1, player1rect) 
    ventana.blit(player2, player2rect) 
    pygame.display.flip() 
    pygame.time.Clock().tick(60) 
pygame.quit() 