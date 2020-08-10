import itertools
from colorama import Fore, Back, Style, init
init()

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
 

    #Horizontal Win Situation (---)
    for row in game:
        print(row)
        if all_same(row):
                print(f"Player {row[0]} is the winner Horizontally")
                return True
    
    #Diagnol Win Situation (\)
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner Diagonally")
        return True

    #Diagnol Win Situation (/)
    diags = []
    for i in range(len(game)):
        diags.append(game[i][i])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner Diagonally")
        return True
    
    #Vertical Win Situation
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])
    if all_same(check):
        print(f"Player {check[0]} is the winner Diagonally")
        return True
    return False


def game_board(game_map, player = 0, row = 0, coloumn = 0, just_display = False):
    try:
        if game_map[row][coloumn] != 0:
            print("This Positon is occupied")
            return game_map, False
        print("   "+"   ".join(str(i) for i in range(len(game_map))))
        if not just_display:
            game_map[row][coloumn] = player


        for count,row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "    " 
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.BLUE + ' O ' + Style.RESET_ALL
            print(count,colored_row)

        return game_map ,True
    
    except IndexError as e:
        print("Make Sure Your Input is 0, 1 or 2?",e)
        return game_map,False
    
    except Exception as e:
        print("Something Went Wrong!", e)
        return game_map,False
    

play = True
players = [1, 2]
while play:
    game_size = int(input("What Size Game of Tic Tac Toe : "))
    game = [[0 for i in range(game_size)]for i in range(game_size)]

    game_won = False
    game, _ = game_board(game , just_display = True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            coloumn_choice = int(input("What Coloumn Do You Want to Play?(0, 1, 2): "))
            row_choice = int(input("What Row Do You Want to Play?(0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, coloumn_choice)

        if win(game):
            game_won = True
            again = input("Game Over. Do You Wanna Play again?(y/n): ")
            if again.lower() == 'y':
                print("Restarting")
            elif again.lower() == 'n':
                print("Good Bye")
                play = False
            else:
                print("Not a valid answer")
                play = False
            