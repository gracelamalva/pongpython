import sys, pygame
pygame.init()

# screen configurations
size = width, height = 500,500
screen = pygame.display.set_mode(size)
black = 0, 0, 0
red = 255, 0, 0

# init objects
paddle_speed = [0,5]
paddle_color = red
left_paddle_x = 50
l_left, l_top, l_width, l_height = left_paddle_x,0,20,60

left_paddle = pygame.draw.rect(screen, red, (l_left, l_top, l_width, l_height))

def draw_left_paddle():
    global l_top, l_bottom
    global paddle_speed
    left_paddle = pygame.draw.rect(screen, red, (l_left, l_top, l_width, l_height))
    
    if l_top < 0 or l_top+l_height > height:
        paddle_speed[1] = -paddle_speed[1]
    
    l_top += paddle_speed[1]
    
    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.time.delay(10)
    
    screen.fill(black)
    draw_left_paddle()
    pygame.display.flip()