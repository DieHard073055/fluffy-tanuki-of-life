#
# @file     screen.py
# @author   Eshan Shafeeq
# @version  v0.5
# @date     27 August 2015
# @brief    This file contains the functionality to print all the
#           pixels to the screen. Also prints the HUD at the bottom
#           to indicate the game status and other stuff.
#
#


from pygame.locals import *
import random
class screen():
    """docstring for screen"""
    def __init__(self, pygame):
        self.pygame = pygame

        self.MONITOR_SIZE_X = int(str(self.pygame.display.Info()).split(',')[-2:][0].strip()[-4:])
        self.MONITOR_SIZE_Y = int(str(self.pygame.display.Info()).split(',')[-2:][1].strip()[:-2][-4:])


        self.SIZE_X = int(str(self.pygame.display.Info()).split(',')[-2:][0].strip()[-4:])/2
        self.SIZE_Y = int(str(self.pygame.display.Info()).split(',')[-2:][1].strip()[:-2][-4:])/2

        self.PIXEL_SIZE = 20

        self.tick = 10
        self.clock = self.pygame.time.Clock()

        self._caption = "GAME OF LIFE"

        self.BOARD_X = self.SIZE_X / self.PIXEL_SIZE
        self.BOARD_Y = int((self.SIZE_Y - (self.SIZE_Y*0.2)) / self.PIXEL_SIZE)

        self._surface = self.pygame.display.set_mode((self.SIZE_X, self.SIZE_Y))
        self.pygame.display.set_caption(self._caption)

    def reload_screen(self, game_states):
        self.pygame.display.quit()
        self.pygame.display.init()
        if game_states['fullscreen']:
            self.SIZE_X = int(str(self.pygame.display.Info()).split(',')[-2:][0].strip()[-4:])
            self.SIZE_Y = int(str(self.pygame.display.Info()).split(',')[-2:][1].strip()[:-2][-4:])

        self.BOARD_X = self.SIZE_X / self.PIXEL_SIZE
        self.BOARD_Y = int((self.SIZE_Y - (self.SIZE_Y*0.2)) / self.PIXEL_SIZE)

        cursor = self.pygame.mouse.get_cursor()
        #tmp = self._surface.convert()

        if game_states['fullscreen']:
            self._surface = self.pygame.display.set_mode((self.SIZE_X, self.SIZE_Y), FULLSCREEN)
        else:
            self._surface = self.pygame.display.set_mode((self.SIZE_X, self.SIZE_Y))

        self._surface = self.pygame.display.get_surface()

        self.pygame.display.set_caption(self._caption)
        self.pygame.key.set_mods(0)
        self.pygame.mouse.set_cursor(*cursor)

    def get_colors( self, color_theme, y, x ):
        if color_theme == 0:
            return [ 0, 255, 0 ]
        if color_theme == 1:
            return [ 0, 255, 255 ]
        if color_theme == 2:
            return [ 255, 255, 0 ]
        if color_theme == 3:
            return [ random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) ]
        if color_theme == 4:
            return [ y % 255, x % 255, y * x % 255 ]

    def draw_game_board(self, grid, game_states):
        self._surface.fill(self.pygame.Color(0, 0, 0))
        for x in range((self.BOARD_X)-1):
            for y in range((self.BOARD_Y)-1):
                if grid[y][x]:
                    r, g, b = self.get_colors( game_states['color_theme'], y, x )
                    self.pygame.draw.rect(self._surface, self.pygame.Color(r, g, b), (x*self.PIXEL_SIZE , y*self.PIXEL_SIZE , self.PIXEL_SIZE , self.PIXEL_SIZE ))


    def draw_game_status_panel(self, status):
        _y_distance_increment = int(self.SIZE_Y * 0.02) + int(self.SIZE_Y * 0.02)/2
        _x_distance_increment = 0.3
        _x_distance = 20


        st_font = self.pygame.font.Font('freesansbold.ttf', int(self.SIZE_Y * 0.027))


        status_data = []
        status_data.append("Pixel Processing Rule : " + str(status['pixel_p_mode']))
        status_data.append("Process State : " + str(status['process_state']))
        status_data.append("Theme : " + str(status['color_theme']))
        status_data.append("Cursor Draw : " + str(status['draw_mouse']))
        status_data.append("Selected Creature : " + str(status['selected_creature']))
        status_data.append("Pixel Size : " + str(self.PIXEL_SIZE))
        status_data.append("Grid Size : " + str([self.BOARD_X, self.BOARD_Y]))
        status_data.append("Pixel x, y : " + str(status['mouse_pos']))
        status_data.append(str(status['status']))

        _y_distance = self.BOARD_Y * self.PIXEL_SIZE + _y_distance_increment/2

        for s in range(4):
            text_surface_obj = st_font.render(status_data[s], False, self.pygame.Color(120, 120, 120))
            text_obj = text_surface_obj.get_rect()
            text_obj.topleft=(_x_distance,  _y_distance)
            _y_distance = _y_distance + _y_distance_increment
            self._surface.blit(text_surface_obj, text_obj)

        _x_distance = _x_distance + (self.BOARD_X * self.PIXEL_SIZE) * _x_distance_increment
        _y_distance = self.BOARD_Y * self.PIXEL_SIZE + _y_distance_increment/2

        for s in range(4, 8):
            text_surface_obj = st_font.render(status_data[s], False, self.pygame.Color(120, 120, 120))
            text_obj = text_surface_obj.get_rect()
            text_obj.topleft=(_x_distance,  _y_distance)
            _y_distance = _y_distance + _y_distance_increment
            self._surface.blit(text_surface_obj, text_obj)


        st_font = self.pygame.font.Font('freesansbold.ttf', int(self.SIZE_Y * 0.04))
        _y_distance_increment = int(self.SIZE_Y * 0.04)

        _x_distance = _x_distance + (self.BOARD_X * self.PIXEL_SIZE) * _x_distance_increment
        _y_distance = (self.BOARD_Y * self.PIXEL_SIZE) + (self.SIZE_Y - (self.BOARD_Y * self.PIXEL_SIZE + _y_distance_increment * 2) ) / 2

        text_surface_obj = st_font.render(status_data[8], False, self.pygame.Color(220, 220, 0))
        text_obj = text_surface_obj.get_rect()
        text_obj.topleft=(_x_distance,  _y_distance)
        _y_distance = _y_distance + _y_distance_increment
        self._surface.blit(text_surface_obj, text_obj)

    def draw_search_path(self, s_algo, game_states):
        if game_states['search_algorithm'] >= 2:
            for seen in s_algo.unvisited:
                x, y = seen
                self.pygame.draw.rect(self._surface, self.pygame.Color(0,102,255), (x*self.PIXEL_SIZE , y*self.PIXEL_SIZE , self.PIXEL_SIZE , self.PIXEL_SIZE ))

            for walked in s_algo.visited:
                x, y = walked
                self.pygame.draw.rect(self._surface, self.pygame.Color(255,102,0), (x*self.PIXEL_SIZE , y*self.PIXEL_SIZE , self.PIXEL_SIZE , self.PIXEL_SIZE ))

        if not s_algo.start_pos == []:
            self.pygame.draw.rect(self._surface, self.pygame.Color(255,255,50), (s_algo.start_pos[0]*self.PIXEL_SIZE , s_algo.start_pos[1]*self.PIXEL_SIZE , self.PIXEL_SIZE , self.PIXEL_SIZE ))
        if not s_algo.goal_pos == []:
            self.pygame.draw.rect(self._surface, self.pygame.Color(100,255,250), (s_algo.goal_pos[0]*self.PIXEL_SIZE , s_algo.goal_pos[1]*self.PIXEL_SIZE , self.PIXEL_SIZE , self.PIXEL_SIZE ))

    def update_screen(self):
        self.pygame.display.update()
        self.clock.tick(self.tick)
