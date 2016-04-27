#
# @file     input_handler.py
# @author   Eshan Shafeeq
# @version  v0.5
# @date     27 August 2015
# @breif    This file contains all the functionality to handle key strokes
#           and mouse movement. It defines all the functionality for the
#           key presses and mouse movements.


from pygame.locals import *
import sys
class input_handler():
    """docstring for input_handler"""
    def __init__(self, pygame, sys):
        self.pygame = pygame
        self.sys = sys


    def handle_event(self, grid_p, window, s_algo, game_states):
        for event in self.pygame.event.get():
            """
            To Quit the Game
            """
            if event.type == QUIT:
                self.pygame.quit()
                self.sys.exit()

            if event.type == MOUSEMOTION:
                    m_x, m_y = event.pos
                    game_states['mouse_pos'] = event.pos
                    game_states['mouse_pos'] = [game_states['mouse_pos'][0]/window.PIXEL_SIZE , game_states['mouse_pos'][1]/window.PIXEL_SIZE ]
                    if game_states['draw_mouse']:
                        if(m_x < window.SIZE_X-window.PIXEL_SIZE  and m_y < (window.SIZE_Y- (window.SIZE_Y*0.2))-window.PIXEL_SIZE):
                            mx = m_x / window.PIXEL_SIZE
                            my = m_y / window.PIXEL_SIZE
                            if game_states['search_algorithm'] == 2:
                                if [mx, my] not in s_algo.visited and [mx, my] not in s_algo.unvisited and not [mx, my] == s_algo.start_pos and not [mx, my] == s_algo.goal_pos:
                                    grid_p.grid[my][mx] = 1
                            else:
                                grid_p.grid[my][mx] = 1


            if event.type == MOUSEBUTTONUP:
                m_x, m_y = event.pos
                if(m_x < window.SIZE_X-window.PIXEL_SIZE  and m_y < (window.SIZE_Y- int(window.SIZE_Y*0.2))-window.PIXEL_SIZE):
                    mx = m_x / window.PIXEL_SIZE
                    my = m_y / window.PIXEL_SIZE
                    if game_states['search_algorithm'] == 2:
                        if [mx, my] not in s_algo.visited and [mx, my] not in s_algo.unvisited and not [mx, my] == s_algo.start_pos and not [mx, my] == s_algo.goal_pos:
                            grid_p.grid[my][mx] = not grid_p.grid[my][mx]
                    else:
                        grid_p.grid[my][mx] = not grid_p.grid[my][mx]



            if event.type == KEYDOWN:
                if event.key == K_a:
                    grid_p.generate_grid([window.SIZE_X, window.SIZE_Y])

                elif event.key == K_x:
                    game_states['process_state'] = not game_states['process_state']
                    if game_states['process_state']:
                        game_states['status'] = 'Processing'
                    else:
                        game_states['status'] =''

                elif event.key == K_c:
                    game_states['draw_mouse'] = not game_states['draw_mouse']
                    if game_states['draw_mouse']:
                        game_states['status'] ='Mouse Draw on'
                    else:
                        game_states['status'] ='Mouse Draw off'
                elif event.key == K_z:
                    game_states['pixel_p_mode'] = game_states['pixel_p_mode'] + 1
                    game_states['status']= 'PPM Changed'
                    if game_states['pixel_p_mode'] == 7:
                        game_states['pixel_p_mode'] = 0

                elif event.key == K_s:
                    grid_p.save_grid(window)
                    game_states['status']= 'Grid Saved'

                elif event.key == K_EQUALS:
                    window.PIXEL_SIZE = window.PIXEL_SIZE + 1
                    grid_p.reload_generate_grid(window, [window.SIZE_X, window.SIZE_Y])
                    window.reload_screen(game_states)
                    game_states['status']= 'Pixel Size Changed'

                elif event.key == K_MINUS:
                    if window.PIXEL_SIZE > 1:
                        window.PIXEL_SIZE = window.PIXEL_SIZE - 1
                        grid_p.reload_generate_grid(window, [window.SIZE_X, window.SIZE_Y])
                        window.reload_screen(game_states)
                        game_states['status']= 'Pixel Size Changed'

                elif event.key == K_q:
                    sys.exit()

                elif event.key == K_d:
                    game_states['color_theme'] = game_states['color_theme'] + 1
                    if game_states['color_theme'] == 5:
                        game_states['color_theme'] = 0

                elif event.key == K_e:
                    #Deploy selected Monster
                    grid_p.deploy_creature(window, game_states)
                    game_states['status'] = 'Creature : ' + str(game_states['selected_creature']) + ' Deployed!'

                elif event.key == K_w:
                    #Swap selected Monster
                    game_states['selected_creature'] = game_states['selected_creature'] +1
                    game_states['status'] = 'Creature : ' + str(game_states['selected_creature']) + ' Ready!'
                    if game_states['selected_creature'] == 3:
                        game_states['selected_creature'] = 0

                elif event.key == K_F11:
                    #Full screen
                    game_states['fullscreen'] = not game_states['fullscreen']
                    grid_p.reload_generate_grid(window, [window.SIZE_X, window.SIZE_Y])
                    window.reload_screen(game_states)

                elif event.key == K_F10:
                    #Make screen x larger
                    if window.MONITOR_SIZE_X > (window.SIZE_X + 50) and not game_states['fullscreen']:
                        window.SIZE_X = window.SIZE_X+50
                        grid_p.reload_generate_grid(window, [window.SIZE_X, window.SIZE_Y])
                        window.reload_screen(game_states)
                        game_states['status']= 'Screen_X altered'

                elif event.key == K_F9:
                    #make screen x smaller
                    if 100 < (window.SIZE_X - 50) and not game_states['fullscreen']:
                        window.SIZE_X = window.SIZE_X-50
                        grid_p.reload_generate_grid(window, [window.SIZE_X, window.SIZE_Y])
                        window.reload_screen(game_states)
                        game_states['status']= 'Screen_X altered'

                elif event.key == K_F8:
                    #Make screen y larger
                    if window.MONITOR_SIZE_Y > (window.SIZE_Y + 50) and not game_states['fullscreen']:
                        window.SIZE_Y = window.SIZE_Y+50
                        grid_p.reload_generate_grid(window, [window.SIZE_X, window.SIZE_Y])
                        window.reload_screen(game_states)
                        game_states['status']= 'Screen_Y altered'

                elif event.key == K_F7:
                    #make screen y smaller
                    if 100 < (window.SIZE_Y - 50) and not game_states['fullscreen']:
                        window.SIZE_Y = window.SIZE_Y-50
                        grid_p.reload_generate_grid(window, [window.SIZE_X, window.SIZE_Y])
                        window.reload_screen(game_states)
                        game_states['status']= 'Screen_Y altered'

                elif event.key == K_f:
                    if game_states['search_algorithm']==0:
                        game_states['search_algorithm'] = 1
                        s_algo.start_pos = [game_states['mouse_pos'][0], game_states['mouse_pos'][1]]

                    elif game_states['search_algorithm'] == 1:
                        game_states['search_algorithm']=2
                        game_states['status']='Searching...'
                        s_algo.goal_pos = [game_states['mouse_pos'][0], game_states['mouse_pos'][1]]

                    elif game_states['search_algorithm'] == 2:
                        game_states['search_algorithm'] = 3
                        game_states['status']='Stopped'
                    elif game_states['search_algorithm']==3:
                        #Stop the search
                        game_states['search_algorithm'] = 0
                        game_states['status'] = ''
                        s_algo.start_pos = []
                        s_algo.goal_pos = []
                        s_algo.unvisited = []
                        s_algo.visited = []
