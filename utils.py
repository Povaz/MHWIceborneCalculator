from tkinter import *


# Creates a colored Button in containerWidget, at position (row, column) of the Grid with sticky option
# and returns the reference to that button:
def create_colored_buttongrid(containerwidget, row, column, color, sticky):
    button = Button(containerwidget, bg=color)
    button.grid(row=row, column=column, sticky=sticky)
    return button


# Create a Checkbox in containerWidget, at position (row, column) of the Grid with text 'text'
def create_checkboxgrid(containerwidget, row, column, text):
    variable = BooleanVar()
    variable.set(False)
    checkbox = Checkbutton(containerwidget, text=text, var=variable)
    checkbox.grid(row=row, column=column)
    return checkbox, variable
