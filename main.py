import pygame, sys
from pygame.locals import *
import screen
import input_handler
import grid_processor
import search_algorithm



def main():

    pygame.init()
    window = screen.screen(pygame)
    input_h = input_handler.input_handler(pygame, sys)
    grid_p = grid_processor.grid_processor([window.SIZE_X, window.SIZE_Y] )
    s_algo = search_algorithm.search_algorithm()

    game_states={}

    game_states['pixel_p_mode'] = 0
    game_states['process_state'] = False
    game_states['color_theme'] = 0
    game_states['draw_mouse'] = False
    game_states['search_algorithm'] = 0
    game_states['selected_creature'] = 0
    game_states['mouse_pos'] = [0,0]
    game_states['status'] = ''
    game_states['fullscreen'] = False



    while(True):

        #Draw the grid panel
        window.draw_game_board(grid_p.grid)
        #Draw the status panel
        window.draw_game_status_panel(game_states)

        #Draw Search Algorithm
        window.draw_search_path(s_algo, game_states)
        #Run the PROCESSING
        if game_states['process_state']:
            grid_p.process(window, game_states)
        #Run the Searching
        if game_states['search_algorithm'] == 2:
            search_state = s_algo.step_search_dfs(grid_p.grid, window)
            if search_state:
                game_states['search_algorithm'] = 3
                game_states['status'] = 'Solution Found'


            elif search_state == False:
                game_states['search_algorithm'] = 3
                game_states['status'] = 'Solution not Found'

        #Handle User input events
        input_h.handle_event(grid_p, window, s_algo,game_states)

        window.update_screen()

if __name__ == '__main__':
    main()
