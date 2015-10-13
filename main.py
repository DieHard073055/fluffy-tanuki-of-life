import pygame, sys
from pygame.locals import *
import random
import numpy

SIZE_X = 1080
SIZE_Y = 720
def setup():
    global windowSurfaceObject
    global fpsClock
    #Setup Pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    #Setup window
    windowSurfaceObject = pygame.display.set_mode((SIZE_X, SIZE_Y+200))
    pygame.display.set_caption('Game Of Life')

    #Setup Colors
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    black = pygame.Color(0, 0, 0)

    #Setup game array

    grid = generate_grid()

    return grid

def generate_grid():
    #Random initial state 1
    grid = numpy.zeros((SIZE_Y/10, SIZE_X/10))

    # for x in range(108-1):
    #    for y in range(72-1):
    #        if random.randint(0, 1) == random.randint(0, 1):
    #            grid[y][x]=1


    # for i in range(1):
    #     xx = random.randint(0, 90)
    #     yy = random.randint(0, 60)
    #
    #     for x in range(xx, xx+6):
    #        for y in range(yy, yy+6):
    #            if random.randint(0, 1) == random.randint(0, 1):
    #                grid[y][x]=1


    # for t in range(1000):
    #     grid[random.randint(0, 71)][random.randint(0, 107)] = 1
    return grid

def count_surrounding(grid, x, y):
    count = 0
    #check top
    if(y > 0):
        if(grid[y-1][x]):
            count=count+1
    #check left
    if(x > 0):
        if(grid[y][x-1]):
            count=count+1
    #check top left
    if(y > 0 and x > 0):
            if(grid[y-1][x-1]):
                count=count+1
    #check right
    if(x < SIZE_X/10):
            if(grid[y][x+1]):
                count=count+1
    #check top right
    if(y > 0 and x < SIZE_X/10):
            if(grid[y-1][x+1]):
                count=count+1
    #check down
    if(y < SIZE_Y/10):
            if(grid[y+1][x]):
                count=count+1
    #check down right
    if(y < SIZE_Y/10 and x < SIZE_X/10):
            if(grid[y+1][x+1]):
                count=count+1
    #check down left
    if(y < SIZE_Y/10 and x > 0):
            if(grid[y+1][x-1]):
                count=count+1

    return count



def run_process(grid):
    global gamemode
    if gamemode == 0:
        for x in range((SIZE_X/10)-1):
            for y in range((SIZE_Y/10)-1):
                c = count_surrounding(grid, x, y)

                #print "Count " + str(c)
                if grid[y][x]:
                    #Check for lonliness
                    if c == 0:
                        grid[y][x] = 0
                    #Check for over crowding
                    if c > 3:
                        grid[y][x] = 0
                else:
                    #Spawn if there are near by pixels
                    if c == 3:
                        grid[y][x] = 1
    elif gamemode == 1:
        for x in range((SIZE_X/10)-1):
            for y in range((SIZE_Y/10)-1):
                c = count_surrounding(grid, x, y)

                #print "Count " + str(c)
                if grid[y][x]:
                    #Check for lonliness
                    if c == 0 or c==1:
                        grid[y][x] = 0
                    #Check for over crowding
                    if c > 3:
                        grid[y][x] = 0
                else:
                    #Spawn if there are near by pixels
                    if c == 3:
                        grid[y][x] = 1
    elif gamemode == 2:
        new_grid = numpy.zeros((SIZE_Y/10, SIZE_X/10))
        for x in range((SIZE_X/10)-1):
            for y in range((SIZE_Y/10)-1):
                c = count_surrounding(grid, x, y)

                #print "Count " + str(c)
                if grid[y][x]:
                    #Check for lonliness
                    if c == 0:
                        new_grid[y][x] = 0
                    else:
                        new_grid[y][x] = 1
                    #Check for over crowding
                    if c > 3:
                        new_grid[y][x] = 0
                    else:
                        new_grid[y][x] = 1
                else:
                    #Spawn if there are near by pixels
                    if c >= 3:
                        new_grid[y][x] = 1
                    else:
                        new_grid[y][x] = 0

        grid = new_grid
    elif gamemode == 3:
        for x in range((SIZE_X/10)-1):
            for y in range((SIZE_Y/10)-1):
                c = count_surrounding(grid, x, y)

                #print "Count " + str(c)
                if grid[y][x]:
                    #Check for lonliness
                    if c == 0:
                        grid[y][x] = 0
                    #Check for over crowding
                    if c >= 3:
                        grid[y][x] = 0
                else:
                    #Spawn if there are near by pixels
                    if c >= 3:
                        grid[y][x] = 1

    return grid

def get_color(colortheme, x, y):
    colors = []
    if colortheme == 0:
        colors.append(((y*x)*x) % 255)
        colors.append(((x*y)*y) % 255)
        colors.append((colors[0] * colors[1]) % 255)
    elif colortheme == 1:
        colors.append(random.randint(0,255))
        colors.append(random.randint(0,255))
        colors.append(random.randint(0,255))
    elif colortheme == 2:
        colors.append(0)
        colors.append(255)
        colors.append(0)
    elif colortheme == 3:
        c = random.randint(0,255)
        colors.append(133 % 255)
        colors.append((3*300) % 255 )
        colors.append(c)
    return colors


def loop(grid):
    global windowSurfaceObject
    global fpsClock
    global gamemode
    global colortheme
    colortheme = 0
    gamemode = 0
    process = 0
    draw_mouse = 0
    #Game loop
    while True:
        #Fill the background
        windowSurfaceObject.fill(pygame.Color(0, 0, 0))

        #Draw the pixels
        for x in range((SIZE_X/10)-1):
            for y in range((SIZE_Y/10)-1):
                if grid[y][x]:
                    r, g, b = get_color(colortheme, x, y)
                    pygame.draw.rect(windowSurfaceObject, pygame.Color(r, g, b), (x*10, y*10, 10, 10))

        #Write out the game data
        #720 to 920
        st_font = pygame.font.Font('freesansbold.ttf', 15)
        status = []
        status.append("Mouse Draw : " + str(draw_mouse))
        status.append("Execute Mode : " + str(process))
        status.append("Game Mode : " + str(gamemode))
        status.append("Colour Theme : " + str(colortheme))

        start_y = 40
        start_x = 10
        for s in status:
            text_surface_obj = st_font.render(s, False, pygame.Color(120, 120, 120))
            text_obj = text_surface_obj.get_rect()
            text_obj.topleft=(start_x, (720 + start_y))
            start_y = start_y + 20
            windowSurfaceObject.blit(text_surface_obj, text_obj)

        #Process the grid with the rules
        if process:
            grid = run_process(grid)



        #Handle any input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if draw_mouse:
                    m_x, m_y = event.pos
                    if(m_x < 1080 and m_y < 720):
                        mx = m_x / 10
                        my = m_y / 10
                        grid[my][mx] = 1
            elif event.type == MOUSEBUTTONUP:
                m_x, m_y = event.pos
                if(m_x < 1080 and m_y < 720):
                    mx = m_x / 10
                    my = m_y / 10
                    grid[my][mx] = not grid[my][mx]
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    grid = generate_grid()
                if event.key == K_x:
                    process = not process
                if event.key == K_c:
                    draw_mouse = not draw_mouse
                if event.key == K_z:
                    gamemode = gamemode + 1
                    if gamemode == 4:
                        gamemode = 0
                if event.key == K_d:
                    colortheme = colortheme + 1
                    if colortheme == 4:
                        colortheme = 0

        #Update the game display and set Frames per second
        pygame.display.update()
        fpsClock.tick(60)

if __name__ == '__main__':
    grid = setup()
    loop(grid)
