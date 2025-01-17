from geometry import Point, Line

class Cell():
    def __init__(self, window, x1, y1, x2, y2, wall_t=True, wall_r=True, wall_b=True, wall_l=True):
        self.win = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.wall_t = wall_t
        self.wall_r = wall_r
        self.wall_b = wall_b
        self.wall_l = wall_l

    def draw(self):
        if self.wall_t:
            t_line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(t_line)
        if self.wall_r:
            r_line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(r_line)
        if self.wall_b:
            b_line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(b_line)
        if self.wall_l:
            l_line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(l_line)

