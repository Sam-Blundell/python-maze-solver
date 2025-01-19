from geometry import Point, Line

class Cell():
    def __init__(self, window=None):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.wall_t = True
        self.wall_r = True
        self.wall_b = True
        self.wall_l = True
        self.visited = False
        self.win = window

    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        t_line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
        r_line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
        b_line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
        l_line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
        self.win.draw_line(t_line, "black" if self.wall_t else "white")
        self.win.draw_line(r_line, "black" if self.wall_r else "white")
        self.win.draw_line(b_line, "black" if self.wall_b else "white")
        self.win.draw_line(l_line, "black" if self.wall_l else "white")

    def draw_move(self, to_cell, undo=False):
        color = "red" if undo else "gray"
        start_point = Point(
            self.x1 + ((self.x2 - self.x1) / 2),
            self.y1 + ((self.y2 - self.y1) / 2),
        )
        end_point = Point(
            to_cell.x1 + ((to_cell.x2 - to_cell.x1) / 2),
            to_cell.y1 + ((to_cell.y2 - to_cell.y1) / 2),
        )
        self.win.draw_line(Line(start_point, end_point), color)
