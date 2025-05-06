from tkinter import Canvas, Tk, BOTH

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def draw(self, c: Canvas, fill_color: str="black"):
        c.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)


class Window:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(master=self.__root, bg="grey", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
    
    def draw_line(self, l: Line, fill_color: str="black"):
        l.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False        