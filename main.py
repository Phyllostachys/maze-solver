from graphics import Line, Point, Window
from cell import Cell

if __name__ == "__main__":
    print("Hello from maze-solver!")

    w = Window(800, 600)
    # w.draw_line(Line(Point(4, 10), Point(10, 30)), "white")
    # w.draw_line(Line(Point(1, 25), Point(45, 27)), "white")
    # w.draw_line(Line(Point(8, 7), Point(70, 150)), "white")
    c1 = Cell(w)
    c1.has_right_wall = False
    c1.draw(10, 10, 100, 100)

    c2 = Cell(w)
    c2.has_left_wall = False
    c2.draw(101, 101, 150, 150)

    c3 = Cell(w)
    c3.has_bottom_wall = False
    c3.draw(150, 150, 160, 160)

    c4 = Cell(w)
    c4.has_top_wall = False
    c4.draw(165, 165, 170, 170)

    w.wait_for_close()
