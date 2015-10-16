import pygame, sys, os
from pygame.locals import *
import random
import numpy

SIZE_X = 0
SIZE_Y = 0

BOARD_X = 0
BOARD_Y = 0
def setup():
    global windowSurfaceObject
    global fpsClock

    global SIZE_X
    global SIZE_Y

    global BOARD_Y
    global BOARD_X

    #Setup Pygame
    pygame.init()
    #get screen size
    try:
        SIZE_X = int(str(pygame.display.Info()).split(',')[-2:][0].strip()[-4:])
        SIZE_Y = int(str(pygame.display.Info()).split(',')[-2:][1].strip()[:-2][-4:])
    except Exception as e:
        screen = os.popen("xrandr -q -d :0").readlines()[0]
        SIZE_X = int(screen.split(',')[1].split()[1])
        SIZE_Y = int(screen.split(',')[1].split()[3])

    SIZE_X = 1080
    SIZE_Y = 900
    BOARD_X = SIZE_X / 5
    BOARD_Y = (SIZE_Y - (SIZE_Y/8)) / 5


    fpsClock = pygame.time.Clock()
    #Setup window
    windowSurfaceObject = pygame.display.set_mode((SIZE_X, SIZE_Y))
    pygame.display.set_caption('Game Of Life')


    windowSurfaceObject = pygame.display.get_surface()
    tmp = windowSurfaceObject.convert()

    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()
    SIZE_X, SIZE_Y = windowSurfaceObject.get_width(), windowSurfaceObject.get_height()
    flags = windowSurfaceObject.get_flags()
    bits = windowSurfaceObject.get_bitsize()

    # pygame.display.quit()
    # pygame.display.init()
    #
    # windowSurfaceObject = pygame.display.set_mode((SIZE_X, SIZE_Y), flags^FULLSCREEN, bits)
    # windowSurfaceObject.blit(tmp,(0,0))
    # pygame.display.set_caption(*caption)
    #
    # pygame.key.set_mods(0)
    #
    # pygame.mouse.set_cursor(*cursor)
    #Setup game array

    grid = generate_grid()

    return grid

def generate_grid():
    #Random initial state 1
    grid = numpy.zeros((BOARD_Y, BOARD_X))
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
def deploy_creature(grid, mouse):
    l_creatures = [[1,5],[2,5],[1,6],[2,6],[11,5],[11,6],[11,7],[12,4],[12,8],[13,3],[13,9],[14,3],[14,9],[15,6],[16,4],[16,8],[17,5],[17,7],[17,6],[18,6],[21,3],[21,4],[21,5],[22,3],[22,4],[22,5],[23,2],[23,6],[25,2],[25,6],[25,7],[25,1],[35,3],[35,4],[36,3],[36,4]]
    for coordinates in l_creatures:
        if SIZE_X > (mouse[0]+coordinates[0]) and SIZE_Y > (mouse[1]+coordinates[1]):
            grid[mouse[1]+coordinates[1]][mouse[0]+coordinates[0]] = 1

    return grid

def count_surrounding(gamemode, grid, x, y):
    count = 0
    #check top
    if(y > 0 and gamemode != 4):
        if(grid[y-1][x]):
            count=count+1
    #check left
    if(x > 0 and gamemode != 4):
        if(grid[y][x-1]):
            count=count+1
    #check top left

    if(y > 0 and x > 0 and gamemode != 5):
            if(grid[y-1][x-1]):
                count=count+1
    #check right
    if(x < BOARD_X and gamemode != 4):
            if(grid[y][x+1]):
                count=count+1
    #check top right
    if(y > 0 and x < BOARD_X and gamemode != 5):
            if(grid[y-1][x+1]):
                count=count+1
    #check down
    if(y < BOARD_Y and gamemode != 4):
            if(grid[y+1][x]):
                count=count+1
    #check down right
    if(y < BOARD_Y and x < BOARD_X and gamemode != 5):
            if(grid[y+1][x+1]):
                count=count+1
    #check down left
    if(y < BOARD_Y and x > 0 and gamemode != 5):
            if(grid[y+1][x-1]):
                count=count+1

    return count



def run_process(grid):
    global gamemode
    if gamemode == 0:
        for x in range((BOARD_X)-1):
            for y in range((BOARD_Y)-1):
                c = count_surrounding(gamemode, grid, x, y)

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
                    if c == 2:
                        grid[y][x] = 1
    elif gamemode == 1:
        for x in range((BOARD_X)-1):
            for y in range((BOARD_Y)-1):
                c = count_surrounding(gamemode, grid, x, y)

                #print "Count " + str(c)
                if grid[y][x]:
                    #Check for lonliness
                    if c < 2:
                        grid[y][x] = 0
                    #Check for over crowding
                    if c >= 3:
                        grid[y][x] = 0
                else:
                    #Spawn if there are near by pixels
                    if c ==3:
                        grid[y][x] = 1
    elif gamemode == 2:
        new_grid = numpy.zeros((BOARD_Y, BOARD_X))
        for x in range((BOARD_X)-1):
            for y in range((BOARD_Y)-1):
                c = count_surrounding(gamemode, grid, x, y)

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
        new_grid = numpy.zeros((BOARD_Y, BOARD_X))
        for y in range((BOARD_Y)-1):
            for x in range((BOARD_X)-1):
                c = count_surrounding(gamemode, grid, x, y)

                #print "Count " + str(c)
                if grid[y][x]:
                    #Check for lonliness
                    if c < 2:
                        new_grid[y][x] = 0
                    #Check for over crowding
                    elif c > 3:
                        new_grid[y][x] = 0
                    else:
                        new_grid[y][x] = 1
                else:
                    #Spawn if there are near by pixels
                    if c == 3:
                        new_grid[y][x] = 1
                    else:
                        new_grid[y][x] = 0

        grid = new_grid
    elif gamemode == 4:
        for x in range((BOARD_X)-1):
            for y in range((BOARD_Y)-1):
                c = count_surrounding(gamemode, grid, x, y)

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
                    if c == 2:
                        grid[y][x] = 1

    elif gamemode == 5:
        for x in range((BOARD_X)-1):
            for y in range((BOARD_Y)-1):
                c = count_surrounding(gamemode, grid, x, y)

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
                    if c == 2:
                        grid[y][x] = 1

    elif gamemode == 6:
        new_grid = numpy.zeros((BOARD_Y, BOARD_X))
        for y in range((BOARD_Y)-1):
            for x in range((BOARD_X)-1):
                c = count_surrounding(gamemode, grid, x, y)

                #print "Count " + str(c)
                if grid[y][x]:
                    #Check for lonliness
                    if c < 2:
                        new_grid[y][x] = 0
                    else:
                        new_grid[y][x] = 1
                    #Check for over crowding
                    if c >= 3:
                        new_grid[y][x] = 0
                    else:
                        new_grid[y][x] = 1
                else:
                    #Spawn if there are near by pixels
                    if c == 3:
                        new_grid[y][x] = 1
                    else:
                        new_grid[y][x] = 0

        grid = new_grid

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

def save_grid(grid):
    from datetime import datetime
    import time
    filename = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    s = "[" + str(BOARD_X) + ", " + str(BOARD_Y) + "]\n"

    for x in range((BOARD_X)-1):
        for y in range((BOARD_Y)-1):
            if grid[y][x]:
                s = s + "(" + str(x) + ", " + str(y) + ")\n"

    data_file = open(filename, "w")
    data_file.write(s)
    data_file.close

def search_algorithm(grid, sstart, sgoal, s_visited, s_unvisited):
    if s_unvisited == [] and s_visited == []:
        s_unvisited.append(sstart)

    #s_unvisited = a_star(s_unvisited, sgoal)
    x, y = s_unvisited.pop()

    #Top
    if(y > 0):
        if(not grid[y-1][x] and [x, (y-1)] not in s_visited):
            s_unvisited.append([x, y-1])
    #check left
    if(x > 0 ):
        if(not grid[y][x-1] and [(x-1), y] not in s_visited):
            s_unvisited.append([x-1, y])
    #check right
    if(x < BOARD_X-1):
        if(not grid[y][x+1] and [x+1, y] not in s_visited):
            s_unvisited.append([x+1, y])
    #check down
    if(y < BOARD_Y-1 ):
        if(not grid[y+1][x] and [x, (y+1)] not in s_visited):
            s_unvisited.append([x, y+1])

    s_visited.append([x, y])

    if sgoal == [x, y]:
        return True

    if s_unvisited == []:
        return False



def loop(grid):
    global windowSurfaceObject
    global fpsClock
    global gamemode
    global colortheme

    mouse_pos=[]

    colortheme = 0
    gamemode = 0
    process = 0
    draw_mouse = 0

    searching = 0
    sstart = []
    sgoal = []
    s_visited = []
    s_unvisited = []

    found = 0

    selected_creature = 0

    #Game loop
    while True:
        #Fill the background
        windowSurfaceObject.fill(pygame.Color(0, 0, 0))

        #Draw the pixels

        #pixls = pygame.PixelArray(windowSurfaceObject)
        for x in range((BOARD_X)-1):
            for y in range((BOARD_Y)-1):
                if grid[y][x]:
                    r, g, b = get_color(colortheme, x, y)
                    pygame.draw.rect(windowSurfaceObject, pygame.Color(r, g, b), (x*5, y*5, 5, 5))
                    #pixls[x][y] = pygame.Color(r, g, b)

        if searching > 1:
            #put the coordinates for the AI

            for seen in s_unvisited:
                x, y = seen
                pygame.draw.rect(windowSurfaceObject, pygame.Color(0,102,255), (x*5, y*5, 5, 5))

            for walked in s_visited:
                x, y = walked
                pygame.draw.rect(windowSurfaceObject, pygame.Color(255,102,0), (x*5, y*5, 5, 5))

        if not sstart == []:
            pygame.draw.rect(windowSurfaceObject, pygame.Color(255,255,50), (sstart[0]*5, sstart[1]*5, 5, 5))
        if not sgoal == []:
            pygame.draw.rect(windowSurfaceObject, pygame.Color(100,255,250), (sgoal[0]*5, sgoal[1]*5, 5, 5))
        #del pixls
        #Write out the game data
        #720 to 920
        st_font = pygame.font.Font('freesansbold.ttf', 15)
        status = []
        status.append("Mouse Draw : " + str(draw_mouse))
        status.append("Execute Mode : " + str(process))
        status.append("Game Mode : " + str(gamemode))
        status.append("Colour Theme : " + str(colortheme))

        start_y = 20
        start_x = 10
        for s in status:
            text_surface_obj = st_font.render(s, False, pygame.Color(120, 120, 120))
            text_obj = text_surface_obj.get_rect()
            text_obj.topleft=(start_x, ((BOARD_Y * 5) + start_y))
            start_y = start_y + 20
            windowSurfaceObject.blit(text_surface_obj, text_obj)

        if found == True:
            text_surface_obj = st_font.render("Solution Found", False, pygame.Color(0, 153, 0))
            text_obj = text_surface_obj.get_rect()
            text_obj.topleft=(600, ((BOARD_Y * 5) + start_y))
            windowSurfaceObject.blit(text_surface_obj, text_obj)

        if searching == 2:
            text_surface_obj = st_font.render("Searching..", False, pygame.Color(102, 0, 102))
            text_obj = text_surface_obj.get_rect()
            text_obj.topleft=(600, ((BOARD_Y * 5) + start_y))
            windowSurfaceObject.blit(text_surface_obj, text_obj)


        #Process the grid with the rules
        if process:
            grid = run_process(grid)

        if searching == 2 and not sstart == []:
            alg = search_algorithm(grid, sstart, sgoal, s_visited, s_unvisited)
            if alg == False:
                searching = 3
                sstart = []
                sgoal = []
            elif alg == True:
                searching = 3
                found = True


        #Handle any input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                m_x, m_y = event.pos
                mouse_pos = event.pos
                mouse_pos = [mouse_pos[0]/5, mouse_pos[1]/5]
                if draw_mouse and searching==0:
                    if(m_x < SIZE_X-5 and m_y < SIZE_Y- (SIZE_Y/8)):
                        mx = m_x / 5
                        my = m_y / 5
                        grid[my][mx] = 1
            elif event.type == MOUSEBUTTONUP:
                m_x, m_y = event.pos
                if searching==1:
                    #get mouse coordinates
                    sgoal = mouse_pos
                    searching = 2
                elif(m_x < SIZE_X-5 and m_y < SIZE_Y- (SIZE_Y/8)):
                    mx = m_x / 5
                    my = m_y / 5
                    grid[my][mx] = not grid[my][mx]
            elif event.type == KEYDOWN:
                if event.key == K_a and searching==0:
                    grid = generate_grid()
                if event.key == K_x and searching==0:
                    process = not process
                if event.key == K_c and searching==0:
                    draw_mouse = not draw_mouse
                if event.key == K_z and searching==0:
                    gamemode = gamemode + 1
                    if gamemode == 7:
                        gamemode = 0
                if event.key == K_s and searching==0:
                    save_grid(grid)
                if event.key == K_q:
                    sys.exit()
                if event.key == K_d:
                    colortheme = colortheme + 1
                    if colortheme == 4:
                        colortheme = 0
                if event.key == K_e:
                    #Deploy selected Monster
                    deploy_creature(grid, mouse_pos)
                if event.key == K_w:
                    #Swap selected Monster
                    pass
                if event.key == K_f:
                    if searching==0:
                        searching = 1
                        sstart = [mouse_pos[0], mouse_pos[1]]
                    if searching == 2:
                        searching = 3
                    elif searching==3:
                        #Stop the search
                        searching = 0
                        sstart = []
                        sgoal = []
                        s_unvisited = []
                        s_visited = []
                        found = 0


        #Update the game display and set Frames per second
        pygame.display.update()
        #fpsClock.tick(60)

if __name__ == '__main__':
    grid = setup()
    loop(grid)
