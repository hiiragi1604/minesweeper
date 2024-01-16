# pylint: disable=locally-disabled, pointless-string-statement, line-too-long, consider-using-f-string, no-member, unused-variable, too-many-nested-blocks, too-many-branches
import random as r
import math as m
import time as t
from datetime import datetime
import os
import sys
import sweeperlib as sl

Result_text = {
    'w': """
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝

""",
    'l': """
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝

"""
}

Metadata = {
    'time_start': 0,
    'time_end': 0,
    'player': '',
    'elapsed': 0,
}
Game_actions = {
    'y': True,
    'n': False
}

Menu_actions = {
    'n': 1,
    'h': 2,
    'q': 3
}

History_actions = {
    'd': 1,
    'b': 2
}

State = {
    "field": []
}

Field_data = {
    "height": 0,
    "width": 0,
    "mines": 0,
    "placed_mine": False,
    "field": [],
    "play_field": [],
    "available": [],
    "opened": 0,
    "time": ''
}

def readme():
    """
    Print out the rules of minesweeper and instructions for the player
    """
    print("""
██████╗░███████╗░█████╗░██████╗░███╗░░░███╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░████║██╔════╝
██████╔╝█████╗░░███████║██║░░██║██╔████╔██║█████╗░░
██╔══██╗██╔══╝░░██╔══██║██║░░██║██║╚██╔╝██║██╔══╝░░
██║░░██║███████╗██║░░██║██████╔╝██║░╚═╝░██║███████╗
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚══════╝


ABOUT MINESWEEPER
Minesweeper is a game where mines are hidden in a grid of squares.
Safe squares have numbers telling you how many mines touch the square.
You can use the number clues to solve the game by opening all of the safe squares.
If you click on a mine you lose the game!


CONTROL
Left click to open the selected tile
Right click to mark the selected tile with a flag
Right click again to remove the flag from a tile


INPUT INSTRUCTION
The height of the field must be equal to or under 20
The width of the field must be equal to or under 38
The number of mines must be equal to or under the number of tiles minus 9

""")
    'input("Press enter to continue...")'
    os.system('pause')
def retry():
    """
    Prompt the options for retrying the game
    """
    choice = input("""Do you wish to play again? (Y/N)
""").lower().strip()
    try:
        if Game_actions[choice] is False:
            os.system('cls')
            print_title()
            menu()
        if Game_actions[choice] is True:
            os.system('cls')
            start_game()
    except KeyError:
        print("""Please input valid options
        """)
        retry()

def save_history(game_result):
    """
    Save game results to history
    """
    elapsed = Metadata['time_end'] - Metadata['time_start']
    remaining = (Field_data["height"] * Field_data["width"]) - Field_data["opened"] - Field_data["mines"]
    date = datetime.now().strftime("%Y.%m.%d")
    if os.path.isfile("history.txt") is False:
        with open("history.txt","a", encoding="utf-8") as file:
            file.close()
    with open("history.txt", "r+", encoding="utf-8") as target:
        content = target.read()
        target.seek(0, 0)
        target.write(f"""{date}\u00A0{Field_data["time"]}\u00A0{Metadata['player']}\u00A0{
        t.strftime("%H:%M:%S.{}".format(str(elapsed % 1)[2:])[:9], t.gmtime(elapsed))}\u00A0{
        game_result}\u00A0{Field_data["opened"]}\u00A0{remaining}\n""" + content)

def delete_history():
    """
    Delete game history
    """
    with open("history.txt", "w", encoding="utf-8") as target:
        target.write("")

def history_menu():
    """
    Prompt menu options for history
    """
    print("""
DELETE HISTORY (D)
BACK (B)""")
    try:
        choice = input("What would you like to do? ").lower().strip()
        if History_actions[choice] == 1:
            os.system('cls')
            delete_history()
            print("""Game history is deleted!
            """)
            os.system('pause')
            os.system('cls')
            view_history()
        if History_actions[choice] == 2:
            os.system('cls')
            print_title()
            menu()
    except KeyError:
        print("Please input valid options")
        history_menu()

def view_history():
    """
    Print previously saved game results
    """
    print("""GAME HISTORY:
      """)
    if os.path.isfile("history.txt") is False:
        with open("history.txt","a", encoding="utf-8") as file:
            file.close()
    with open("history.txt", "r", encoding="utf-8") as target:
        while True:
            line = target.readline()
            if not line:
                break
            date, Field_data["time"], player, elapsed, result, Field_data["opened"], remaining = line.split('\u00A0')
            print(f"""{date} at {Field_data["time"]}, player {player} played a game for {
                elapsed} and {
                result}, with {Field_data["opened"]} tiles opened and {remaining} tiles left""")
    history_menu()

def print_title():
    """
    Print the title of the game
    """
    print("""
    
███╗░░░███╗██╗███╗░░██╗███████╗░██████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░███████╗██████╗░
████╗░████║██║████╗░██║██╔════╝██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║██╔██╗██║█████╗░░╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░██████╔╝█████╗░░██████╔╝
██║╚██╔╝██║██║██║╚████║██╔══╝░░░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░██╔═══╝░██╔══╝░░██╔══██╗
██║░╚═╝░██║██║██║░╚███║███████╗██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

""")

def menu():
    """
    Prompt the main menu options of the game
    """
    print("""
NEW GAME (N)
GAME HISTORY (H)
QUIT (Q)
""")
    menu_action = input("What would you like to do? ").lower().strip()
    try:
        if Menu_actions[menu_action] == 1:
            os.system('cls')
            start_game()
        if Menu_actions[menu_action] == 2:
            os.system('cls')
            view_history()
        if Menu_actions[menu_action] == 3:
            os.system('cls')
            sys.exit()
    except KeyError:
        print("""Please input valid options
        """)
        menu()
    
def win_con(y, x):
    """
    Check if the game is ended or not
    """
    print(f"""Opened: {Field_data["opened"]}.   Remaining: {(Field_data["height"] * Field_data["width"]) - Field_data["mines"] - Field_data["opened"]}""")
    game_ended = False
    if (Field_data["height"] * Field_data["width"]) - Field_data["mines"] == Field_data["opened"]:
        print(Result_text['w'])
        result = 'won'
        game_ended = True
    if Field_data["play_field"][x][y] == 'x':
        print(Result_text['l'])
        result = 'lost'
        game_ended = True
    if game_ended is True:
        Metadata['time_end'] = t.time()
        sl.close()
        save_history(result)
        retry()
    
def start_game():
    """
    Start new game
    """
    try:
        Metadata['player'] = input("Enter player's name: ")
        Field_data["height"] = int(input("Enter height: "))
        Field_data["width"] = int(input("Enter width: "))
        Field_data["mines"] = int(input("Enter number of mines: "))
        if Field_data["height"] > 20 or Field_data["width"] > 38 or Field_data["mines"] > (Field_data["height"] * Field_data["width"]) - 9:
            print("Please enter appropriate values!")
            start_game()
        else:
            Field_data["field"] = []
            Field_data["opened"] = 0
            for row in range(Field_data["height"]):
                Field_data["field"].append([])
                for col in range(Field_data["width"]):
                    Field_data["field"][-1].append(" ")
            Field_data["play_field"] = []
            for row in range(Field_data["height"]):
                Field_data["play_field"].append([])
                for col in range(Field_data["width"]):
                    Field_data["play_field"][-1].append(" ")
            State["field"] = Field_data["field"]
            Field_data["available"] = []
            for x in range(Field_data["width"]):
                for y in range(Field_data["height"]):
                    Field_data["available"].append((x, y))
            Field_data["placed_mine"] = False
            start_window()
    except ValueError:
        print("""Please input valid option
                """)
        start_game()

def place_mines(matrix, avail, mine, x, y):
    """
    Places N mines to a field in random tiles.
    """
    track = (Field_data["height"] * Field_data["width"]) - 1
    while mine > 0:
        i = r.randint(0, track)
        x_1 = avail[i][0]
        y_1 = avail[i][1]
        if max(abs(x_1 - x), abs(y_1 - y)) > 1:
            avail.pop(i)
            matrix[y_1][x_1] = 'x'
            mine -= 1
            track -= 1


def initialize(coor_y, coor_x):
    """
    Initialize the fields for new game
    """
    Field_data["play_field"][coor_x][coor_y] = 0
    place_mines(Field_data["field"], Field_data["available"], Field_data["mines"], coor_y, coor_x)
    for row in range(Field_data["height"]):
        for col in range(Field_data["width"]):
            if Field_data["field"][row][col] != 'x':
                Field_data["field"][row][col] = count_mines(col, row, Field_data["field"])
            if Field_data["play_field"][row][col] == 'f':
                Field_data["play_field"][row][col] = ' '
    floodfill(Field_data["play_field"], Field_data["field"], coor_y, coor_x)
    Field_data["placed_mine"] = True


def count_mines(x, y, data):
    """
    Counts the mines surrounding one tile in the given room and
    returns the result.
    """
    count = 0
    if x == 0:
        x_start = 0
    else:
        x_start = x - 1
    if y == 0:
        y_start = 0
    else:
        y_start = y - 1
    for i in range(y_start, y + 2, 1):
        try:
            row = data[i]
            for j in range(x_start, x + 2, 1):
                try:
                    if row[j] == 'x':
                        count += 1
                except IndexError:
                    break
        except IndexError:
            break
    return count


def floodfill(matrix, base, x_1, y_1):
    """
    Marks previously unknown connected areas as safe, starting from the given
    x, y coordinates.
    """
    lis = [(x_1, y_1)]
    while len(lis) != 0:
        try:
            if base[lis[- 1][1]][lis[- 1][0]] == 'x':
                del lis[-1]
        except IndexError:
            if len(lis) > 0:
                del lis[-1]
        try:
            if base[lis[- 1][1]][lis[- 1][0]] != "x":
                matrix[lis[- 1][1]][lis[- 1][0]] = base[lis[- 1][1]][lis[- 1][0]]
                Field_data["opened"] += 1
                'print("Opened at floodfill")'
                if lis[- 1][0] == 0:
                    x_start = 0
                else:
                    x_start = lis[- 1][0] - 1
                if lis[- 1][1] == 0:
                    y_start = 0
                else:
                    y_start = lis[- 1][1] - 1
                end_x = lis[- 1][0]
                end_y = lis[- 1][1]
                if base[lis[- 1][1]][lis[- 1][0]] != 0:
                    del lis[-1]
                    continue
                del lis[-1]
                for j in range(y_start, end_y + 2, 1):
                    try:
                        for i in range(x_start, end_x + 2, 1):
                            try:
                                if matrix[j][i] == ' ':
                                    if (i, j) in lis:
                                        pass
                                    else:
                                        lis.insert(0, (i, j))
                            except IndexError:
                                break
                    except IndexError:
                        break
        except IndexError:
            if len(lis) > 0:
                del lis[-1]


def draw_field():
    """
    A handler function that draws a field represented by a two-dimensional list
    into a game window. This function is called whenever the game engine requests
    a screen update.
    """
    sl.clear_window()
    sl.begin_sprite_draw()
    for j in range(0, Field_data["width"], 1):
        for i in range(0, Field_data["height"], 1):
            match Field_data["play_field"][i][j]:
                case 'x':
                    sl.prepare_sprite('x', j * 40, (Field_data["height"] - 1 - i) * 40)
                case ' ':
                    sl.prepare_sprite(' ', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 0:
                    sl.prepare_sprite('0', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 1:
                    sl.prepare_sprite('1', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 2:
                    sl.prepare_sprite('2', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 3:
                    sl.prepare_sprite('3', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 4:
                    sl.prepare_sprite('4', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 5:
                    sl.prepare_sprite('5', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 6:
                    sl.prepare_sprite('6', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 7:
                    sl.prepare_sprite('7', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 8:
                    sl.prepare_sprite('8', j * 40, (Field_data["height"] - 1 - i) * 40)
                case 'f':
                    sl.prepare_sprite('f', j * 40, (Field_data["height"] - 1 - i) * 40)
    sl.draw_sprites()


def handle_mouse(x, y, m_button, mod_key):
    """
    This function is called when a mouse button is clicked inside the game window.
    Prints the position and clicked button of the mouse to the terminal.
    """
    if m_button & sl.MOUSE_LEFT:
        if Field_data["placed_mine"] is False:
            coor_y = int(m.ceil(x/40)) - 1
            coor_x = Field_data["height"] - int(m.ceil(y/40))
            initialize(coor_y, coor_x)
            win_con(coor_y, coor_x)
        else:
            coor_y = int(m.ceil(x/40)) - 1
            coor_x = Field_data["height"] - int(m.ceil(y/40))
            if Field_data["play_field"][coor_x][coor_y] == 'f':
                return
            if Field_data["field"][coor_x][coor_y] != 0 and Field_data["play_field"][coor_x][coor_y] == ' ':
                Field_data["play_field"][coor_x][coor_y] = Field_data["field"][coor_x][coor_y]
                if Field_data["field"][coor_x][coor_y] != 'x':
                    Field_data["opened"] += 1
                'print("Opened at left click")'
            elif Field_data["field"][coor_x][coor_y] == 0 and Field_data["play_field"][coor_x][coor_y] == ' ':
                floodfill(Field_data["play_field"], Field_data["field"], coor_y, coor_x)
            draw_field()
            win_con(coor_y, coor_x)
    if m_button & sl.MOUSE_RIGHT:
        coor_y = int(m.ceil(x/40)) - 1
        coor_x = Field_data["height"] - int(m.ceil(y/40))
        if Field_data["play_field"][coor_x][coor_y] == 'f':
            Field_data["play_field"][coor_x][coor_y] = ' '
        elif Field_data["play_field"][coor_x][coor_y] == ' ':
            Field_data["play_field"][coor_x][coor_y] = 'f'


def start_window():
    """
    Loads the game graphics, creates a game window and sets a draw handler for it.
    """
    sl.load_sprites("sprites")
    sl.create_window(Field_data["width"] * 40, Field_data["height"] * 40)
    sl.set_mouse_handler(handle_mouse)
    sl.set_draw_handler(draw_field)
    Metadata['time_start'] = t.time()
    Field_data["time"] = datetime.now().strftime('%H:%M:%S')
    sl.start()


def main():
    """
    Main function
    """
    os.system('cls')
    readme()
    os.system('cls')
    print_title()
    menu()

if __name__ == "__main__":
    main()
