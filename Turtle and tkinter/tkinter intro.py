import turtle
import tkinter as tk


class App:
    def do_stuff(self):
        for color in ["red", "yellow", "green"]:
            self.my_lovely_turtle.color(color)
            self.my_lovely_turtle.right(120)

    def press(self):
        self.do_stuff()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
