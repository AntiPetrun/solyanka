import os
from string import digits
from game_stat import data
import time

the_board = [i for i in range(1, 10)]
menu_answer = {'1': 'statistic', '2': 'playgame', '3': 'exit'}
is_the_user_x = True
TURNS = {True: 'X', False: 'O'}


def get_answer():
    answer = input('Your choise: ')
    return menu_answer.get(answer)


def show_menu():
    os.system('clear')
    print(
    '___MENU___\n',
    '1. Show statistic\n',
    '2. Play the game\n',
    '3. Exit\n'
    )
    answer = get_answer()
    while not answer:
        print('Pls peek the right option')
        answer = get_answer()
    return answer


def show_the_board():
    os.system('clear')
    print(f'{the_board[0]} | {the_board[1]} | {the_board[2]}')
    print('--|---|--')
    print(f'{the_board[3]} | {the_board[4]} | {the_board[5]}')
    print('--|---|--')
    print(f'{the_board[6]} | {the_board[7]} | {the_board[8]}')


def show_statistic():
    os.system('clear')
    with open('game_stat.py', 'r') as file:
        file.seek(0)
        for line in file:
            print(line)
    time.sleep(5)
    main()


def exit():
    while True:
        break


def get_user_turn():
    while True:
        global is_the_user_x
        turn = input(f'User {TURNS.get(is_the_user_x)} turn (1-9): ')
        try:
            if int(turn) in the_board:
                the_board.insert(int(turn) - 1, TURNS.get(is_the_user_x))
                the_board.remove(int(turn))
                is_the_user_x = not is_the_user_x
                return turn
            else:
                print('Enter correct value or this cell is already occupied')
        except:
            print('Enter correct value or this cell is already occupied')


def check_win():
    win_combo = [
        [the_board[0], the_board[1], the_board[2]],
        [the_board[3], the_board[4], the_board[5]],
        [the_board[6], the_board[7], the_board[8]],
        [the_board[0], the_board[3], the_board[6]],
        [the_board[1], the_board[4], the_board[7]],
        [the_board[2], the_board[5], the_board[8]],
        [the_board[0], the_board[4], the_board[8]],
        [the_board[2], the_board[4], the_board[6]]
    ]
    for combo in win_combo:
        if combo[0] == combo[1] == combo[2]:
            return True


def check_draw():
    for symbol in the_board:
        if str(symbol) in 'XO':
            continue
        else:
            return False
    return True


def display_result():
    global the_board
    os.system('clear')
    if win is True:
        print(f'User {TURNS.get(not is_the_user_x)} has WON!\nPlease wait few second to enter MENU')
    elif draw is True:
        print('Your result is DRAW\nPlease wait few second to enter MENU')
    time.sleep(5)
    the_board = [i for i in range(1, 10)]
    main()


def play_the_game():
    print('Playing the game')
    show_the_board()
    global win, draw
    while True:
        turn = get_user_turn()
        show_the_board()
        win = check_win()
        if win is True:
            show_result = display_result()
            break
        draw = check_draw()
        if draw is False:
            continue
        elif draw is True:
            show_result = display_result()
            break


def main():
    answer = show_menu()
    if answer == 'statistic':
        show_statistic()
    elif answer == 'playgame':
        play_the_game()
    else:
        exit()
        

if __name__ == '__main__':
    main()
