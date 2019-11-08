import pygame 


pygame.init() #initiate pygame and every module that comes with pygame 
#game display
display_width = 1280
display_height = 720
gameDisplay = pygame.display.set_mode((display_width,display_height)) # put extra brackets so that it is a tuple and is only the parameter for our frame/window.
pygame.display.set_caption('Plane') #creates name for the frame
#pictures to be added 
plane= pygame.image.load("Images/plane3.png")
#plane= pygame.transform.scale(plane,(display_width-500,display_height-200))
FPS= 30
clock = pygame.time.Clock() 

#def airplane(x,y):
gameDisplay.blit(plane,(x,y))
def game_loop():
    x=0
    y=0
    x_change = 0 
    y_change = 0
    #gameloop
    dead = False
    """main game loop"""
    while not dead:   
        
        """Moving an object (Plane)"""
        for event in pygame.event.get():#gets all the event that happens what key user is pressing and your mouse 
            if event.type == pygame.QUIT:
                dead = True 
            if event.type == pygame.KEYDOWN: #Pressing DOwn ON a key 
                if event.key == pygame.K_a:
                    x_change = -10
                if event.key == pygame.K_d:
                    x_change = 10
                if event.key == pygame.K_s:  # Not sure why y axis is inverted 
                    y_change = 10
                if event.key == pygame.K_w:
                    y_change = -10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a  or pygame.K_d:
                    x_change = 0 
                if event.key == pygame.K_w  or pygame.K_s:
                    y_change = 0 
                    
        x += x_change
        y += y_change
        print(x)
        print(y)
        gameDisplay.fill((255,255,255)) # dont understand why this is nessasry 
        airplane(x,y)
        
        """creating boundaries for when the plane reaches the edge it dies"""
        #if x > display_width-plane_width or x < 0:  #the plane width is the image witdth but not coded on here yet 
           # dead = True
            
        
        
        pygame.display.update() # or you can use flip just updates the whole entire surface
        clock.tick(FPS)
game_loop()
pygame.quit()     
#quit()


    