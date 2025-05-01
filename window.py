
from tkinter import Tk, BOTH, Canvas
from line import Line
from cell import Cell

class Window():
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="blue", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

    
    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self,lin1,fill_color ):
       lin1.draw(self.__canvas,fill_color)
       self.__canvas.pack(fill=BOTH, expand=1)

    def draw_cell(self,cell1,fill_color ):
       cell1.draw(self.__canvas,fill_color)
       self.__canvas.pack(fill=BOTH, expand=1)

 