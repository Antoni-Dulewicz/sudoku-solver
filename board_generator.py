from copy import deepcopy
import numpy as np

def generate_first_board(board):
    n = len(board)
    new_board = deepcopy(board)

    for x_start,x_end in [(0,3),(3,6),(6,9)]:
        for y_start,y_end in [(0,3),(3,6),(6,9)]:

            num_counter = [0 for _ in range(n+1)]

            for i in range(y_start,y_end):
                for j in range(x_start,x_end):
                    num = board[i][j]
                    if num != 0:
                        num_counter[num] += 1

            
            free_numbers = []
            for k in range(1,n+1):
                cnt = num_counter[k]
                if cnt == 0:
                    free_numbers.append(k)

            np.random.shuffle(free_numbers)
            k = 0
            for i in range(y_start,y_end):
                for j in range(x_start,x_end):
                    if board[i][j] == 0:
                        new_board[i][j] = free_numbers[k]
                        k += 1 

    return new_board

def generate_neighboard(initial_board,board):

    new_board = deepcopy(board)

    x_ranges = [(0,3),(3,6),(6,9)]
    y_ranges = [(0,3),(3,6),(6,9)]

    x_idx = np.random.randint(0, len(x_ranges))
    y_idx = np.random.randint(0, len(y_ranges))

    x_start,x_end = x_ranges[x_idx]
    y_start,y_end = y_ranges[y_idx]

    not_initial = []

    for i in range(y_start,y_end):
        for j in range(x_start,x_end):
            if initial_board[i][j] == 0:
                not_initial.append((j,i))
    

    selected = np.random.choice(len(not_initial), size=2, replace=False)
    
    x1,y1 = not_initial[selected[0]]
    x2,y2 = not_initial[selected[1]]

    new_board[y1][x1],new_board[y2][x2] = new_board[y2][x2],new_board[y1][x1]
    return new_board

