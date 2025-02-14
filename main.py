from window import Window, Point, Line


def main():
    win = Window(800, 600)
    line = Line(Point(20,20),Point(150,150))
    win.draw_line(line, "blue")
    win.wait_for_close()

if __name__ == "__main__":
    main()    