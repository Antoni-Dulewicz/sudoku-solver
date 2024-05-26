<font size="6">
Sudoku Solver
</font>
<br>

In this repo I implemented the simulated annealing algorithm to solve the sudoku puzzle.  The puzzle starts with some cells filled in with digits, and the goal is to fill in the remaining cells.

1. Algorithm starts by randomly filling in the empty cells with digits ensuring that there aren't any conflicts in each 3x3 grid. 
```python
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
```
<br>
Generating neighbour state:
The algorithm randomly selects a 3x3 grid and 2 digits in it, checks if the digits aren't the ones given in init sudoku board and if not it switches them.

```python
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
```
<br>
Calculating energy:
It calculates the energy of the current solution by counting the number of conflicts in the rows, columns. 

```python
def find_energy(board):
    n = len(board)

    energy = 0
    
    for row in board:
        num_counter = [0 for _ in range(n+1)]

        for num in row:
            if num != 0:
                if num_counter[num] > 0:
                    energy += 1
                num_counter[num] += 1

    for i in range(n):
        num_counter = [0 for _ in range(n+1)]
        for j in range(n):
            num = board[j][i]
            if num != 0:
                if num_counter[num] > 0:
                    energy += 1
                num_counter[num] += 1

    return energy
```


<br>
Multiple highs and lows in the energy and temperature plot are due to the reheat functionality. 
<br>
Given to-solve sudoku looks like that:

```python
3xxxxxx2x
xxxxxx964
2x8xxxx5x
17xx8xxxx
xxx2xxxx7
xxxx5x4xx
xx9xxxxxx
xx6xx4xx5
x2x9x6xxx
```
Where x is a cell to fill in.

Example of randomly filled sudoku board:
```python
[3, 7, 5, 5, 8, 2, 1, 2, 3]
[9, 4, 1, 7, 6, 3, 9, 6, 4]
[2, 6, 8, 1, 9, 4, 7, 5, 8]
[1, 7, 2, 7, 8, 4, 2, 5, 8]
[6, 9, 8, 2, 6, 1, 6, 1, 7]
[4, 3, 5, 3, 5, 9, 4, 9, 3]
[5, 3, 9, 7, 8, 2, 8, 3, 9]
[4, 7, 6, 5, 1, 4, 7, 1, 5]
[8, 2, 1, 9, 3, 6, 6, 4, 2]

With energy equals to: 49
```

Energy plot for the solution:

![energy](output/energy_plot.png)

Temperature plot for the solution:

![temp](output/temp_plot.png)

Solution:
```python
[3, 6, 4, 1, 9, 5, 7, 2, 8]
[7, 5, 1, 8, 3, 2, 9, 6, 4]
[2, 9, 8, 6, 4, 7, 3, 5, 1]
[1, 7, 5, 4, 8, 9, 6, 3, 2]
[9, 4, 3, 2, 6, 1, 5, 8, 7]
[6, 8, 2, 7, 5, 3, 4, 1, 9]
[4, 3, 9, 5, 2, 8, 1, 7, 6]
[8, 1, 6, 3, 7, 4, 2, 9, 5]
[5, 2, 7, 9, 1, 6, 8, 4, 3]

With energy equals to: 0
```

Source code of whole solver function can be found in [solve.py](solve.py)
