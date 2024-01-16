
def count_ninjas(x, y, data):
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
                    if r[j] == 'N':
                        count += 1
                except IndexError:
                    break
        except IndexError:
            break
    return count


room = [
    ['N', ' ', ' ', ' ', ' '],
    ['N', 'N', 'N', 'N', ' '],
    ['N', ' ', 'N', ' ', ' '],
    ['N', 'N', 'N', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]
print(" ", "- " * 5)
for row in room:
    print("|", " ".join(row), "|")
print(" ", "- " * 5)
xcor = int(input("Input x coordinate: "))
ycor = int(input("Input y coordinate: "))
print(f"The tile is surrounded by {count_ninjas(xcor, ycor, room)} ninjas")
