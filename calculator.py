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
    rawdam_entry = utils.create_labelentry_grid(centerframe, 0, 0, 3, rawdam, "Raw Damage Value: ")
    elemdam_entry = utils.create_labelentry_grid(centerframe, 1, 0, 3, elemdam, "Elemental Damage Value: ")

    elementalbuttons()

    rawsharp_entry = utils.create_labelentry_grid(centerframe, 3, 0, 3, rawsharp, "Physical Sharpness Factor: ")
    elemsharp_entry = utils.create_labelentry_grid(centerframe, 4, 0, 3, elemsharp, "Elemental Sharpness Factor: ")

    sharpnessbuttons(rawsharp, elemsharp, 5)

    aff = DoubleVar()
    aff_entry = utils.create_labelentry_grid(centerframe, 6, 0, 3, aff, "Affinity Factor: ")

    button_calc = Button(centerframe,
                         text='Calculate You Lil Shit',
                         command=lambda: engine.damageoutput(globals.current_motionvalue, globals.current_bloater,
                                                             rawdam_entry, elemdam_entry, rawsharp_entry,
                                                             elemsharp_entry, aff_entry, rawtruedam, elemtruedam,
                                                             truedam))
    button_calc.grid(row=7, column=1, columnspan=4)

    rawtruedam = DoubleVar()
    elemtruedam = DoubleVar()
    truedam = DoubleVar()
    utils.create_labelentry_grid(centerframe, 8, 0, 3, rawtruedam, "Physical True Damage: ")
    utils.create_labelentry_grid(centerframe, 9, 0, 3, elemtruedam, "Elemental True Damage: ")
    utils.create_labelentry_grid(centerframe, 10, 0, 3, truedam, "Total True Damage: ")


def elementalbuttons():
    fire_logo = PhotoImage(file='./files/elements/fire_logo.png')
    water_logo = PhotoImage(file='./files/elements/water_logo.png')
    thunder_logo = PhotoImage(file='./files/elements/thunder_logo.png')
    ice_logo = PhotoImage(file='./files/elements/ice_logo.png')
    dragon_logo = PhotoImage(file='./files/elements/dragon_logo.png')

    logos = [fire_logo, water_logo, thunder_logo, ice_logo, dragon_logo]
    elements = ['Fire', 'Water', 'Thunder', 'Ice', 'Dragon']
    elembuttons = []
    for i in range(len(logos)):
        button = utils.create_imagebutton_grid(centerframe, logos[i], 30, 30, 0, 2, i)
        elembuttons.append(button)
        elembuttons[i].config(command=engine.lambda_setelement(elements[i]))


def sharpnessbuttons(rawsharp, elemsharp, row):
    colors = ['purple', 'white', 'blue', 'green', 'yellow', 'orange', 'red']
    sharpbuttons = []

    for i in range(7):
        button = utils.create_coloredbutton_grid(centerframe, row, i, colors[i], sticky=N + S + E + W)
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
        globals.weapondatastructure.get(i)[1].bind("<<ComboboxSelected>>", engine.weapon_callback)


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
        result = utils.create_checkbox_grid(rightframe, 0, i + 1, "Lv" + str(i + 1))
        checkboxes.append(result[0])
        variables.append(result[1])
        checkboxes[i].config(command=engine.lambda_apply_criticalboost(variables, i))


def criticalelement():
    label = Label(rightframe, text="Critical Element:")
    label.grid(row=1, column=0)
    result = utils.create_checkbox_grid(rightframe, 1, 1, "Lv" + str(1))
    result[0].config(command=lambda: engine.apply_criticalelement(result[1]))


def criticaleye():
    checkboxes = []
    variables = []
    levels = 7
    label = Label(rightframe, text="Critical Eye:")
    label.grid(row=3, column=0)

    for i in range(levels):
        result = utils.create_checkbox_grid(rightframe, 3, i + 1, "Lv" + str(i + 1))
        checkboxes.append(result[0])
        variables.append(result[1])
        checkboxes[i].config(command=engine.lambda_apply_criticaleye(variables, i))


def manangebottomframe():
    columns = 5
    button_height = 100
    button_width = 100
    pad = 10
    monsterbuttons = []
    for key in globals.monsterdatastructure:
        button_row = (key // columns)*2
        combobox_row = (key // columns)*2 + 1
        column = key % columns
        image = globals.monsterdatastructure.get(key)[2]

        button = utils.create_imagebutton_grid(bottomframe, image, button_height, button_width, pad, button_row, column)
        monsterbuttons.append(button)
        monsterbuttons[key].config(command=engine.lambda_setmonster(monsterbuttons, key))

        namelist = globals.monsterdatastructure.get(key)[1]['Part'].tolist()
        globals.monsterdatastructure.get(key)[3] = ttk.Combobox(bottomframe, values=namelist, state='disabled', width=15)
        globals.monsterdatastructure.get(key)[3].grid(row=combobox_row, column=column, sticky=W, padx=pad)
        globals.monsterdatastructure.get(key)[3].current(0)
        globals.monsterdatastructure.get(key)[3].bind("<<ComboboxSelected>>", engine.monster_callback)


window = Tk()
window.title("Monster Hunter World: Iceborne Calculator")

globals.setweapondata()
globals.setmonsterdata()

leftframe = LabelFrame(window, text="Weapon Choice")
leftframe.grid(row=0, column=0)
manageleftframe()

centerframe = LabelFrame(window, text="Weapon Stats")
centerframe.grid(row=0, column=1)
managecenterframe()

rightframe = LabelFrame(window, text="Skills")
rightframe.grid(row=0, column=2)
managerightframe()

bottomframe = LabelFrame(window, text="Monsters")
bottomframe.grid(row=1, column=0, columnspan=3)
manangebottomframe()

window.mainloop()
