from graphics import Line, Point, Window
from cell import Cell
from maze import Maze

if __name__ == "__main__":
    print("Hello from maze-solver!")

    width = 800
    height = 600
    cell_size = 15
    padding = 10
    rows = (height - (2 * padding)) // cell_size
    cols = (width - (2 * padding)) // cell_size

    w = Window(width, height)
    m = Maze(padding, padding, rows, cols, cell_size, cell_size, w)
    m.solve()

    w.wait_for_close()
