from tkinter import *


# Creates a colored Button in containerWidget, at position (row, column) of the Grid with sticky option
# and returns the reference to that button:
def create_coloredbutton_grid(containerwidget, row, column, color, sticky):
    button = Button(containerwidget, bg=color)
    button.grid(row=row, column=column, sticky=sticky)
    return button


# Creates a Button in containerwidght, at position (row,column) of the Grid, with height 'button_height' and
# width 'button_width' and with a resized image 'image'
def create_imagebutton_grid(containerwidget, image, button_height, button_width, pad, row, column):
    image = image.subsample(image.height() // button_height, image.width() // button_width)
    button = Button(containerwidget, image=image)
    button.image = image
    button.grid(row=row, column=column, padx=pad, pady=pad)
    button.config(height=button_height, width=button_width)
    return button


# Creates a Checkbox in containerWidget, at position (row, column) of the Grid with text 'text'
def create_checkbox_grid(containerwidget, row, column, text):
    variable = BooleanVar()
    variable.set(False)
    checkbox = Checkbutton(containerwidget, text=text, var=variable)
    checkbox.grid(row=row, column=column)
    return checkbox, variable


# Creates a couple Label,Entry in containerWidget, in positions (row,column) and (row, column+columnspan)
# respectively, with Label Text 'text' and Entry Variable 'entryvar'
def create_labelentry_grid(containerwidget, row, column, columnspan, entryvar, text):
    label = Label(containerwidget, text=text)
    label.grid(row=row, column=column, columnspan=3)
    entry = Entry(containerwidget, textvariable=entryvar)
    entry.grid(row=row, column=column+columnspan, columnspan=3)
    return entry


# Generates a list of even numbers from 0 to n:
def even_numbers(n):
    temp = [i for i in range(n)]
    return [i for i in temp if i % 2 == 0]
