from window import Line, Point, Window
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 =y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self._create_cells()
        
    def _create_cells(self):
        self._cells = [[Cell(self.win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        pos_x = (i*self.cell_size_x) + self.x1
        pos_y = (j*self.cell_size_y) + self.y1
        self._cells[i][j].draw(pos_x, pos_y, pos_x+ self.cell_size_x, pos_y+self.cell_size_y)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)


class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1),Point(x1, y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1),Point(x2, y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1),Point(x2, y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2),Point(x2, y2))
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        from_x = (self._x1 + self._x2)/2
        from_y = (self._y1 + self._y2)/2
        to_x = (to_cell._x1 + to_cell._x2)/2
        to_y = (to_cell._y1 + to_cell._y2)/2
        line = Line(Point(from_x, from_y), Point(to_x, to_y))
        line_color = "gray"       
        if undo == False:
            line_color = "red"
        self._win.draw_line(line, line_color)
        
        
