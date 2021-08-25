import tkinter as tk
import ttk
from tkinter import *
import tkinter.font as tkFont

window = tk.Tk()
window.geometry('700x500')
window.title("Saya Life Calculator")

fontStyle = tkFont.Font(family="AppleSystemUIFont", size=15)

frame1 = Frame(window, pady=15) # sf/mf?
frame1.pack()
frame2 = Frame(window, pady=15) # sf/mf collect water usage input
frame2.pack()
frame3 = Frame(window, pady=15) # display bill,tier,biggest issue
frame3.pack()
frame4 = Frame(window, pady=15) # display suggestions for biggest issue
frame4.pack()

sfMonthlyBill = 70 # monthly bill for single families, calculate through saya's bill calcuator
mfMonthlyBill = 90 # monthly bill for multi families,  calculate through saya's bill calcuator
progBarLength = 0

# values given to us by saya, show how much water saya can save through fixing leaks/behavior/hot water
Leaks = 20
Behavior = 30
HotWater = 40



def runCalc(family):
    # if the user has chosen single family, we will calculate their water bill using single family rates. vice versa.
    frame1.destroy()
    if family == "Single Family":
        runSingleFamily()
    else:
        runMultiFamily()


def showSuggestions(biggestIssue):
    # frame 4, show suggestions based on biggest issue
    lbl_test = tk.Label(frame4, text=str(biggestIssue), font=fontStyle)
    lbl_test.grid(column=0, row=0)
    lbl_test = tk.Label(frame4, text="havent gotten code for actual behavior suggestion", font=fontStyle)
    lbl_test.grid(column=0, row=1)


def displayStats(thisTier):
    # frame 3, create new screen that displays water bill, tier, and the user's biggest issue
    frame2.destroy()
    window.title("Analysis")
    lbl_monthlyBill = tk.Label(frame3, text="Your Monthly Water Bill is $" + str(sfMonthlyBill), font=fontStyle)
    lbl_monthlyBill.grid(column=0, row=0)
    lbl_tier = tk.Label(frame3, text="Your current tier is: " + str(thisTier), font=fontStyle)
    lbl_tier.grid(column=0, row=1)
    if thisTier <= 2:
        return
    else:
        lbl_suggestion = tk.Label(frame3, text="", font=fontStyle)
        lbl_suggestion.grid(column=0, row=2)
        # find fixing which method will save them the most water
        biggestIssue=""
        if Leaks > Behavior and Leaks > HotWater:
            lbl_suggestion['text'] = "Leaks are your biggest issue. Here are some steps to solve it!"
            biggestIssue="Leaks"
        elif Behavior > Leaks and Behavior > HotWater:
            lbl_suggestion['text'] = "Behavior is your biggest issue. Here are some steps to solve it!"
            biggestIssue = "Behavior"
        else:
            lbl_suggestion['text'] = "Hot Water is your biggest issue. Here are some steps to solve it!"
            biggestIssue = "HotWater"

        btn_sf = tk.Button(frame3, text="See the Steps!", command=lambda: showSuggestions(biggestIssue), pady=10, font=fontStyle)
        btn_sf.grid(column=0, row=3)


def tier(totalUsage, monthlyBill, singleFamily):
    # calculate tier - from ayushi's code
    # if singleFamily is true, the tier function will use sfMonthlyBill. otherwise, it will use the mfMonthlyBill
    if singleFamily:
        monthlyBill = sfMonthlyBill
    else:
        monthlyBill = mfMonthlyBill
    cost = float(totalUsage) * 0.006
    usagePercent = [(monthlyBill - cost) // monthlyBill] * 100
    thisTier = 0
    if usagePercent <= 40:
        thisTier = 1
    elif usagePercent <= 100:
        thisTier = 2
    elif usagePercent <= 140:
        thisTier = 3
    else:
        thisTier = 4

    displayStats(thisTier)


def runSingleFamily():
    # calculating rates for single family
    window.title("Single Family Calculator")
    lbl_sf = tk.Label(frame2, text="Please enter how much water you have consumed this month (gallons): ", font=fontStyle)
    lbl_sf.grid(column=0, row=0)
    ent_sf = Entry(frame2, font=fontStyle)
    ent_sf.grid(column=0, row=1)
    btn_sf = tk.Button(frame2, text="Calculate!", command= lambda: tier(ent_sf.get(), sfMonthlyBill, True), font=fontStyle)
    btn_sf.grid(column=0, row=2)


def runMultiFamily():
    # calculating rates for multi family
    window.title("Multi Family Calculator")
    lbl_mf = tk.Label(frame2, text="Please enter how much water you have consumed this month (gallons): ", font=fontStyle)
    lbl_mf.grid(column=0, row=0)
    ent_sf = Entry(frame2, font=fontStyle)
    ent_sf.grid(column=0, row=1)
    btn_sf = tk.Button(frame2, text="Calculate!", command=lambda: tier(ent_sf.get(), mfMonthlyBill, False), font=fontStyle)
    btn_sf.grid(column=0, row=2)


def startProgram():
    # This is the code that first runs. Asks the user if the home is a single or multi family house.
    # Depending on which option is chosen, monthly bill will be different.
    lbl_intro = tk.Label(frame1, text="Hello! Please select if your home is a Single Family, or Multi Family home.", font=fontStyle)
    lbl_intro.grid(column=0, row=0)
    combo_intro = ttk.Combobox(frame1, values=["Single Family", "Multiple Family"], font=fontStyle)
    combo_intro.grid(column=0, row=1)
    btn_intro = tk.Button(frame1, text="Submit!", command= lambda: runCalc(combo_intro.get()), font=fontStyle)
    btn_intro.grid(column=0, row=2)


startProgram()

window.mainloop()
