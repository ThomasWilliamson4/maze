from window import Line, Point, Window
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 =y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        if seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

        
    def _create_cells(self):

        self._cells = [[Cell(self.win) for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        pos_x = (j*self.cell_size_x) + self.x1
        pos_y = (i*self.cell_size_y) + self.y1
        self._cells[i][j].draw(pos_x, pos_y, pos_x+ self.cell_size_x, pos_y+self.cell_size_y)
        self._animate()

    
    def _animate(self):
        if self.win is None:
            return        
        self.win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        start.has_top_wall = False
        end = self._cells[self.num_rows-1][self.num_cols-1]
        end.has_bottom_wall = False
        end.draw(end._x1, end._y1, end._x2, end._y2)
        start.draw(start._x1, start._y1, start._x2, start._y2)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j]._visited:
                to_visit.append((i-1, j))
            if j > 0 and not self._cells[i][j-1]._visited:
                to_visit.append((i, j-1))
            if i +1  < self.num_cols and not self._cells[i+1][j]._visited:
                to_visit.append((i+1, j))
            if j +1  < self.num_rows and not self._cells[i][j+1]._visited:
                to_visit.append((i, j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            index = random.randrange(0,len(to_visit))
            cell = to_visit[index] 
            new_i = cell[0]
            new_j = cell[1]

            if i+1 == new_i:
                self._cells[i][j].has_right_wall = False
                self._cells[new_i][new_j].has_left_wall = False
            if i-1 == new_i:
                self._cells[i][j].has_left_wall = False
                self._cells[new_i][new_j].has_right_wall = False
            if j+1 == new_j:
                self._cells[i][j].has_top_wall = False
                self._cells[new_i][new_j].has_bottom_wall = False
            if j-1 == new_j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_i][new_j].has_top_wall = False
            
            self._break_walls_r(new_i, new_j)
            



class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self._visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        color = "black" if self.has_left_wall else "#d9d9d9"
        line = Line(Point(x1, y1),Point(x1, y2))
        self._win.draw_line(line, color)
        
        color = "black" if self.has_right_wall else "#d9d9d9"
        line = Line(Point(x2, y1),Point(x2, y2))
        self._win.draw_line(line, color)

        color = "black" if self.has_top_wall else "#d9d9d9"
        line = Line(Point(x1, y1),Point(x2, y1))
        self._win.draw_line(line, color)

        color = "black" if self.has_bottom_wall else "#d9d9d9"
        line = Line(Point(x1, y2),Point(x2, y2))
        self._win.draw_line(line, color)

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
        
        
