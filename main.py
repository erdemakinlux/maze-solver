from window import Window
from line import Line
from cell import Cell
from point import Point


def main():
    #maze solver
    win = Window(800, 600)
    #lin1 = Line(Point(50,50), Point(100,100))
    #win.draw_line(lin1,"red")
    cell1 = Cell(True,False,True,True,1,51,1,51)
    cell2 = Cell(True,True,False,True,101,151,1,51)
    cell3 = Cell(False,True,True,True,1,51,101,151)
    cell4 = Cell(True,True,True,False,101,151,101,151)
    win.draw_cell(cell1,"red")
    win.draw_cell(cell2,"red")
    win.draw_cell(cell3,"red")
    win.draw_cell(cell4,"red")
    win.wait_for_close()
    print("Maze Solver")

if __name__ == "__main__":
    main()

    