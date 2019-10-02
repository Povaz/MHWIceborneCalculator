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
    dualblades_mv = pd.read_csv('./files/weapons/dualblades_mv.csv')
    dualblades_cb = ttk.Combobox()
    hammer_mv = pd.read_csv('./files/weapons/hammer_mv.csv')
    hammer_cb = ttk.Combobox()
    bow_mv = pd.read_csv('./files/weapons/bow_mv.csv')
    bow_cb = ttk.Combobox()

    global weapondatastructure
    weapondatastructure = {0: [dualblades_mv, dualblades_cb, 'Dual Blades'],
                           1: [hammer_mv, hammer_cb, 'Hammer'],
                           2: [bow_mv, bow_cb, 'Bow']}

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