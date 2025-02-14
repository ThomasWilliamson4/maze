from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("root")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)







class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_one, point_two):
        self.x1 = point_one.x
        self.x2 = point_two.x
        self.y1 = point_one.y
        self.y2 = point_two.y

    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
        
    