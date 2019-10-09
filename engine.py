import globals


def damageoutput(motionvalue, bloater, rawdam_entry, elemdam_entry, rawsharp_entry, elemsharp_entry, aff_entry,
                 rawtruedam, elemtruedam, truedam):
    rawdam_value = float(rawdam_entry.get())
    elemdam_value = float(elemdam_entry.get())
    rawsharp_value = float(rawsharp_entry.get())
    elemsharp_value = float(elemsharp_entry.get())
    aff_value = float(aff_entry.get())

    aff_value = aff_value + globals.criticaleye_value

    if aff_value < 0.0:
        critdamage = 0.75 + globals.criticalboost_value
        aff_value = - aff_value
    else:
        critdamage = 1.25 + globals.criticalboost_value

    affinity_multiplier = ((1 - aff_value) + aff_value * critdamage)

    if globals.criticalelement_active:
        elemental_affinity = ((1 - aff_value) + aff_value * globals.current_critelem)
    else:
        elemental_affinity = 1

    phystotal = (rawdam_value * affinity_multiplier * rawsharp_value * motionvalue * globals.rawweak) / bloater
    elemtotal = ((elemdam_value/10) * elemental_affinity * elemsharp_value * (1 + globals.elemweak))
    truedamage = phystotal + elemtotal

    rawtruedam.set(str(round(phystotal, 4)))
    elemtruedam.set(str(round(elemtotal, 4)))
    truedam.set(str(round(truedamage, 4)))


def lambda_setsharpness(color, rawsharp, elemsharp):
    return lambda: setsharpness(color, rawsharp, elemsharp)


def setsharpness(color, rawsharp, elemsharp):
    for i in range(7):
        if i == color:
            rawsharp.set(str(globals.sharpvalues[i][0]))
            elemsharp.set(str(globals.sharpvalues[i][1]))


def fetch_mv(attackname, attackdata):
    temp = attackdata.loc[attackdata['Name'] == attackname]
    mv = temp.iloc[:, 1:].sum(1)
    return mv.item() / 100


def fetch_first_mv(weapon):
    weapondata = globals.weapondatastructure.get(weapon)[0]
    temp = weapondata.iloc[0, :]
    mv = temp.iloc[1:].sum()
    return mv.item() / 100


def lambda_apply_criticalboost(variables, i):
    return lambda: apply_criticalboost(variables, i)


def apply_criticalboost(variables, i):
    lenght = len(variables)
    for j in range(lenght):
        if j != i:
            variables[j].set(False)
        else:
            if variables[j].get():
                print('Set Critical Boost to lv ' + str(j+1))
                globals.criticalboost_value = 0.05*(j+1)
            else:
                print('Reset Critical Boost')
                globals.criticalboost_value = 0.0
                variables[j].set(False)


def apply_criticalelement(variable):
    if variable.get():
        variable.set(True)
        print("Critical Element is: " + str(variable.get()))
        globals.criticalelement_active = True
    else:
        variable.set(False)
        print("Critical Element is: " + str(variable.get()))
        globals.criticalelement_active = False


def lambda_apply_criticaleye(variables, i):
    return lambda: apply_criticaleye(variables, i)


def apply_criticaleye(variables, i):
    lenght = len(variables)
    for j in range(lenght):
        if j != i:
            variables[j].set(False)
        else:
            if variables[j].get():
                print('Set Critical Eye to lv ' + str(j + 1))
                globals.criticaleye_value = 0.05 * (j + 1)
                if i == 6:
                    globals.criticaleye_value = globals.criticaleye_value + 0.05
            else:
                print('Reset Critical Boost')
                globals.criticaleye_value = 0.0
                variables[j].set(False)


def lambda_setweapon(tickboxes, i):
    return lambda: setweapon(tickboxes, i)


def setweapon(tickboxes, i):
    for j in range(len(tickboxes)):
        if j != i:
            tickboxes[j].set(False)
            globals.weapondatastructure.get(j)[1].config(state='disabled')
        else:
            globals.current_weapon = i
            globals.current_motionvalue = globals.motionvalues[i]
            globals.current_bloater = globals.bloaters[i]
            globals.current_critelem = globals.crit_elems[i]
            if tickboxes[i].get():
                globals.weapondatastructure.get(i)[1].config(state='readonly')
            else:
                globals.weapondatastructure.get(i)[1].config(state='disabled')


def callback(eventObject):
    weapon = globals.current_weapon
    globals.current_attackname = globals.weapondatastructure.get(weapon)[1].get()
    globals.motionvalues[weapon] = fetch_mv(globals.current_attackname, globals.weapondatastructure.get(weapon)[0])
    globals.current_motionvalue = globals.motionvalues[weapon]
    print(globals.weapondatastructure.get(weapon)[2] + ': ' + globals.current_attackname
          + " (" + str(globals.motionvalues[weapon]) + ") is selected")
