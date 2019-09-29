from tkinter import *
import utils

# Monster Parameters
elemweak = 0.25
rawweak = 0.7

# Weapon Parameters
motionvalues = []
bloaters = []
crit_elems = []
current_motionvalue = 0.0
current_bloater = 1.00
current_rawsharp = 0.0
current_elemsharp = 0.0
current_critelem = 1.00

# Skills Parameters
criticalboost_value = 0.0
criticalelement_active = False
criticaleye_value = 0.0


def managecenterframe():

    adjustcentergrid()

    rawdam = DoubleVar()
    rawdam_label = Label(centerframe, text="Raw Damage Value: ")
    rawdam_label.grid(row=0, column=0, columnspan=3)
    rawdam_entry = Entry(centerframe, textvariable=rawdam)
    rawdam_entry.grid(row=0, column=3, columnspan=3)

    elemdam = DoubleVar()
    elemdam_label = Label(centerframe, text="Elemental Damage Value: ")
    elemdam_label.grid(row=1, column=0, columnspan=3)
    elemdam_entry = Entry(centerframe, textvariable=elemdam)
    elemdam_entry.grid(row=1, column=3, columnspan=3)

    rawsharp = DoubleVar()
    rawsharp_label = Label(centerframe, text="Physical Sharpness Factor: ")
    rawsharp_label.grid(row=2, column=0, columnspan=3)
    rawsharp_entry = Entry(centerframe, textvariable=rawsharp)
    rawsharp_entry.grid(row=2, column=3, columnspan=3)

    elemsharp = DoubleVar()
    elemsharp_label = Label(centerframe, text="Elemental Sharpness Factor: ")
    elemsharp_label.grid(row=3, column=0, columnspan=3)
    elemsharp_entry = Entry(centerframe, textvariable=elemsharp)
    elemsharp_entry.grid(row=3, column=3, columnspan=3)

    sharpnessbuttons(rawsharp, elemsharp, 4)

    aff = DoubleVar()
    aff_label = Label(centerframe, text="Affinity Factor: ")
    aff_label.grid(row=5, column=0, columnspan=3)
    aff_entry = Entry(centerframe, textvariable=aff)
    aff_entry.grid(row=5, column=3, columnspan=3)

    button_calc = Button(centerframe,
                         text='Calculate You Lil Shit',
                         command=lambda: damageoutput(current_motionvalue, current_bloater, rawdam_entry,
                                                      elemdam_entry, rawsharp_entry, elemsharp_entry,
                                                      aff_entry, rawtruedam, elemtruedam, truedam))
    button_calc.grid(row=6, column=1, columnspan=4)

    rawtruedam = DoubleVar()
    rawtruedam_label = Label(centerframe, text="Physical True Damage: ")
    rawtruedam_label.grid(row=7, column=0, columnspan=3)
    rawtruedam_entry = Entry(centerframe, textvariable=rawtruedam)
    rawtruedam_entry.grid(row=7, column=3, columnspan=3)

    elemtruedam = DoubleVar()
    elemtruedam_label = Label(centerframe, text="Elemental True Damage: ")
    elemtruedam_label.grid(row=8, column=0, columnspan=3)
    elemtruedam_entry = Entry(centerframe, textvariable=elemtruedam)
    elemtruedam_entry.grid(row=8, column=3, columnspan=3)

    truedam = DoubleVar()
    truedam_label = Label(centerframe, text="Total True Damage: ")
    truedam_label.grid(row=9, column=0, columnspan=3)
    truedam_entry = Entry(centerframe, textvariable=truedam)
    truedam_entry.grid(row=9, column=3, columnspan=3)


def damageoutput(motionvalue, bloater, rawdam_entry, elemdam_entry, rawsharp_entry, elemsharp_entry, aff_entry, rawtruedam, elemtruedam, truedam):
    rawdam_value = float(rawdam_entry.get())
    elemdam_value = float(elemdam_entry.get())
    rawsharp_value = float(rawsharp_entry.get())
    elemsharp_value = float(elemsharp_entry.get())
    aff_value = float(aff_entry.get())

    aff_value = aff_value + criticaleye_value

    if aff_value < 0.0:
        critdamage = 0.75 + criticalboost_value
        aff_value = - aff_value
    else:
        critdamage = 1.25 + criticalboost_value

    affinity_multiplier = ((1 - aff_value) + aff_value * critdamage)

    if criticalelement_active:
        elemental_affinity = ((1 - aff_value) + aff_value * current_critelem)
    else:
        elemental_affinity = 1

    phystotal = (rawdam_value * affinity_multiplier * rawsharp_value * motionvalue * rawweak) / bloater
    elemtotal = (elemdam_value * elemental_affinity * elemsharp_value * motionvalue * elemweak) / bloater
    truedamage = phystotal + elemtotal

    rawtruedam.set(str(round(phystotal, 4)))
    elemtruedam.set(str(round(elemtotal, 4)))
    truedam.set(str(round(truedamage, 4)))


def setsharpness(color, rawsharp, elemsharp):
    sharpvalues = [[1.39, 1.25], [1.32, 1.125], [1.2, 1.0625],
                   [1.05, 1], [1.00, 0.75], [0.75, 0.50], [0.50, 0.25]]
    for i in range(7):
        if i == color:
            print(color)
            print(i)
            rawsharp.set(str(sharpvalues[i][0]))
            elemsharp.set(str(sharpvalues[i][1]))


def sharpnessbuttons(rawsharp, elemsharp, row):
    color = ['purple', 'white', 'blue', 'green', 'yellow', 'orange', 'red']
    sharpbuttons = []

    for i in range(7):
        button = utils.create_colored_buttongrid(centerframe, row, i, color[i], sticky=N + S + E + W)
        sharpbuttons.append(button)

    sharpbuttons[0].config(command=lambda: setsharpness(0, rawsharp, elemsharp))
    sharpbuttons[1].config(command=lambda: setsharpness(1, rawsharp, elemsharp))
    sharpbuttons[2].config(command=lambda: setsharpness(2, rawsharp, elemsharp))
    sharpbuttons[3].config(command=lambda: setsharpness(3, rawsharp, elemsharp))
    sharpbuttons[4].config(command=lambda: setsharpness(4, rawsharp, elemsharp))
    sharpbuttons[5].config(command=lambda: setsharpness(5, rawsharp, elemsharp))
    sharpbuttons[6].config(command=lambda: setsharpness(6, rawsharp, elemsharp))


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
    tickbox = []

    # Dual Blades: Index 0
    tickbox.append(BooleanVar())
    check_db = Checkbutton(leftframe, text="Dual Blades", var=tickbox[0], command=lambda: setweapon(tickbox, 0))
    check_db.grid(row=0, column=0, sticky=W)

    # Hammer: Index 1
    tickbox.append(BooleanVar())
    check_hm = Checkbutton(leftframe, text="Hammer", var=tickbox[1], command=lambda: setweapon(tickbox, 1))
    check_hm.grid(row=0, column=1, sticky=W)

    # Bow: Index 2
    tickbox.append(BooleanVar())
    check_hm = Checkbutton(leftframe, text="Bow", var=tickbox[2], command=lambda: setweapon(tickbox, 2))
    check_hm.grid(row=1, column=0, sticky=W)


def setweapon(tickboxes, i):
    for j in range(len(tickboxes)):
        if j != i:
            tickboxes[j].set(False)
        else:
            global current_motionvalue
            current_motionvalue = motionvalues[i]
            global current_bloater
            current_bloater = bloaters[i]
            global current_critelem
            current_critelem = crit_elems[i]


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

    checkboxes[0].config(command=lambda: apply_criticalboost(variables, 0))
    checkboxes[1].config(command=lambda: apply_criticalboost(variables, 1))
    checkboxes[2].config(command=lambda: apply_criticalboost(variables, 2))


def apply_criticalboost(variables, i):
    global criticalboost_value
    lenght = len(variables)
    for j in range(lenght):
        if j != i:
            variables[j].set(False)
        else:
            if variables[j].get():
                print('Set Critical Boost to lv ' + str(j+1))
                criticalboost_value = 0.05*(j+1)
            else:
                print('Reset Critical Boost')
                criticalboost_value = 0.0
                variables[j].set(False)


def criticalelement():
    label = Label(rightframe, text="Critical Element:")
    label.grid(row=1, column=0)

    result = utils.create_checkboxgrid(rightframe, 1, 1, "Lv" + str(1))

    result[0].config(command=lambda: apply_criticalelement(result[1]))


def apply_criticalelement(variable):
    global criticalelement_active
    if variable.get():
        variable.set(True)
        print("Checkbox is: " + str(variable.get()))
        criticalelement_active = True
    else:
        variable.set(False)
        print("Checkbox is: " + str(variable.get()))
        criticalelement_active = False


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

    checkboxes[0].config(command=lambda: apply_criticaleye(variables, 0))
    checkboxes[1].config(command=lambda: apply_criticaleye(variables, 1))
    checkboxes[2].config(command=lambda: apply_criticaleye(variables, 2))
    checkboxes[3].config(command=lambda: apply_criticaleye(variables, 3))
    checkboxes[4].config(command=lambda: apply_criticaleye(variables, 4))
    checkboxes[5].config(command=lambda: apply_criticaleye(variables, 5))
    checkboxes[6].config(command=lambda: apply_criticaleye(variables, 6))


def apply_criticaleye(variables, i):
    global criticaleye_value
    lenght = len(variables)
    for j in range(lenght):
        if j != i:
            variables[j].set(False)
        else:
            if variables[j].get():
                print('Set Critical Eye to lv ' + str(j + 1))
                criticaleye_value = 0.05 * (j + 1)
                if i == 6:
                    criticaleye_value = criticaleye_value + 0.05
            else:
                print('Reset Critical Boost')
                criticaleye_value = 0.0
                variables[j].set(False)


# TODO: Needs to be moved in a file
def gatherdata():
    # Dual Blades: Index 0
    motionvalues.append(0.19)
    bloaters.append(1.4)
    crit_elems.append(1.35)

    # Hammer: Index 1
    motionvalues.append(0.2)
    bloaters.append(5.2)
    crit_elems.append(1.25)

    # Bow: Index 2
    motionvalues.append(0.08)
    bloaters.append(1.2)
    crit_elems.append(1.35)


gatherdata()
window = Tk()
window.title("Monster Hunter World: Iceborne Calculator")

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
