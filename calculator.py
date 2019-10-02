from tkinter import *
from tkinter import ttk
import globals
import utils
import engine


def managecenterframe():

    adjustcentergrid()

    rawdam = DoubleVar()
    elemdam = DoubleVar()
    rawsharp = DoubleVar()
    elemsharp = DoubleVar()
    rawdam_entry = utils.create_labelentrygrid(centerframe, 0, 0, 3, rawdam, "Raw Damage Value: ")
    elemdam_entry = utils.create_labelentrygrid(centerframe, 1, 0, 3, elemdam, "Elemental Damage Value: ")
    rawsharp_entry = utils.create_labelentrygrid(centerframe, 2, 0, 3, rawsharp, "Physical Sharpness Factor: ")
    elemsharp_entry = utils.create_labelentrygrid(centerframe, 3, 0, 3, elemsharp, "Elemental Sharpness Factor: ")

    sharpnessbuttons(rawsharp, elemsharp, 4)

    aff = DoubleVar()
    aff_entry = utils.create_labelentrygrid(centerframe, 5, 0, 3, aff, "Affinity Factor: ")

    button_calc = Button(centerframe,
                         text='Calculate You Lil Shit',
                         command=lambda: engine.damageoutput(globals.current_motionvalue, globals.current_bloater,
                                                             rawdam_entry, elemdam_entry, rawsharp_entry,
                                                             elemsharp_entry, aff_entry, rawtruedam, elemtruedam,
                                                             truedam))
    button_calc.grid(row=6, column=1, columnspan=4)

    rawtruedam = DoubleVar()
    elemtruedam = DoubleVar()
    truedam = DoubleVar()
    utils.create_labelentrygrid(centerframe, 7, 0, 3, rawtruedam, "Physical True Damage: ")
    utils.create_labelentrygrid(centerframe, 8, 0, 3, rawtruedam, "Elemental True Damage: ")
    utils.create_labelentrygrid(centerframe, 9, 0, 3, rawtruedam, "Total True Damage: ")


def sharpnessbuttons(rawsharp, elemsharp, row):
    colors = ['purple', 'white', 'blue', 'green', 'yellow', 'orange', 'red']
    sharpbuttons = []

    for i in range(7):
        button = utils.create_colored_buttongrid(centerframe, row, i, colors[i], sticky=N + S + E + W)
        sharpbuttons.append(button)
        sharpbuttons[i].config(command=engine.lambda_setsharpness(i, rawsharp, elemsharp))


def adjustcentergrid():
    index = 0
    while index < 10:
        centerframe.rowconfigure(index, weight=1)
        index += 1

    index = 0
    while index < 6:
        centerframe.columnconfigure(index, weight=1, minsize=50)
        index += 1


def manageleftframe():
    row = 0
    tickbox = []
    checkbox = []
    weapon_count = len(globals.weapondatastructure)
    for i in range(weapon_count):
        if i % 2 == 0:
            row = i
            column = 0
        else:
            column = 1

        tickbox.append(BooleanVar())
        cb = Checkbutton(leftframe, text=globals.weapondatastructure.get(i)[2], var=tickbox[i])
        cb.grid(row=row, column=column, sticky=W)
        checkbox.append(cb)
        checkbox[i].config(command=engine.lambda_setweapon(tickbox, i))

        namelist = globals.weapondatastructure.get(i)[0]['Name'].tolist()
        globals.weapondatastructure.get(i)[1] = ttk.Combobox(leftframe, values=namelist, state='disabled', width=35)
        globals.weapondatastructure.get(i)[1].grid(row=row + 1, column=column, sticky=W)
        globals.weapondatastructure.get(i)[1].current(0)
        globals.weapondatastructure.get(i)[1].bind("<<ComboboxSelected>>", engine.callback)


def managerightframe():
    criticalboost()
    criticalelement()
    criticaleye()


def criticalboost():
    checkboxes = []
    variables = []
    levels = 3
    label = Label(rightframe, text="Critical Boost:")
    label.grid(row=0, column=0)

    for i in range(levels):
        result = utils.create_checkboxgrid(rightframe, 0, i+1, "Lv" + str(i+1))
        checkboxes.append(result[0])
        variables.append(result[1])
        checkboxes[i].config(command=engine.lambda_apply_criticalboost(variables, i))


def criticalelement():
    label = Label(rightframe, text="Critical Element:")
    label.grid(row=1, column=0)
    result = utils.create_checkboxgrid(rightframe, 1, 1, "Lv" + str(1))
    result[0].config(command=lambda: engine.apply_criticalelement(result[1]))


def criticaleye():
    checkboxes = []
    variables = []
    levels = 7
    label = Label(rightframe, text="Critical Eye:")
    label.grid(row=3, column=0)

    for i in range(levels):
        result = utils.create_checkboxgrid(rightframe, 3, i+1, "Lv" + str(i+1))
        checkboxes.append(result[0])
        variables.append(result[1])
        checkboxes[i].config(command=engine.lambda_apply_criticaleye(variables, i))


window = Tk()
window.title("Monster Hunter World: Iceborne Calculator")

globals.setdata()

leftframe = LabelFrame(window, text="Weapon Choice")
leftframe.grid(row=0, column=0)
manageleftframe()

centerframe = LabelFrame(window, text="Weapon Stats")
centerframe.grid(row=0, column=1)
managecenterframe()

rightframe = LabelFrame(window, text="Skills")
rightframe.grid(row=0, column=2)
managerightframe()

window.mainloop()
