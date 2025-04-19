from tkinter import Tk, BOTH, Canvas
from tkinter import ttk

class Window():
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        root = Tk()
        root.title("Maze Solver")

        C = Canvas(root, bg="blue", height=250, width=300)

        C.pack()
        root.mainloop()


def main():
    wd = Window(100, 100)
    print("Maze Solver")

if __name__ == "__main__":
    main()

    