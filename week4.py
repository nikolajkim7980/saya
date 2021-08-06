import tkinter as tk
from tkinter import ttk
from tkinter import *

L = 1 # L is reducing leaks
B = 2 # B is recommending good behavior
H = 3 # H is hot water.
savedWater = L + B + H # hcf saved by saya
savedMoney = 0 # amount of money saved based on water rates

def solve(x, y, tier, family):
    #orange county
    print("Current profits: $" + str(y-x))
    lbl_currentProfits['text'] = "Current Profits: $" + str(y-x) # update label for current profits

    if family == "Single Family":
        savedMoney = singleFamilyCalcuator(tier)
    else:
        savedMoney = multiFamilyCalculator(tier)

    print("Money Saved with Saya: $" + str(savedMoney))
    lbl_moneySaved['text'] = "Money Saved with Saya: $" + str(savedMoney) # update label for saved money
    print("Resulting profits: $" + str(y-x + savedMoney))
    lbl_resultingProfits['text'] = "Resulting Profits: $" + str(y-x + savedMoney) # update label for resulting profits


def singleFamilyCalcuator(tier):
    singleRates = [2.55, 2.61, 2.71]
    savedMoney = savedWater * singleRates[tier-1]
    return savedMoney


def multiFamilyCalculator(tier):
    multiRates = [2.54, 2.58, 2.63]
    savedMoney = savedWater * multiRates[tier-1]
    return savedMoney


# solve(110, 100, 1, "Single Family")
# solve(Utility Cost, Paid Bill, Tier, singleFamily?)

# --------------------------------------------------- tkinter

window = tk.Tk()
window.geometry('700x500')
window.title("Saya Life Calculator")


def getInputs():
    family = combo_q1.get()
    tier = combo_q2.get()
    utilityCost = ent_q3.get()
    paidBill = ent_q4.get()
    print(family + "\nTier: " + tier + "\nUtility Cost: $" + utilityCost + "\nPaid Bill: $ " + paidBill)
    print("-----------------")
    solve(int(utilityCost), int(paidBill), int(tier), family)


# single/multiple prompt
lbl_q1 = tk.Label(window, text="Single Family or Multiple Family: ")
lbl_q1.grid(column=0, row=0)
combo_q1 = ttk.Combobox(values=["Single Family", "Multiple Family"])
combo_q1.grid(column=0, row=1)
btn_q1 = tk.Button(text="Calculate!", command=getInputs)
btn_q1.grid(column=0, row=2)

# tier prompt
lbl_q2 = tk.Label(window, text="Tier: ")
lbl_q2.grid(column=1, row=0)
combo_q2 = ttk.Combobox(values=["1", "2", "3", "4"])
combo_q2.grid(column=1, row=1)

# utility cost prompt
lbl_q3 = tk.Label(window, text="Utility Cost: $")
lbl_q3.grid(column=3, row=0)
ent_q3 = Entry(window)
ent_q3.grid(column=3, row=1)

# paid bill prompt
lbl_q4 = tk.Label(window, text="Paid Bill: $")
lbl_q4.grid(column=4, row=0)
ent_q4 = Entry(window)
ent_q4.grid(column=4, row=1)

# print calculated values
lbl_currentProfits = tk.Label(window, text="")
lbl_currentProfits.grid(column=0, row=3)
lbl_moneySaved = tk.Label(window, text="")
lbl_moneySaved.grid(column=0, row=4)
lbl_resultingProfits = tk.Label(window, text="")
lbl_resultingProfits.grid(column=0, row=5)

window.mainloop()
