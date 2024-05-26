def load_sudoku(filename):
    board = []

    with open(filename,'r') as file:
        for line in file:
            row = line.strip()
            if row:
                board.append([int(val) if val != 'x' else 0 for val in row])
    return board

