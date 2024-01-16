# pylint: disable=too-many-nested-blocks
# pylint: disable=too-many-branches
import sweeperlib as sl


def draw_field():
    """
    A handler function that draws a field represented by a two-dimensional list
    into a game window. This function is called whenever the game engine requests
    a screen update.
    """
    sl.clear_window()
    sl.begin_sprite_draw()
    for j in range(0, 13, 1):
        for i in range(0, 6, 1):
            match planet[i][j]:
                case 'x':
                    sl.prepare_sprite('x', j * 40, (5 - i) * 40)
                case ' ':
                    sl.prepare_sprite(' ', j * 40, (5 - i) * 40)
                case 0:
                    sl.prepare_sprite('0', j * 40, (5 - i) * 40)
                case 1:
                    sl.prepare_sprite('1', j * 40, (5 - 1 - i) * 40)
                case 2:
                    sl.prepare_sprite('2', j * 40, (5 - 1 - i) * 40)
                case 3:
                    sl.prepare_sprite('3', j * 40, (5 - 1 - i) * 40)
                case 4:
                    sl.prepare_sprite('4', j * 40, (5 - 1 - i) * 40)
                case 5:
                    sl.prepare_sprite('5', j * 40, (5 - 1 - i) * 40)
                case 6:
                    sl.prepare_sprite('6', j * 40, (5 - 1 - i) * 40)
                case 7:
                    sl.prepare_sprite('7', j * 40, (5 - 1 - i) * 40)
                case 8:
                    sl.prepare_sprite('8', j * 40, (5 - 1 - i) * 40)
                case 9:
                    sl.prepare_sprite('f', j * 40, (5 - 1 - i) * 40)
    sl.draw_sprites()


def count_mines(x, y, data):
    """
    Counts the ninjas surrounding one tile in the given room and
    returns the result. The function assumes the selected tile does
    not have a ninja in it - if it does, it counts that one as well.
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
            r = data[i]
            for j in range(x_start, x + 2, 1):
                try:
                    if r[j] == 'x':
                        count += 1
                except IndexError:
                    break
        except IndexError:
            break
    return count


def floodfill(matrix, x_1, y_1):
    """
    Marks previously unknown connected areas as safe, starting from the given
    x, y coordinates.
    """
    lis = [(x_1, y_1)]
    while len(lis) > 0:
        try:
            if matrix[lis[- 1][1]][lis[- 1][0]] == 'x':
                del lis[-1]
        except IndexError:
            if len(lis) > 0:
                del lis[-1]
        try:
            if matrix[lis[- 1][1]][lis[- 1][0]] == ' ':
                matrix[lis[- 1][1]][lis[- 1][0]] = '0'
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


def main(matrix):
    """
    Loads the game graphics, creates a game window, and sets a draw handler
    """
    sl.load_sprites("sprites")
    sl.create_window(len(matrix[0])*40, len(matrix)*40)
    sl.set_draw_handler(draw_field)
    sl.start()


if __name__ == "__main__":
    planet = [
        [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "],
        [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "],
        [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "],
        ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "],
        ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "],
        [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
    ]
    xcor = int(input("x: "))
    ycor = int(input("y: "))
    floodfill(planet, xcor, ycor)
    main(planet)
    print(planet)
