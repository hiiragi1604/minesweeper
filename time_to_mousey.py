import sweeperlib as sl
Keys = {
    sl.MOUSE_LEFT: "left",
    sl.MOUSE_RIGHT: "right",
    sl.MOUSE_MIDDLE: "middle",
}

def handle_mouse(x, y, m_button, mod_key):
    """
    This function is called when a mouse button is clicked inside the game window.
    Prints the position and clicked button of the mouse to the terminal.
    """
    print(f"The {Keys[m_button]} mouse button was pressed at {x}, {y}")

def main():
    """
    Creates a game window and sets a handler for mouse clicks.
    Starts the game.
    """
    sl.create_window()
    sl.set_mouse_handler(handle_mouse)
    sl.start()

if __name__ == "__main__":
    main()
