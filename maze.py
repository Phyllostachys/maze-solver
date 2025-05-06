import time

from graphics import Window
from cell import Cell

class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for idx in range(0, self._num_cols):
            sub_list = []
            for jdx in range(0, self._num_rows):
                sub_list.append(Cell(self._win))
            self._cells.append(sub_list)
        
        for idx in range(0, self._num_cols):
            for jdx in range(0, self._num_rows):
                self._draw_cell(idx, jdx)

    def _draw_cell(self, i: int, j: int):
        c: Cell = self._cells[i][j]
        top_left_x = self._x1 + (i % self._num_cols) * self._cell_size_x
        top_left_y = self._y1 + (j % self._num_rows) * self._cell_size_y
        print(f"cell ({i}, {j}) - top_left_x = {top_left_x}, top_left_y = {top_left_y}")
        c.draw(top_left_x, top_left_y, top_left_x + self._cell_size_x, top_left_y + self._cell_size_y)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.008)