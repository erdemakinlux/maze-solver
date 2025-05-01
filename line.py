from point import Point
from tkinter import Tk, BOTH, Canvas

class Line():
    def __init__(self,x1, x2, y1, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def draw(self,cnv,fill_color):
        cnv.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
