#
# @file     search_algorithm.py
# @author   Eshan Shafeeq
# @version  v0.5
# @date     27 August 2015
# @brief    This file contains the depth first search algorithm to
#           do a DFS after generating a random maze from the maze
#           generation algorithm.


class search_algorithm():
    """docstring for search_algorithm"""
    def __init__(self):
        self.start_pos = []
        self.goal_pos = []
        self.visited = []
        self.unvisited = []

    def step_search_dfs(self, grid, window):
        if self.unvisited == [] and self.visited == []:
            self.unvisited.append(self.start_pos)

        #self.unvisited = a_star(self.unvisited, sgoal)
        x, y = self.unvisited.pop()

        #Top
        if(y > 0):
            if(not grid[y-1][x] and [x, (y-1)] not in self.visited):
                self.unvisited.append([x, y-1])
        #check left
        if(x > 0 ):
            if(not grid[y][x-1] and [(x-1), y] not in self.visited):
                self.unvisited.append([x-1, y])
        #check right
        if(x < window.BOARD_X-1):
            if(not grid[y][x+1] and [x+1, y] not in self.visited):
                self.unvisited.append([x+1, y])
        #check down
        if(y < window.BOARD_Y-1 ):
            if(not grid[y+1][x] and [x, (y+1)] not in self.visited):
                self.unvisited.append([x, y+1])

        self.visited.append([x, y])

        if self.goal_pos == [x, y]:
            return True

        if self.unvisited == []:
            return False
