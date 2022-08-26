import pygame    

pygame.init()# initializing the constructor
res = (600,600)# screen resolution
screen = pygame.display.set_mode(res)# opens up a window
color = (255,255,255)# white color
color_light = (170,170,170)# light shade of the button
color_dark = (100,100,100)# dark shade of the button
width = screen.get_width() # stores the width of the screen into a variable
height = screen.get_height()# stores the height of the screen into a variable
smallfont = pygame.font.SysFont('Corbel',35)  # defining a font
text = smallfont.render('quit' , True , color)# rendering a text written in this font

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the
            # button the game is terminated
            if 412 <= mouse[0] <= 412+150 and height/2-20 <= mouse[1] <= height/2-20+40:
                pygame.quit()
                  
    # fills the screen with a color
    screen.fill((60,25,60))
      
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()
      
    # if mouse is hovered on a button it
    # changes to lighter shade 
    if 412 <= mouse[0] <= 412+150 and height/2-20 <= mouse[1] <= height/2-20+40:
        pygame.draw.rect(screen,color_light,[412,height/2-20,150,40])
          
    else:
        pygame.draw.rect(screen,color_dark,[412,height/2-20,150,40])
        
    if 412-37-150 <= mouse[0] <= 412-37-150+150 and height/2-20 <= mouse[1] <= height/2-20+40:
        pygame.draw.rect(screen,color_light,[412-37-150,height/2-20,150,40])
          
    else:
        pygame.draw.rect(screen,color_dark,[412-37-150,height/2-20,150,40])
        
    if 412-37-150-37-150 <= mouse[0] <= 412-37-150-37-150+150 and height/2-20 <= mouse[1] <= height/2-20+40:
        pygame.draw.rect(screen,color_light,[412-37-150-37-150,height/2-20,150,40])
          
    else:
        pygame.draw.rect(screen,color_dark,[412-37-150-37-150,height/2-20,150,40])

      
    # superimposing the text onto our button
    screen.blit(text , (412+50,height/2-20))
    screen.blit(text,(412-37-150+50,height/2-20))
    screen.blit(text,(412-37-150-37-150+50,height/2-20))
      
    # updates the frames of the game
    pygame.display.update()