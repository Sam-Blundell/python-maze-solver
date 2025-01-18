from window import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    Maze(win, 20, 20, 40, 40, 19, 14)
    win.wait_for_close()

main()
