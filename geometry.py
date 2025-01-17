class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two
    
    def draw(self, canvas, fill):
        canvas.create_line(self.point_one.x, self.point_one.y, self.point_two.x, self.point_two.y, fill=fill, width=2)
