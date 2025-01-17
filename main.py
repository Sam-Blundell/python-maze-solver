from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win, 40, 40, 60, 60, False, True, False, True)
    cell2 = Cell(win, 40, 60, 60, 80, False, False, True, True)
    cell3 = Cell(win, 60, 40, 80, 60, True, False, False, True)
    cell4 = Cell(win, 60, 60, 80, 80, False, True, True, False)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    win.wait_for_close()

main()
