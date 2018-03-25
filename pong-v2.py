
#GL
import pygame

pygame.init() #start pygame

white = (255,255,255)  #set color vals
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


gameDisplay = pygame.display.set_mode ((800,600))  #windowsize
pygame.display.set_caption("Pong")         #window title

gameExit = False			#game is on

lead_x = 300			#INITIAL POSITION SAMPLE WILL DEFF CHANGE
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()	#frames per second init



while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:	#left and right direction event handling
                lead_x_change =-10
            if event.key ==pygame.K_RIGHT:
                lead_x_change = 10

    lead_x+= lead_x_change		#movement

    gameDisplay.fill(white)		#background color
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, 10,10])#object color and size

    pygame.display.update()		#update screen

    clock.tick(20)	#frames per second 



pygame.quit()		# quit py 
quit()

