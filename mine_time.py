import random as r
import sweeperlib as sl
state = {
    "field": []
}
field = []
for row in range(10):
    field.append([])
    for col in range(15):
        field[-1].append(" ")
state["field"] = field
    
available = []
for x in range(15):
    for y in range(10):
        available.append((x, y))

def place_mines(matrix, avail, mine):
    """
    Places N mines to a field in random tiles.
    """
    track = 149
    while mine > 0:
        i = r.randint(0, track)
        x_1 = avail[i][0]
        y_1 = avail[i][1]
        avail.pop(i)
        matrix[y_1][x_1] = 'x'
        mine -= 1
        track -= 1

def draw_field():
    """
    A handler function that draws a field represented by a two-dimensional list
    into a game window. This function is called whenever the game engine requests
    a screen update.
    """
    sl.clear_window()
    sl.begin_sprite_draw()
    for j in range(0, 15, 1):
        for i in range(0, 10, 1):
            match field[i][j]:
                case 'x':
                    sl.prepare_sprite('x', j * 40, i * 40)
                case ' ':
                    sl.prepare_sprite(' ', j * 40, i * 40)
    sl.draw_sprites()

def main():
    """
    Loads the game graphics, creates a game window and sets a draw handler for it.
    """
    
    sl.load_sprites("sprites")
    sl.create_window(600, 400)
    sl.set_draw_handler(draw_field)
    sl.start()
    
if __name__ == "__main__":
    place_mines(field, available, 35)
    main()
    