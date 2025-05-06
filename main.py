from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def draw(self, c: Canvas, fill_color: str):
        c.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(master=self.__root, bg="grey")
        self.__canvas.pack()
        self.__running = False
    
    def draw_line(self, l: Line, fill_color: str):
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

def main():
    print("Hello from maze-solver!")

    w = Window(800, 600)
    w.draw_line(Line(Point(4, 10), Point(10, 30)), "white")
    w.draw_line(Line(Point(1, 25), Point(45, 27)), "white")
    w.draw_line(Line(Point(8, 7), Point(70, 150)), "white")
    w.wait_for_close()


if __name__ == "__main__":
    main()
