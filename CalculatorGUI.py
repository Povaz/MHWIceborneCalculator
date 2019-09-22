from tkinter import *

# Monster Parameters
elemweak = 0.25
rawweak = 0.7

# Weapon Parameters
motionvalues = []
bloaters = []
current_motionvalue = 0.0
current_bloater = 1


def damageoutput(motionvalue, bloater, rawdam_entry, elemdam_entry, rawsharp_entry, elemsharp_entry, aff_entry, rawtruedam, elemtruedam, truedam):
    rawdam_value = float(rawdam_entry.get())
    elemdam_value = float(elemdam_entry.get())
    rawsharp_value = float(rawsharp_entry.get())
    elemsharp_value = float(elemsharp_entry.get())
    aff_value = float(aff_entry.get())

    if aff_value < 0.0:
        critdamage = 0.75
        aff_value = - aff_value
    else:
        critdamage = 1.25

    affinity_multiplier = ((1 - aff_value) + aff_value * critdamage)
    phystotal = (rawdam_value * affinity_multiplier * rawsharp_value * motionvalue * rawweak) / bloater
    elemtotal = (elemdam_value * elemsharp_value * motionvalue * elemweak) / bloater
    truedamage = phystotal + elemtotal

    rawtruedam.set(str(round(phystotal, 2)))
    elemtruedam.set(str(round(elemtotal, 2)))
    truedam.set(str(round(truedamage, 2)))


def setweapon(tickboxes, i):
    for j in range(len(tickboxes)):
        if j != i:
            tickboxes[j].set(False)
        else:
            global current_motionvalue
            current_motionvalue = motionvalues[i]
            global current_bloater
            current_bloater = bloaters[i]
    print(current_bloater)
    print(current_motionvalue)


def managerightframe():
    rawdam = DoubleVar()
    rawdam_label = Label(rightframe, text="Raw Damage Value: ")
    rawdam_label.grid(row=0, column=0)
    rawdam_entry = Entry(rightframe, textvariable=rawdam)
    rawdam_entry.grid(row=0, column=1)

    elemdam = DoubleVar()
    elemdam_label = Label(rightframe, text="Elemental Damage Value: ")
    elemdam_label.grid(row=1, column=0)
    elemdam_entry = Entry(rightframe, textvariable=elemdam)
    elemdam_entry.grid(row=1, column=1)

    rawsharp = DoubleVar()
    rawsharp_label = Label(rightframe, text="Physical Sharpness Factor: ")
    rawsharp_label.grid(row=2, column=0)
    rawsharp_entry = Entry(rightframe, textvariable=rawsharp)
    rawsharp_entry.grid(row=2, column=1)

    elemsharp = DoubleVar()
    elemsharp_label = Label(rightframe, text="Elemental Sharpness Factor: ")
    elemsharp_label.grid(row=3, column=0)
    elemsharp_entry = Entry(rightframe, textvariable=elemsharp)
    elemsharp_entry.grid(row=3, column=1)

    aff = DoubleVar()
    aff_label = Label(rightframe, text="Affinity Factor: ")
    aff_label.grid(row=4, column=0)
    aff_entry = Entry(rightframe, textvariable=aff)
    aff_entry.grid(row=4, column=1)

    button_calc = Button(rightframe,
                         text='Calculate You Lil Shit',
                         command=lambda: damageoutput(current_motionvalue, current_bloater, rawdam_entry,
                                                      elemdam_entry, rawsharp_entry, elemsharp_entry,
                                                      aff_entry, rawtruedam, elemtruedam, truedam))
    button_calc.grid(columnspan=2)

    rawtruedam = DoubleVar()
    rawtruedam_label = Label(rightframe, text="Physical True Damage: ")
    rawtruedam_label.grid(row=6, column=0)
    rawtruedam_entry = Entry(rightframe, textvariable=rawtruedam)
    rawtruedam_entry.grid(row=6, column=1)

    elemtruedam = DoubleVar()
    elemtruedam_label = Label(rightframe, text="Elemental True Damage: ")
    elemtruedam_label.grid(row=7, column=0)
    elemtruedam_entry = Entry(rightframe, textvariable=elemtruedam)
    elemtruedam_entry.grid(row=7, column=1)

    truedam = DoubleVar()
    truedam_label = Label(rightframe, text="Total True Damage: ")
    truedam_label.grid(row=8, column=0)
    truedam_entry = Entry(rightframe, textvariable=truedam)
    truedam_entry.grid(row=8, column=1)


def manageleftframe():
    tickbox = []

    # Dual Blades: Index 0
    tickbox.append(BooleanVar())
    check_db = Checkbutton(leftframe, text="Dual Blades", var=tickbox[0], command=lambda: setweapon(tickbox, 0))
    check_db.grid(row=0, column=0)

    # Hammer: Index 1
    tickbox.append(BooleanVar())
    check_hm = Checkbutton(leftframe, text="Hammer", var=tickbox[1], command=lambda: setweapon(tickbox, 1))
    check_hm.grid(row=0, column=1)


# TODO: Needs to be moved in a file soon
def gatherdata():
    # Dual Blades: Index 0
    motionvalues.append(0.19)
    bloaters.append(1.4)

    # Hammer: Index 1
    motionvalues.append(0.2)
    bloaters.append(5.2)


gatherdata()
window = Tk()
window.title("Monster Hunter World: Iceborne Calculator")

leftframe = Frame(window)
leftframe.pack(side=LEFT)
manageleftframe()

rightframe = Frame(window)
rightframe.pack(side=RIGHT)
managerightframe()

window.mainloop()
