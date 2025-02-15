from window import Window, Point, Line
from maze import Cell


def main():
    win = Window(800, 600)
    line = Line(Point(20,20),Point(150,150))
    win.draw_line(line, "blue")

    cell_1 = Cell(win)
    cell_1.has_left_wall = False
    cell_1.draw(50, 50, 100, 100)

    cell_2 = Cell(win)
    cell_2.has_bottom_wall = False
    cell_2.draw(100, 100, 150, 150)

    cell_1.draw_move(cell_2)

    win.wait_for_close()

if __name__ == "__main__":
    main()    