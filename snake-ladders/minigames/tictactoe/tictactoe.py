def make_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False
def round(player):
    print (f"{player}'s turn")

def switch_player(player):
   if player == 'X':
       return 'O'
   else:
       return 'X'
   
   
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            winner = row[0]
            loser = ' ' if winner == 'X' else 'X'
            return winner, loser
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            winner = board[0][col]
            loser = 'O' if winner == 'X' else 'X'
            return winner, loser
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        winner = board[0][0]
        loser = 'O' if winner == 'X' else 'X'
        return winner, loser
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        winner = board[0][2]
        loser = 'O' if winner == 'X' else 'X'
        return winner, loser
    
    return None 
check_draw = lambda board: all(cell != ' ' for row in board for cell in row)  

result = check_winner(board)
if result:
    winner, loser = result
    print(f"{winner} wins! {loser} loses.") 
elif check_draw(board):
    print("It's a draw!")

