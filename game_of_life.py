import random
import os
import time


def dead_state(width, height):
    state = [[0 for x in range(width)] for y in range(height)]
    return state


def random_state(width, height):
    state = [[0 for x in range(width)] for y in range(height)]

    for row in range(height):
        for col in range (width):
            rand_number = random.random()

            if rand_number > 0.9:
               state[row][col] = 1
            else:
                state[row][col] = 0
    return state



def render(state):

    print('-'* (len(state[0]) + 4) ) # width board + " |  | " (borders)
    for row in state:
        print('| ' , end = '')

        for element in row:
            if element == 1: cell = u"\u2588"
            else: cell = ' '

            print (cell, end = '')

        print(' |')
    print('-'* (len(state[0]) + 4) ) # width board + " |  | " (borders)


def next_board_state(cur_state):
    width = len(cur_state[0])
    height = len(cur_state)

    next_state = dead_state(width, height)

    for row in range(height):
        for col in range(width):
            living_cells = 0

            row_start = row-1
            row_end = row+2
            col_start = col-1
            col_end = col+2

            if row == 0:
                row_start = row
            if row == len(cur_state) - 1:
                row_end = row+1
            if col == 0:
                col_start = col
            if col == len(cur_state[0]) - 1:
                col_end = col+1

            for a in range (row_start, row_end):
                for b in range (col_start,col_end):
                    if cur_state[a][b] == 1:
                        living_cells += 1

            if cur_state[row][col] == 1:

                if living_cells > 4:
                    next_state[row][col] = 0

                elif living_cells < 3:
                    next_state[row][col] = 0

                elif living_cells == 3 or living_cells == 4:
                    next_state[row][col] = 1

            if cur_state[row][col] == 0:

                if living_cells == 3:
                    next_state[row][col] = 1

    return next_state



if __name__ == "__main__":

    width = 100
    height = 50


    state = random_state(width,height)
    #state = [[0,0,0,0,0,0],
    #         [0,0,0,0,0,0],
    #         [0,0,0,0,0,0],
    #         [0,1,1,1,0,0],
    #         [0,0,0,0,0,0],
    #         [0,0,0,0,0,0]]

    while True:
        render(state)
        state = next_board_state(state)
        #time.sleep(.1)
        os.system("cls")
