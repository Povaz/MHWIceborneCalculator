from tkinter import *

# Monster Parameters
elemweak = 0.25
rawweak = 0.7


def damageoutput(motionvalue, bloater):

    rawdam_value = float(rawdam_entry.get())
    elemdam_value = float(elemsharp_entry.get())
    rawsharp_value = float(rawsharp_entry.get())
    elemsharp_value = float(elemsharp_entry.get())
    aff_value = float(aff_entry.get())

    if aff_value < 0.0:
        critdamage = 0.75
        aff_value = - aff_value
    else:
        critdamage = 1.25

    affinity_multiplier = ((1 - aff_value) + aff_value * critdamage)
    phystotal = rawdam_value * affinity_multiplier * rawsharp_value * motionvalue * rawweak
    elemtotal = elemdam_value * elemsharp_value * motionvalue * elemweak
    outputdamage = phystotal + elemtotal
    truedamage = outputdamage/bloater

    truedam.set(str(round(truedamage, 2)))


window = Tk()
window.title("Monster Hunter World: Iceborne Calculator")

rawdam = DoubleVar()
rawdam_label = Label(window, text="Raw Damage Value: ")
rawdam_label.grid(row=0, column=0)
rawdam_entry = Entry(window, textvariable=rawdam)
rawdam_entry.grid(row=0, column=1)

elemdam = DoubleVar()
elemdam_label = Label(window, text="Elemental Damage Value: ")
elemdam_label.grid(row=1, column=0)
elemdam_entry = Entry(window, textvariable=elemdam)
elemdam_entry.grid(row=1, column=1)

rawsharp = DoubleVar()
rawsharp_label = Label(window, text="Physical Sharpness Factor: ")
rawsharp_label.grid(row=2, column=0)
rawsharp_entry = Entry(window, textvariable=rawsharp)
rawsharp_entry.grid(row=2, column=1)

elemsharp = DoubleVar()
elemsharp_label = Label(window, text="Elemental Sharpness Factor: ")
elemsharp_label.grid(row=3, column=0)
elemsharp_entry = Entry(window, textvariable=elemsharp)
elemsharp_entry.grid(row=3, column=1)

aff = DoubleVar()
aff_label = Label(window, text="Affinity Factor: ")
aff_label.grid(row=4, column=0)
aff_entry = Entry(window, textvariable=aff)
aff_entry.grid(row=4, column=1)

button_calc = Button(window, text='Calculate You Lil Shit', command=lambda: damageoutput(0.19, 1.4))
button_calc.grid(columnspan=2)

truedam = DoubleVar()
truedam_label = Label(window, text="True Damage: ")
truedam_label.grid(row=6, column=0)
truedam_entry = Entry(window, textvariable=truedam)
truedam_entry.grid(row=6, column=1)

window.mainloop()
