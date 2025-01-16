from window import Window
from point import Point
from line import Line

def main():
    line = Line(Point(100, 200), Point(400, 500))
    win = Window(800, 600)
    win.draw_line(line, "black")
    win.wait_for_close()

main()
