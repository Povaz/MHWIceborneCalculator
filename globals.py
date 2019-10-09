from tkinter import ttk
import pandas as pd

# Data Structure
weapondatastructure = []
current_weapon = 0

# Monster Parameters
elemweak = 0.25
rawweak = 0.7

# Skills Parameters
criticalboost_value = 0.0
criticalelement_active = False
criticaleye_value = 0.0

# Weapon Parameters
sharpvalues = [[1.39, 1.25], [1.32, 1.125], [1.2, 1.0625],
               [1.05, 1], [1.00, 0.75], [0.75, 0.50], [0.50, 0.25]]
motionvalues = []
bloaters = []
crit_elems = []
current_attackname = 'Null'
current_motionvalue = 0.0
current_bloater = 1.00
current_rawsharp = 0.0
current_elemsharp = 0.0
current_critelem = 1.00


def setdata():
    # Imported Data and Combobox for Weapons
    dualblades_mv = pd.read_csv('./files/weapons/dualblades_mv.csv', sep=';')
    dualblades_cb = ttk.Combobox()
    hammer_mv = pd.read_csv('./files/weapons/hammer_mv.csv', sep=';')
    hammer_cb = ttk.Combobox()
    bow_mv = pd.read_csv('./files/weapons/bow_mv.csv', sep=';')
    bow_cb = ttk.Combobox()
    greatsword_mv = pd.read_csv('./files/weapons/greatsword_mv.csv', sep=';')
    greatsword_cb = ttk.Combobox()
    longsword_mv = pd.read_csv('./files/weapons/longsword_mv.csv', sep=';')
    longsword_cb = ttk.Combobox()
    swordandshield_mv = pd.read_csv('./files/weapons/swordandshield_mv.csv', sep=';')
    swordandshield_cb = ttk.Combobox()
    huntinghorn_mv = pd.read_csv('./files/weapons/huntinghorn_mv.csv', sep=';')
    huntinghorn_cb = ttk.Combobox()
    lance_mv = pd.read_csv('./files/weapons/lance_mv.csv', sep=';')
    lance_cb = ttk.Combobox()
    gunlance_mv = pd.read_csv('./files/weapons/gunlance_mv.csv', sep=';')
    gunlance_cb = ttk.Combobox()
    switchaxe_mv = pd.read_csv('./files/weapons/switchaxe_mv.csv', sep=';')
    switchaxe_cb = ttk.Combobox()
    chargeblade_mv = pd.read_csv('./files/weapons/chargeblade_mv.csv', sep=';')
    chargeblade_cb = ttk.Combobox()

    global weapondatastructure
    weapondatastructure = {0: [dualblades_mv, dualblades_cb, 'Dual Blades'],
                           1: [hammer_mv, hammer_cb, 'Hammer'],
                           2: [bow_mv, bow_cb, 'Bow'],
                           3: [greatsword_mv, greatsword_cb, 'Great Sword'],
                           4: [longsword_mv, longsword_cb, 'Long Sword'],
                           5: [swordandshield_mv, swordandshield_cb, 'Sword and Shield'],
                           6: [huntinghorn_mv, huntinghorn_cb, 'Hunting Horn'],
                           7: [lance_mv, lance_cb, 'Lance'],
                           8: [gunlance_mv, gunlance_cb, 'Gunlance'],
                           9: [switchaxe_mv, switchaxe_cb, 'Switch Axe'],
                           10: [chargeblade_mv, chargeblade_cb, 'Charge Blade']}

    # Weapons hard coded values

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

    # Great Sword: Index 3
    motionvalues.append(0.48)
    bloaters.append(4.8)
    crit_elems.append(1.2)

    # Long Sword: Index 4
    motionvalues.append(0.24)
    bloaters.append(3.3)
    crit_elems.append(1.25)

    # Sword and Shield: Index 5
    motionvalues.append(0.14)
    bloaters.append(1.4)
    crit_elems.append(1.35)

    # Hunting Horn: Index 6
    motionvalues.append(0.27)
    bloaters.append(4.2)
    crit_elems.append(1.25)

    # Lance: Index 7
    motionvalues.append(0.2)
    bloaters.append(2.3)
    crit_elems.append(1.25)

    # TODO Gunlance: Special Attacks
    # Gunlance: Index 8
    motionvalues.append(0.3)
    bloaters.append(2.3)
    crit_elems.append(1.25)

    # Switch Axe: Index 9
    motionvalues.append(0.29)
    bloaters.append(3.5)
    crit_elems.append(1.25)

    # TODO Charge Blade: Special Attacks
    # Charge Blade: Index 10
    motionvalues.append(0.2)
    bloaters.append(3.6)
    crit_elems.append(1.25)
