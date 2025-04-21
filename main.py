from window import Window
from line import Line
from point import Point


def main():
    win = Window(800, 600)
    lin1 = Line(Point(50,50), Point(100,100))
    win.draw_line(lin1,"red")
    win.wait_for_close()
    print("Maze Solver")

if __name__ == "__main__":
    main()

    