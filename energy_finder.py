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