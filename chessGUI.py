################################### Note #######################################
# In addition to the model and view files, many programs also keep a separate
# controller file to decouple behavioral aspects of a program from the logic
# (model) and presentation (view). This kind of structural segregation is named
# the model-view-controller (MVC) style of programming.

# However, our chess program has just one event to handle: mouse click for
# moving chess pieces. Creating a separate controller for just one event can
# make the program more complex than it should be.

# Given this limitation, we will handle the presentation (view) and event
# handling (controller) from a single class named GUI.
################################################################################

import tkinter
from tkinter import *
# We first create a GUI class and assign attributes such as rows, columns,
# colors of squares, and the dimension of each square in pixels. We initialize
# our GUI class to create the canvas on which we will draw our chessboard, as
# follows
class GUI():
    """
    We create the 'GUI' class to handle the rendering of our view files.
    """
    rows = 8
    columns = 8
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    dim_square = 64     # square dimensionality of chess board (8x8 = 64)

    # The init method sets up a Canvas widget of the required size which
    # will act as our container for all objects, such as chess square areas and
    # eventually the chess pieces.
    def __init__(self, parent):
        self.parent = parent
        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = Canvas(parent, width=canvas_width, height=canvas_height,
                             background="grey")

        # We have used the Canvas widget as a container, because it provides us the
        # ability to handle tasks based on precise location coordinates of events,
        # such as a click of the mouse button.
        self.canvas.pack(padx=8, pady=8)

        # The init method then calls the draw_board() method, which is
        # responsible for creating square blocks of alternating colors similar
        # to a chessboard.
        self.drawBoard()

    # Now, we draw the squares on the chessboard using the
    # canvas.create_rectangle method, filling it by alternating between the two
    # colors we defined earlier.
    def drawBoard(self):
        color = self.color2
        for r in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2     # alternating between two colors
            for c in range(self.columns):
                x1 = (c * self.dim_square)
                y1 = ((7-r) * self.dim_square)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                # To draw squares on the board we use the
                # canvas.create_rectangle() method, which draws a rectangle
                # given the x, y coordinates for the two diagonally opposite
                # corners of the rectangle (coordinates of upper-left and
                # lower-right edges).

                # We will need to target the board. We, therefore, add a tag
                # named area to each of the squares created on the board.
                # This is similar to tagging of the text widget, as we had
                # done in our text editor program.
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="area")
                color = self.color1 if color == self.color2 else self.color2

# Creating tkinter mainloop as follows:
def main():
    root = Tk()
    root.title("Chess")
    gui = GUI(root)
    root.mainloop()
# Outside the class, we have a main method that sets the Toplevel window,
# starts Tkinter mainloop, instantiates a GUI object, and calls the
# drawboard() method.
if __name__ == "__main__":
    main()
