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


def sharpnessbuttons():
    row = 9
    column = 0

    purplebutton = Button(rightframe, bg='purple')
    purplebutton.grid(row=row, column=column, sticky=N+S+E+W)

    whitebutton = Button(rightframe, bg='white')
    whitebutton.grid(row=row, column=column+1, sticky=N+S+E+W)

    bluebutton = Button(rightframe, bg='blue')
    bluebutton.grid(row=row, column=column+2, sticky=N+S+E+W)

    greenbutton = Button(rightframe, bg='green')
    greenbutton.grid(row=row, column=column+3, sticky=N+S+E+W)

    yellowbutton = Button(rightframe, bg='yellow')
    yellowbutton.grid(row=row, column=column+4, sticky=N+S+E+W)

    redbutton = Button(rightframe, bg='red')
    redbutton.grid(row=row, column=column+5, sticky=N+S+E+W)


def managerightframe():


    rawdam = DoubleVar()
    rawdam_label = Label(rightframe, text="Raw Damage Value: ")
    rawdam_label.grid(row=0, column=0, columnspan=3)
    rawdam_entry = Entry(rightframe, textvariable=rawdam)
    rawdam_entry.grid(row=0, column=3, columnspan=3)

    elemdam = DoubleVar()
    elemdam_label = Label(rightframe, text="Elemental Damage Value: ")
    elemdam_label.grid(row=1, column=0, columnspan=3)
    elemdam_entry = Entry(rightframe, textvariable=elemdam)
    elemdam_entry.grid(row=1, column=3, columnspan=3)

    rawsharp = DoubleVar()
    rawsharp_label = Label(rightframe, text="Physical Sharpness Factor: ")
    rawsharp_label.grid(row=2, column=0, columnspan=3)
    rawsharp_entry = Entry(rightframe, textvariable=rawsharp)
    rawsharp_entry.grid(row=2, column=3, columnspan=3)

    elemsharp = DoubleVar()
    elemsharp_label = Label(rightframe, text="Elemental Sharpness Factor: ")
    elemsharp_label.grid(row=3, column=0, columnspan=3)
    elemsharp_entry = Entry(rightframe, textvariable=elemsharp)
    elemsharp_entry.grid(row=3, column=3, columnspan=3)

    sharpnessbuttons()

    aff = DoubleVar()
    aff_label = Label(rightframe, text="Affinity Factor: ")
    aff_label.grid(row=4, column=0, columnspan=3)
    aff_entry = Entry(rightframe, textvariable=aff)
    aff_entry.grid(row=4, column=3, columnspan=3)

    button_calc = Button(rightframe,
                         text='Calculate You Lil Shit',
                         command=lambda: damageoutput(current_motionvalue, current_bloater, rawdam_entry,
                                                      elemdam_entry, rawsharp_entry, elemsharp_entry,
                                                      aff_entry, rawtruedam, elemtruedam, truedam))
    button_calc.grid(row=5, column=1, columnspan=4)

    rawtruedam = DoubleVar()
    rawtruedam_label = Label(rightframe, text="Physical True Damage: ")
    rawtruedam_label.grid(row=6, column=0, columnspan=3)
    rawtruedam_entry = Entry(rightframe, textvariable=rawtruedam)
    rawtruedam_entry.grid(row=6, column=3, columnspan=3)

    elemtruedam = DoubleVar()
    elemtruedam_label = Label(rightframe, text="Elemental True Damage: ")
    elemtruedam_label.grid(row=7, column=0, columnspan=3)
    elemtruedam_entry = Entry(rightframe, textvariable=elemtruedam)
    elemtruedam_entry.grid(row=7, column=3, columnspan=3)

    truedam = DoubleVar()
    truedam_label = Label(rightframe, text="Total True Damage: ")
    truedam_label.grid(row=8, column=0, columnspan=3)
    truedam_entry = Entry(rightframe, textvariable=truedam)
    truedam_entry.grid(row=8, column=3, columnspan=3)


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

leftframe = LabelFrame(window, text="Weapon Choice")
leftframe.pack(side=LEFT)
manageleftframe()

rightframe = LabelFrame(window, text="Weapon Stats")
rightframe.pack(side=RIGHT)
index = 0
while index < 10:
    rightframe.rowconfigure(index, weight=1)
    index += 1

index = 0
while index < 6:
    rightframe.columnconfigure(index, weight=1, minsize=50)
    index += 1

managerightframe()

window.mainloop()
