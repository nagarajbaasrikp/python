# assign markers
# draw board
# take input
# check for game over
# repeat previous 2 steps
# ask if players want to play again
game_over = False
play_again = True
board = [[None, None, None], [None, None, None], [None, None, None]]
assignment = {}
mapping = {
        7: [0, 0],
        8: [0, 1],
        9: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        1: [2, 0],
        2: [2, 1],
        3: [2, 2],
    }

def assign():
    choice = 0
    valid_input = False
    try:
        while not valid_input:
            choice = int(input('Enter 1 for X or 2 for O'))
            if choice == 1:
                assignment = {'player_1': 'X', 'player_2': 'O'}
                valid_input = True
            elif choice == 2:
                assignment = {'player_1': 'O', 'player_2': 'X'}
                valid_input = True
            else:
                continue
    except Exception as e:
        print(e)
        assign()
    return assignment

def draw():
    for row in board:
        for position in row:
            if position is None:
                print('_', end='\t')
            else:
                print(position, end='\t')
        print('\n')

def check_for_victory():
    for row in board:
        if (row[0] == row[1] == row[2]) and row[0] != None:
            return True
        if ((board[0][0] == board[1][0] == board[2][0]) and board[0][0] != None) or ((board[0][1] == board[1][1] == board[2][1]) and board[0][1] != None) or ((board[0][2] == board[1][2] == board[2][2]) and board[0][2] != None):
            return True
        if ((board[0][0] == board[1][1] == board[2][2]) and board[0][0] != None) or ((board[0][2] == board[1][1] == board[2][0]) and board[0][2] != None):
            return True

def take_input():
    game_ongoing = True
    i = 1
    if assignment['player_1'] == 'X':
        order = [['player_1', 'X'], ['player_2', 'O']]
    else:
        order = [['player_2', 'X'], ['player_1', 'O']]
    print(order)
    while game_ongoing and i in range(1, 10):
        try:
            choice = int(input('Enter 1 - 9 for positions'))
            if choice in range(1, 10):
                print(mapping)
                print(mapping[choice][0], mapping[choice][1], order[0][1])
                if board[mapping[choice][0]][mapping[choice][1]] is None: 
                    board[mapping[choice][0]][mapping[choice][1]] = order[0][1]
                    temp = order[0]
                    order[0] = order[1]
                    order[1] = temp
                    draw()
                else:
                    print('Slot taken')
                    continue
                if check_for_victory():
                    print('Game Over')
                    return
        except Exception as e:
            print(e)
            continue

while play_again:
    assignment = assign()
    print(assignment)
    while not game_over:
        take_input()
        game_over = True
    board = [[None, None, None], [None, None, None], [None, None, None]]
    try:
        choice = int(input("Press 1 to play again, anything else to quit"))
        if choice == 1:
            continue
        else:
            exit(0)
    except Exception as e:
        print(e)