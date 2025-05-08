from graphics import Point, Line, Window

class Cell:
    def __init__(self, win: Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.visited = False
        self._win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self._win is None:
            return
        
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
    
    def draw_move(self, to_cell: 'Cell', undo=False):
        line_color = "gray"
        if undo:
            line_color = "red"

        first_middle = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        second_middle = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        line = Line(first_middle, second_middle)
        self._win.draw_line(line, line_color)