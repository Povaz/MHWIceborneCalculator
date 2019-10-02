from tkinter import *


# Creates a colored Button in containerWidget, at position (row, column) of the Grid with sticky option
# and returns the reference to that button:
def create_colored_buttongrid(containerwidget, row, column, color, sticky):
    button = Button(containerwidget, bg=color)
    button.grid(row=row, column=column, sticky=sticky)
    return button


# Creates a Checkbox in containerWidget, at position (row, column) of the Grid with text 'text'
def create_checkboxgrid(containerwidget, row, column, text):
    variable = BooleanVar()
    variable.set(False)
    checkbox = Checkbutton(containerwidget, text=text, var=variable)
    checkbox.grid(row=row, column=column)
    return checkbox, variable


# Creates a couple Label,Entry in containerWidget, in positions (row,column) and (row, column+columnspan)
# respectively, with Label Text 'text' and Entry Variable 'entryvar'
def create_labelentrygrid(containerwidget, row, column, columnspan, entryvar, text):
    label = Label(containerwidget, text=text)
    label.grid(row=row, column=column, columnspan=3)
    entry = Entry(containerwidget, textvariable=entryvar)
    entry.grid(row=row, column=column+columnspan, columnspan=3)
    return entry


# Generates a list of even numbers from 0 to n:
def even_numbers(n):
    temp = [i for i in range(n)]
    return [i for i in temp if i % 2 == 0]
