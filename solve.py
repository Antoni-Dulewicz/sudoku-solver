from load import load_sudoku
from copy import deepcopy
from plots import plot_energies,plot_temparatures,clear_output_folder
from energy_finder import find_energy
from board_generator import generate_first_board,generate_neighboard
import numpy as np

def solve_sudoku(initial_board,initial_temp,end_temp,cooling_rate,max_iter,output_folder = 'output'):

    clear_output_folder(output_folder)

    #generete a board in which numbers in 3x3 squares are unique
    curr_board = generate_first_board(initial_board)

    for r in curr_board:
        print(r)

    print(find_energy(curr_board))

    #set temp to inital temparature
    temparature = initial_temp
    best_board = deepcopy(curr_board)

    stuck_count = 0
    reheat_rate = initial_temp/0.3

    best_E = find_energy(curr_board)
    E = find_energy(curr_board)

    energies = []
    temparatures = []
    
    target = 0

    #iterate untill max_iter
    for i in range(max_iter):
        if i%10000 == 0 :
            print("Iteration "+str(i)+", temparature: "+str(temparature)+", current score:"+str(E)+"  Best score: "+str(best_E))


        #if our energy reaches the target -> break
        if E == target:
            break


        #if temparature < then ending temaprature -> break
        if temparature < end_temp:
            break 
        

        #reheating
        if stuck_count > 10000 or temparature < 1e-4:
            tmp = temparature *reheat_rate
            print("Program is stuck - rehating from: " + str(temparature) + "to: " + str(tmp))
            temparature *= reheat_rate
            curr_board = generate_first_board(initial_board)
            stuck_count = 0

        #generate new_board
        new_board = generate_neighboard(initial_board,curr_board)

        #find energy of new board
        new_E = find_energy(new_board)

        # if energy is smaller or our probability function allows us -> set energy to new energy
        if new_E < E or np.random.rand() < np.exp((E - new_E) / temparature):
            curr_board = deepcopy(new_board)
            E = new_E
            if new_E < find_energy(best_board):
                best_board = deepcopy(new_board)
                best_E = new_E
            stuck_count = 0

        temparatures.append(temparature)
        energies.append(E)
        temparatures.append(temparature)
        temparature *= cooling_rate
        stuck_count += 1


    plot_energies(energies,output_folder)
    plot_temparatures(temparatures,output_folder)
    return best_board




filename = 'sudoku/sudoku_board.txt'
sudoku_board = load_sudoku(filename)

best_board = solve_sudoku(sudoku_board,10,0.000001,0.99999,5000000)

print(find_energy(best_board))
print("Solved sudoku:\n")
for r in best_board:
    print(r)