
import random
'''
Welcome to Tic Tac Toe!
This game is designed for two players!
Player 1, Do you want to be X or O? X
Player 1 will go first.

Are you ready to play? Enter Yes or No.
Choose your next position: (1-9)

Congratulations! You have won the game!
Do you want to play again? Enter Yes or No:
Written by June Kang
Finished on June 13, 2022

'''


def display_board (board):
    '''
    create an array to show the board position
    '''
    print ('      |      |   ')
    print ( '  '+board[1] +'   |   ' +board[2]+'  |   '+board[3])
    print ('      |      |    ')
    print('---------------------')
    print ('      |      |    ')
    print ( '  '+board[4] +'   |   ' +board[5]+'  |   '+board[6])
    print ('      |      |    ')
    print('---------------------')
    print ('      |      |    ')
    print ( '  '+board[7] +'   |   ' +board[8]+'  |   '+board[9])
    print ('      |      |    ')
    return (board)




def player_input():
    '''
    Players use this function to pick X or O.
    '''
    sign = 'wrong' #initiate sign
    while sign not in ['X', 'O']:
        sign = input('Player 1, do you want to be X or O? ')

        if sign not in ['X', 'O']:
            print ("I don't understand. Please only input X or O")
        if sign == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
    return sign


def place_marker(board, marker, position):
    '''
    assign the desired positon and the correct marker to the board.
    '''
    board[position] = marker
    return board


def win_check(board, marker):
    '''
    Check to see if someone has won.
    '''
    return ((board[1] ==marker and board[2]==marker and board[3]==marker) or
    (board[4] ==marker and board[5]==marker and board[6]==marker) or
    (board[7] ==marker and board[8]==marker and board[9]==marker) or
    (board[1] ==marker and board[3]==marker and board[7]==marker) or
    (board[2] ==marker and board[4]==marker and board[8]==marker) or
    (board[3] ==marker and board[6]==marker and board[9]==marker) or
    (board[1] ==marker and board[5]==marker and board[9]==marker) or
    (board[3] ==marker and board[5]==marker and board[6]==marker))


def choose_first():
    '''
    Randomly decide which player goes first.
    import random is used here
    '''
    return (f'Player {random.randint(1,2)}')


def space_check(board, position):
    '''
    Return boolean value True if the space on the board is empty
    '''
    return board[position] == ' '


def full_board_check(board):
    '''
    checks if the board is full, return boolean True if it's full.
    '''
    for space in range(1,10):
        if space_check(board, space):
            return False # if space available, return false
    return True # otherwise, return True


def player_choice(board):
    '''
    This is the input of the position.
    A validation process is added to check the isdigit and within range.
    Space of the board is checked when isdigit and within range are True.
    '''
    space =0
    space1=0
    rangeforpos = range(0,10)
    with_range = False
    while with_range == False or space.isdigit()== False:
        space=input ('Choose your next position (1-9): ')
        if space.isdigit() == False:
            print ("This game only accepts digits. Please enter number 1 to 9! ")
        if space.isdigit() == True:
            space1= int(space)
            if space1 in rangeforpos:
                with_range = True
                space_check(board, space1)  #check the space availability
            else:
                print ("Please only enter number 1 to 9! ")
                with_range = False
    return int(space)

def replay():
    '''
    Check if player wants to play again. caseless match for answer entered.
    .lower() can also be used to replace .casefold()
    '''
    again = 'invalid'
    while again.casefold() not in ['yes', 'no']:
        again =input('Do you want to play again? Enter Yes or No: ')
    return again.casefold()=='yes'



def main():
    '''
    This is the main code.
    '''
    print ('Welcome to Tic Tac Toe!')
    sample_board = ['#', '1','2','3','4','5','6','7','8','9' ]
    display_board(sample_board)
    print('This game requires two player and the order is randomly assigned.')

    while True:
        '''
        Choose which player will go first.
        player_input() will return two marker, each assign to player 1 and 2.

        '''
        test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player_assign=choose_first()
        print (f'{player_assign} is going first.')
        player1_marker, player2_marker = player_input()


'''
while the game is on. Divide the function of player 1 or player 2.
Both part are replicates.

'''
        game_on = True
        while game_on:
            if player_assign == 'Player 1':
                board=display_board(test_board) #display board
                print ("It's player 1's turn.")
                pos = player_choice(board)  #player 1 choose where to place the marker
                if space_check(board, pos): #if the space is empty
                    marker=player1_marker
                    place_marker (board,marker, pos)    #place marker on board
                    if win_check(board, player1_marker):    #check  if win
                        game_on = False
                        display_board(board)
                        print('Congratulations! You have won the game!')
                    elif full_board_check(board):   #check full board
                        game_on = False
                        display_board(board)
                        print ('This is a draw.')
                    else:
                        player_assign ='Player 2'   #if move is made, no win, no full board, then player 2's turn.

            elif player_assign == 'Player 2':
                board=display_board(test_board)
                print ("It's Player 2's turn.")
                pos = player_choice(board)
                if space_check(board, pos):
                    marker=player2_marker
                    place_marker (board,marker, pos)
                    if win_check(board, player2_marker):
                        game_on = False
                        display_board(board)
                        print('Congratulations! You have won the game!')
                    elif full_board_check(board):
                        game_on = False
                        display_board(board)
                        print ('This is a draw.')
                    else:
                        player_assign = 'Player 1'


    #if player doesn't want to play again, exit
        if not replay():
            break
if __name__ =='__main__': main()
