# Monster Parameters
elemweak = 0.25
rawweak = 0.7

# Weapon Parameters
rawdam = 0
elemdam = 0
rawsharp = 0
elemsharp = 0
aff = 0


def gatherdata():
    global rawdam
    rawdam = float(input("Insert Raw Damage Value: "))
    global elemdam
    elemdam = float(input("Insert Elemental Damage Value: "))
    global rawsharp
    rawsharp = float(input("Insert Physical Sharpness Factor: "))
    global elemsharp
    elemsharp = float(input("Insert Elemental Sharpness Factor: "))
    global aff
    aff = float(input("Insert Affinity Factor: "))


def damageoutput(motionvalue, bloater):
    global aff
    if aff < 0:
        critdamage = 0.75
        aff = - aff
    else:
        critdamage = 1.25

    outputdamage = rawdam * ((1 - aff) + aff * critdamage) * rawsharp * motionvalue * rawweak + elemdam * elemsharp * motionvalue * elemweak

    return outputdamage/bloater


def dualblades():
    bloater = 1.4
    motionvalue = 0.19
    gatherdata()
    output = damageoutput(motionvalue, bloater)
    print("\nTotal Output Damage:" + str(output) + "\n")


def hammer():
    bloater = 5.2
    motionvalue = 0.2
    gatherdata()
    output = damageoutput(motionvalue, bloater)
    print("\nTotal Output Damage:" + str(output) + "\n")


cont = True
while cont:

    print("Welcome to Monster Hunter World: Iceborne Damage Calculator! \n")
    choose = input("1. Dual Blades \n"
                   "2. Hammer \n"
                   "15. Settings \n"
                   "16. Exit \n"
                   "Please, select the Weapon or enter Settings: ")

    if choose == '1':
        dualblades()

    if choose == '2':
        hammer()

    if choose == '16':
        quit()


