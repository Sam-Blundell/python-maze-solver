from window import Window
from cell import Cell
from maze import Maze

def main():
    screen_x = 800
    screen_y = 600
    margin = 50
    num_rows = 12
    num_cols = 16
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)
    my_maze = Maze(margin, margin, cell_size_x, cell_size_y, num_rows, num_cols, win, 1)
    my_maze.solve()
    win.wait_for_close()

main()
