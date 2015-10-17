import random
import numpy
import creatures

class grid_processor():
    """docstring for grid_processor"""
    def __init__(self, board_size):
        self.generate_grid(board_size)

    def generate_grid(self, board_size):
        self.grid = numpy.zeros(board_size)

    def reload_generate_grid(self, window, board_size):
        old_grid = self.grid
        self.grid = numpy.zeros(board_size)

        for x in range((window.BOARD_X)-1):
            for y in range((window.BOARD_Y)-1):
                if(x < old_grid.shape[1] and y < old_grid.shape[0]):
                    if(old_grid[y][x]):
                        self.grid[y][x] = 1

    def save_grid(self, window):
        from datetime import datetime
        import time
        filename = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S')

        s =""

        for x in range((window.BOARD_X)-1):
            for y in range((window.BOARD_Y)-1):
                if self.grid[y][x]:
                    s = s + "[" + str(x) + ", " + str(y) + "],"

        data_file = open(filename, "w")
        data_file.write(s)
        data_file.close

    def count_neighbours(self, gamemode, window, x, y):
        count = 0
        #check top
        if(y > 0 and gamemode != 4):
            if(self.grid[y-1][x]):
                count=count+1
        #check left
        if(x > 0 and gamemode != 4):
            if(self.grid[y][x-1]):
                count=count+1
        #check top left

        if(y > 0 and x > 0 and gamemode != 5):
                if(self.grid[y-1][x-1]):
                    count=count+1
        #check right
        if(x < window.BOARD_X and gamemode != 4):
                if(self.grid[y][x+1]):
                    count=count+1
        #check top right
        if(y > 0 and x < window.BOARD_X and gamemode != 5):
                if(self.grid[y-1][x+1]):
                    count=count+1
        #check down
        if(y < window.BOARD_Y and gamemode != 4):
                if(self.grid[y+1][x]):
                    count=count+1
        #check down right
        if(y < window.BOARD_Y and x < window.BOARD_X and gamemode != 5):
                if(self.grid[y+1][x+1]):
                    count=count+1
        #check down left
        if(y < window.BOARD_Y and x > 0 and gamemode != 5):
                if(self.grid[y+1][x-1]):
                    count=count+1

        return count
    def deploy_creature(self, window, game_states):
        l_creatures = creatures.creatures().get_creature(game_states['selected_creature'])
        for coordinates in l_creatures:
            if window.SIZE_X > (game_states['mouse_pos'][0]+coordinates[0]) and window.SIZE_Y > (game_states['mouse_pos'][1]+coordinates[1]):
                self.grid[game_states['mouse_pos'][1]+coordinates[1]][game_states['mouse_pos'][0]+coordinates[0]] = 1

    def process(self, window, game_states):
        pixel_p = game_states['pixel_p_mode']
        if pixel_p == 0:
            new_grid = numpy.zeros((window.BOARD_Y, window.BOARD_X))
            for y in range((window.BOARD_Y)-1):
                for x in range((window.BOARD_X)-1):
                    neighbours = self.count_neighbours(pixel_p, window, x, y)


                    #print "Count " + str(c)
                    if self.grid[y][x]:
                        #Check for lonliness
                        if neighbours < 2:
                            new_grid[y][x] = 0
                        #Check for over crowding
                        elif neighbours > 3:
                            new_grid[y][x] = 0
                        else:
                            new_grid[y][x] = 1
                    else:
                        #Spawn if there are near by pixels
                        if neighbours == 3:
                            new_grid[y][x] = 1
                        else:
                            new_grid[y][x] = 0

            self.grid = new_grid
        elif pixel_p == 1:
            for x in range((window.BOARD_X)-1):
                for y in range((window.BOARD_Y)-1):
                    neighbours = self.count_neighbours(pixel_p, window, x, y)

                    #print "Count " + str(c)
                    if self.grid[y][x]:
                        #Check for lonliness
                        if neighbours < 2:
                           self.grid[y][x] = 0
                        #Check for over crowding
                        if neighbours >= 3:
                           self.grid[y][x] = 0
                    else:
                        #Spawn if there are near by pixels
                        if neighbours ==3:
                           self.grid[y][x] = 1
        elif pixel_p == 2:
            new_grid = numpy.zeros((window.BOARD_Y, window.BOARD_X))
            for x in range((window.BOARD_X)-1):
                for y in range((window.BOARD_Y)-1):
                    neighbours = self.count_neighbours(pixel_p, window, x, y)

                    #print "Count " + str(c)
                    if self.grid[y][x]:
                        #Check for lonliness
                        if neighbours == 0:
                            new_grid[y][x] = 0
                        else:
                            new_grid[y][x] = 1
                        #Check for over crowding
                        if neighbours > 3:
                            new_grid[y][x] = 0
                        else:
                            new_grid[y][x] = 1
                    else:
                        #Spawn if there are near by pixels
                        if neighbours >= 3:
                            new_grid[y][x] = 1
                        else:
                            new_grid[y][x] = 0

            self.grid = new_grid
        elif pixel_p == 3:
         for x in range((window.BOARD_X)-1):
             for y in range((window.BOARD_Y)-1):
                 neighbours = self.count_neighbours(pixel_p, window, x, y)

                 #print "Count " + str(c)
                 if self.grid[y][x]:
                     #Check for lonliness
                     if neighbours == 0:
                        self.grid[y][x] = 0
                     #Check for over crowding
                     if neighbours > 3:
                        self.grid[y][x] = 0
                 else:
                     #Spawn if there are near by pixels
                     if neighbours == 2:
                        self.grid[y][x] = 1

        elif pixel_p == 4:
            for x in range((window.BOARD_X)-1):
                for y in range((window.BOARD_Y)-1):
                    neighbours = self.count_neighbours(pixel_p, window, x, y)

                    #print "Count " + str(c)
                    if self.grid[y][x]:
                        #Check for lonliness
                        if neighbours == 0:
                           self.grid[y][x] = 0
                        #Check for over crowding
                        if neighbours > 3:
                           self.grid[y][x] = 0
                    else:
                        #Spawn if there are near by pixels
                        if neighbours == 2:
                           self.grid[y][x] = 1

        elif pixel_p == 5:
            for x in range((window.BOARD_X)-1):
                for y in range((window.BOARD_Y)-1):
                    neighbours = self.count_neighbours(pixel_p, window, x, y)

                    #print "Count " + str(c)
                    if self.grid[y][x]:
                        #Check for lonliness
                        if neighbours == 0:
                           self.grid[y][x] = 0
                        #Check for over crowding
                        if neighbours > 3:
                           self.grid[y][x] = 0
                    else:
                        #Spawn if there are near by pixels
                        if neighbours == 2:
                           self.grid[y][x] = 1

        elif pixel_p == 6:
            new_grid = numpy.zeros((window.BOARD_Y, window.BOARD_X))
            for y in range((window.BOARD_Y)-1):
                for x in range((window.BOARD_X)-1):
                    neighbours = self.count_neighbours(pixel_p, window, x, y)

                    #print "Count " + str(c)
                    if self.grid[y][x]:
                        #Check for lonliness
                        if neighbours < 2:
                            new_grid[y][x] = 0
                        else:
                            new_grid[y][x] = 1
                        #Check for over crowding
                        if neighbours >= 3:
                            new_grid[y][x] = 0
                        else:
                            new_grid[y][x] = 1
                    else:
                        #Spawn if there are near by pixels
                        if neighbours == 3:
                            new_grid[y][x] = 1
                        else:
                            new_grid[y][x] = 0

            self.grid = new_grid
