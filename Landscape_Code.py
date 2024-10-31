import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
    # Tree Trunk
Tree_Trunk_x = 130
Tree_Trunk_y = 380
Tree_Trunk_Width = 15
Tree_Trunk_Height = 60
    # Tree Leaves
Tree_Leaves_1_point1_x = 105
Tree_Leaves_1_point1_y = 400
Tree_Leaves_1_point2_x = 170
Tree_Leaves_1_point2_y = 400
Tree_Leaves_1_point3_x = 137.5
Tree_Leaves_1_point3_y = 330
    # Clouds
Cloud_x = 100
Cloud_y = 100
Cloud_2_x = 500
Cloud_2_y = 150
    # Fishes
Fish_Speed = -5
        # Fish 1
Fish_x = 300
Fish_y = 300
jump1 = False
        # Fish 2
Fish_2_x = 320
Fish_2_y = 417
jump2 = False
        # Fish 3
Fish_3_x = 290
Fish_3_y = 450
jump3 = False
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            fish_choice = random.randrange(0,3)
            if fish_choice == 0:
                jump1 = True
                Fish_Speed *= -1
            elif fish_choice == 1:
                jump2 = True
                Fish_Speed *= -1
            elif fish_choice == 2:
                jump3 = True
                Fish_Speed *= -1       
    # GAME STATE UPDATES
    # All game math and comparisons happen here
        # Fish Jump 1
    if jump1 == True:
        Fish_y -= Fish_Speed
    if Fish_y <= 240:
        Fish_Speed *= -1
    if Fish_y >= 300:
        jump1 = False
        # Fish Jump 2
    if jump2 == True:
        Fish_2_y -= Fish_Speed
    if Fish_2_y <= 357:
        Fish_Speed *= -1
    if Fish_2_y >= 417:
        jump2 = False
        # Fish Jump 3
    if jump3 == True:
        Fish_3_y -= Fish_Speed
    if Fish_3_y <= 390:
        Fish_Speed *= -1
    if Fish_3_y >= 450:
        jump3 = False
        # Clouds
    if Cloud_x >= WIDTH + 25:
        Cloud_x = -75
    Cloud_x += 0.5
    if Cloud_2_x >= WIDTH + 25:
        Cloud_2_x = -75
    Cloud_2_x += 0.5

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    pygame.draw.rect(screen, (250,214,165), (0,0,640,480)) #Sky
    pygame.draw.rect(screen, (65,107,223), (0,280,640,200)) # River
    pygame.draw.polygon(screen, (19,109,21), [(0,HEIGHT), (0, 280), (280, 280), (200, HEIGHT)], width=0) #Grass 1
    pygame.draw.polygon(screen, (19,109,21), [(WIDTH,HEIGHT), (WIDTH, 280), (WIDTH-280, 280), (WIDTH-200, HEIGHT)], width=0) #Grass 2
    # Fence
    pygame.draw.rect(screen, (92,64,51), (0,260,280,5))
    pygame.draw.rect(screen, (92,64,51), (360,260,280,5))
    for i in range(5,WIDTH,20):
        if i >= 280 and i <= 360:
            continue
        else:
            pygame.draw.rect(screen, (92,64,51), (i,250,10,30))
    # Trees
    pygame.draw.rect(screen, (113,54,0), (Tree_Trunk_x,Tree_Trunk_y,Tree_Trunk_Width,Tree_Trunk_Height)) #Tree Trunk
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x,Tree_Leaves_1_point1_y), (Tree_Leaves_1_point2_x,Tree_Leaves_1_point2_y), (Tree_Leaves_1_point3_x,Tree_Leaves_1_point3_y)], width=0) #Tree Leaves 1
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x,Tree_Leaves_1_point1_y-30), (Tree_Leaves_1_point2_x,Tree_Leaves_1_point2_y-30), (Tree_Leaves_1_point3_x,Tree_Leaves_1_point3_y)], width=0) #Tree Leaves 2
    pygame.draw.rect(screen, (113,54,0), (Tree_Trunk_x+365,Tree_Trunk_y-10,Tree_Trunk_Width,Tree_Trunk_Height)) #Tree Trunk
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x+365,Tree_Leaves_1_point1_y-10), (Tree_Leaves_1_point2_x+365,Tree_Leaves_1_point2_y-10), (Tree_Leaves_1_point3_x+365,Tree_Leaves_1_point3_y-10)], width=0) #Tree Leaves 1
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x+365,Tree_Leaves_1_point1_y-40), (Tree_Leaves_1_point2_x+365,Tree_Leaves_1_point2_y-40), (Tree_Leaves_1_point3_x+365,Tree_Leaves_1_point3_y-10)], width=0) #Tree Leaves 2
    pygame.draw.rect(screen, (113,54,0), (Tree_Trunk_x-100,Tree_Trunk_y-100,Tree_Trunk_Width,Tree_Trunk_Height)) #Tree Trunk
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x-100,Tree_Leaves_1_point1_y-100), (Tree_Leaves_1_point2_x-100,Tree_Leaves_1_point2_y-100), (Tree_Leaves_1_point3_x-100,Tree_Leaves_1_point3_y-100)], width=0) #Tree Leaves 1
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x-100,Tree_Leaves_1_point1_y-130), (Tree_Leaves_1_point2_x-100,Tree_Leaves_1_point2_y-130), (Tree_Leaves_1_point3_x-100,Tree_Leaves_1_point3_y-100)], width=0) #Tree Leaves 2
    pygame.draw.rect(screen, (113,54,0), (Tree_Trunk_x+450,Tree_Trunk_y-80,Tree_Trunk_Width,Tree_Trunk_Height)) #Tree Trunk
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x+450,Tree_Leaves_1_point1_y-80), (Tree_Leaves_1_point2_x+450,Tree_Leaves_1_point2_y-80), (Tree_Leaves_1_point3_x+450,Tree_Leaves_1_point3_y-80)], width=0) #Tree Leaves 1
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x+450,Tree_Leaves_1_point1_y-110), (Tree_Leaves_1_point2_x+450,Tree_Leaves_1_point2_y-110), (Tree_Leaves_1_point3_x+450,Tree_Leaves_1_point3_y-80)], width=0) #Tree Leaves 2
    pygame.draw.rect(screen, (113,54,0), (Tree_Trunk_x+295,Tree_Trunk_y-95,Tree_Trunk_Width,Tree_Trunk_Height)) #Tree Trunk
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x+295,Tree_Leaves_1_point1_y-95), (Tree_Leaves_1_point2_x+295,Tree_Leaves_1_point2_y-95), (Tree_Leaves_1_point3_x+295,Tree_Leaves_1_point3_y-95)], width=0) #Tree Leaves 1
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x+295,Tree_Leaves_1_point1_y-125), (Tree_Leaves_1_point2_x+295,Tree_Leaves_1_point2_y-125), (Tree_Leaves_1_point3_x+295,Tree_Leaves_1_point3_y-95)], width=0) #Tree Leaves 2
    pygame.draw.rect(screen, (113,54,0), (Tree_Trunk_x+56,Tree_Trunk_y-87,Tree_Trunk_Width,Tree_Trunk_Height)) #Tree Trunk
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x+56,Tree_Leaves_1_point1_y-87), (Tree_Leaves_1_point2_x+56,Tree_Leaves_1_point2_y-87), (Tree_Leaves_1_point3_x+56,Tree_Leaves_1_point3_y-87)], width=0) #Tree Leaves 1
    pygame.draw.polygon(screen, (1,50,32), [(Tree_Leaves_1_point1_x+56,Tree_Leaves_1_point1_y-117), (Tree_Leaves_1_point2_x+56,Tree_Leaves_1_point2_y-117), (Tree_Leaves_1_point3_x+56,Tree_Leaves_1_point3_y-87)], width=0) #Tree Leaves 2
    # Clouds
        # Cloud 1
    pygame.draw.circle(screen, (255,255,255), (Cloud_x,Cloud_y), 25) #Bottom Left Circle
    pygame.draw.circle(screen, (255,255,255), (Cloud_x+25,Cloud_y), 25) #Middle Bottom
    pygame.draw.circle(screen, (255,255,255), (Cloud_x+50,Cloud_y), 25) #Right Bottom
    pygame.draw.circle(screen, (255,255,255), (Cloud_x+12.5,Cloud_y-20), 25) #Left Top
    pygame.draw.circle(screen, (255,255,255), (Cloud_x+37.5,Cloud_y-20), 25) #Right Top
        # Cloud 2
    pygame.draw.circle(screen, (255,255,255), (Cloud_2_x,Cloud_2_y), 25) #Bottom Left Circle
    pygame.draw.circle(screen, (255,255,255), (Cloud_2_x+25,Cloud_2_y), 25) #Middle Bottom
    pygame.draw.circle(screen, (255,255,255), (Cloud_2_x+50,Cloud_2_y), 25) #Right Bottom
    pygame.draw.circle(screen, (255,255,255), (Cloud_2_x+12.5,Cloud_2_y-20), 25) #Left Top
    pygame.draw.circle(screen, (255,255,255), (Cloud_2_x+37.5,Cloud_2_y-20), 25) #Right Top
        # Fishes
    pygame.draw.ellipse(screen, (0,0,139), (Fish_x,Fish_y,10,15)) #Fish 1 Body
    pygame.draw.polygon(screen, (0,0,139), [(Fish_x,Fish_y+17), (Fish_x+5,Fish_y+12), (Fish_x+10,Fish_y+17)]) #Fish 1 Tail
    pygame.draw.rect(screen, (65,107,223), (290,300,30,30)) #Fish 1 Cover
    pygame.draw.ellipse(screen, (0,0,139), (Fish_2_x,Fish_2_y,10,15)) #Fish 2 Body
    pygame.draw.polygon(screen, (0,0,139), [(Fish_2_x,Fish_2_y+17), (Fish_2_x+5,Fish_2_y+12), (Fish_2_x+10,Fish_2_y+17)]) #Fish 2 Tail
    pygame.draw.rect(screen, (65,107,223), (310,400,30,60)) #Fish 2 Cover
    pygame.draw.ellipse(screen, (0,0,139), (Fish_3_x,Fish_3_y,10,15)) #Fish 3 Body
    pygame.draw.polygon(screen, (0,0,139), [(Fish_3_x,Fish_3_y+17), (Fish_3_x+5,Fish_3_y+12), (Fish_3_x+10,Fish_3_y+17)]) #Fish 3 Tail
    pygame.draw.rect(screen, (65,107,223), (272,445,30,30)) #Fish 3 Cover
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()
