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
        win: Window=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

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
        # print(f"cell ({i}, {j}) - top_left_x = {top_left_x}, top_left_y = {top_left_y}")
        c.draw(top_left_x, top_left_y, top_left_x + self._cell_size_x, top_left_y + self._cell_size_y)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        
        self._win.redraw()
        time.sleep(0.008)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        last_x = self._num_cols - 1
        last_y = self._num_rows - 1
        self._cells[last_x][last_y].has_bottom_wall = False
        self._draw_cell(last_x, last_y)