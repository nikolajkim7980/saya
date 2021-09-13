import tkinter as tk
import ttk
from tkinter import *
import tkinter.font as tkFont

window = tk.Tk()
window.geometry('700x500')
window.title("Saya Life Calculator")

# user gest bill. based on usage, throw up suggestions. show water meter helped how much.  improve billing calculator.
# have to list out all of  kype).
# set a goal bill that we want the user to cut down to. make it an input from the user, how much they want to save.

fontStyle = tkFont.Font(family="AppleSystemUIFont", size=15)

frame1 = Frame(window, pady=15) # sf/mf?
frame1.pack()
frame2 = Frame(window, pady=15) # sf/mf collect water usage input
frame2.pack()
frame3 = Frame(window, pady=15) # display bill,tier,biggest issue
frame3.pack()
frame4 = Frame(window, pady=15) # display input for the user to type how much water they want to save
frame4.pack()
frame5 = Frame(window, pady=15) # display suggestiosn for what steps to take
frame5.pack()

sfMonthlyBill = 70 # monthly bill for single families, calculate through saya's bill calcuator
mfMonthlyBill = 90 # monthly bill for multi families,  calculate through saya's bill calcuator

# values given to us by saya, show how much water saya can save through fixing leaks/behavior/hot water
Leaks = 50
Behavior = 40

# hashmap for leak issues:
leakSuggestions = dict({15: "Fix a leaky faucet.", 19: "Repair any leaking hose bibs.",
                        20: "Repair pipe leak or broken sprinkler head.", 21: "Repair any leaks around pool or spa pumps.",
                        30: "Fix a leaky toilet."})
# hashmap for behavior issues:
behaviorSuggestions = dict({1: "Don't use the toilet as a wastebasket.", 2: "Run the dishwasher only when full.",
                            4: "Don't leave the water running while rinsing dishes.", 5: "Shorten showers by 2 minutes.",
                            6: "Install a spa cover to reduce evaporation.", 8: "Turn off the water while brushing your teeth.",
                            9: "Get a new and efficient toilet.", 10: "Purchase a new laundry machine.",
                            14: "Install aerators on faucets.", 19: "Water yard before 6 am or after 8pm.",
                            20: "Adjust sprinklers to reduce overspray onto sidewalks and driveways.",
                            22: "Use a broom instead of a hose to clean the driveway.",
                            25: "Add 2-3 inches of mulch around trees and plants.", 30: "Install a pool cover to reduce evaporation",
                            40: "Install a \"smart irrigation controller\" to automatically adjust watering times.",
                            41: "Replace part of the lawn with native or Russian River friendly plants.",
                            100: "Reduce irrigation time by 2 minutes or eliminate one irrigation cycle per week."})



def increaseProgressBar(goal, progressbar, amount, progressLabel):
    # changes progress bar and progress bar label
    print(amount)
    progressbar['value'] += int(amount)*100/int(goal)
    progressLabel['text'] = "Progress: " + str(int(progressbar['value']*int(goal)/100)) + "/" + str(goal) + " gallons"



def showSuggestions(goal, biggestIssue):
    # frame 5, show suggestions for which steps to take to limit water usage.
    frame4.destroy()
    window.title("Steps to saving " + str(goal) + " gallons")

    # shows label for progressbar
    global progressLabel
    progressLabel = tk.Label(frame5, text="Progress: 0/" + str(goal) + " gallons", font=fontStyle)
    progressLabel.grid(column=0, row=0)

    # make a progress bar to show the progress of saving water
    global progressbar
    progressbar = ttk.Progressbar(frame5, orient=HORIZONTAL, length=400, mode='determinate', )
    progressbar.grid(column=0, row=1)
    # test button / delete later
    space = tk.Label(frame5, text="", pady=10)
    space.grid(column=0, row=2)

    # if the biggest issue is behavior, ues the behaviorSuggestions hashmap. Otherwise, use the leakSuggestions hashmap
    # suggestions is the hashmap, suggestionsKeys is the sorted array of keys of suggestions
    suggestions = behaviorSuggestions.copy()
    if biggestIssue == "Leaks":
        suggestions = leakSuggestions.copy()

    # create a sorted array of the keys of the suggestions.
    suggestionsKeys = suggestions.keys()
    suggestionsKeys.sort()
    print(suggestionsKeys)

    # calculate how many suggestions we have to present to satisfy the user's goal.
    index = 0
    temp = int(goal)
    while temp > 0:
        temp -= suggestionsKeys[index]
        index += 1
        if index >= len(suggestionsKeys):
            break

    # print all of the suggestions
    # this is where im having my issues. im creating the buttons/checkboxes within this while loop. the problem is i need to pass the gallons variable to increaseProgressBar()
    # and the issue is the gallons variable gets rewritten every time. is it even possible to make it so that each checkbox can increaseProgressBar with a unique index?
    i = 0
    while i < len(suggestionsKeys):
        gallons = suggestionsKeys[i] # how many gallons the suggestion will save the user

        text = str(suggestionsKeys[i]) + " gallons: " + str(suggestions.get(suggestionsKeys[i]))
        var1 = IntVar()
        checkbox = Checkbutton(frame5, text=text, variable=var1, command=lambda: increaseProgressBar(goal, progressbar, gallons,progressLabel ))
        checkbox.grid(column=0, row=3+i)
        print(var1)
        i += 1


def inputGoal(biggestIssue, monthyBill, thisTier):
    # frame 4, show input for how much water the user wants to save.
    frame3.destroy()
    window.title("Monthly Bill: $" + str(monthyBill) +" - Tier: " + str(thisTier))
    lbl_test = tk.Label(frame4, text="Your biggest issue is " + str(biggestIssue), font=fontStyle)
    lbl_test.grid(column=0, row=0)
    lbl_test = tk.Label(frame4, text="Enter how much water you'd like to save: (gallons)", font=fontStyle)
    lbl_test.grid(column=0, row=1)
    ent_saveAmt = Entry(frame4, font=fontStyle)
    ent_saveAmt.grid(column=0, row=2)
    btn_sf = tk.Button(frame4, text="See Suggestions!", command=lambda: showSuggestions(ent_saveAmt.get(), biggestIssue), pady=10, font=fontStyle)
    btn_sf.grid(column=0, row=3)


def displayStats(thisTier, monthlyBill):
    # frame 3, create new screen that displays water bill, tier, and the user's biggest issue
    frame2.destroy()
    window.title("Analysis")
    lbl_monthlyBill = tk.Label(frame3, text="Your Monthly Water Bill is $" + str(monthlyBill), font=fontStyle)
    lbl_monthlyBill.grid(column=0, row=0)
    lbl_tier = tk.Label(frame3, text="Your current tier is " + str(thisTier), font=fontStyle)
    lbl_tier.grid(column=0, row=1)
    lbl_status = tk.Label(frame3, text="", font=fontStyle)
    lbl_status.grid(column=0, row=2)
    if thisTier <= 2:
        lbl_status['text'] = "Way to go! You have been very efficient."
    else:
        lbl_status['text'] = "Please take a look at how to minimize your water usage!"

    # find which method will save them the most water
    lbl_suggestion = tk.Label(frame3, text="", font=fontStyle)
    lbl_suggestion.grid(column=0, row=3)
    biggestIssue = ""
    if Behavior > Leaks:
        lbl_suggestion['text'] = "Behavior is your biggest issue. Here are some steps to solve it!"
        biggestIssue = "Behavior"
    else:
        lbl_suggestion['text'] = "Leaks are your biggest issue. Here are some steps to solve it!"
        biggestIssue = "Leaks"

    btn_sf = tk.Button(frame3, text="See the Steps!", command=lambda: inputGoal(biggestIssue, monthlyBill, thisTier), pady=10, font=fontStyle)
    btn_sf.grid(column=0, row=4)


def tier(totalUsage, monthlyBill, singleFamily):
    # calculate tier - from ayushi's code
    # if singleFamily is true, the tier function will use sfMonthlyBill. otherwise, it will use the mfMonthlyBill
    if singleFamily:
        monthlyBill = sfMonthlyBill
    else:
        monthlyBill = mfMonthlyBill
    cost = float(totalUsage) * 0.006
    usagePercent = (monthlyBill - cost) / monthlyBill * 100
    thisTier = 0
    if usagePercent <= 40:
        thisTier = 1
    elif usagePercent <= 100:
        thisTier = 2
    elif usagePercent <= 140:
        thisTier = 3
    else:
        thisTier = 4

    displayStats(thisTier, monthlyBill)


def runSingleFamily():
    # frame 2, calculating rates for single family
    window.title("Single Family Calculator")
    lbl_sf = tk.Label(frame2, text="Please enter how much water you have consumed this month (gallons): ", font=fontStyle)
    lbl_sf.grid(column=0, row=0)
    ent_sf = Entry(frame2, font=fontStyle)
    ent_sf.grid(column=0, row=1)
    btn_sf = tk.Button(frame2, text="Calculate!", command= lambda: tier(ent_sf.get(), sfMonthlyBill, True), font=fontStyle)
    btn_sf.grid(column=0, row=2)


def runMultiFamily():
    # frame 2, calculating rates for multi family
    window.title("Multi Family Calculator")
    lbl_mf = tk.Label(frame2, text="Please enter how much water you have consumed this month (gallons): ", font=fontStyle)
    lbl_mf.grid(column=0, row=0)
    ent_sf = Entry(frame2, font=fontStyle)
    ent_sf.grid(column=0, row=1)
    btn_sf = tk.Button(frame2, text="Calculate!", command=lambda: tier(ent_sf.get(), mfMonthlyBill, False), font=fontStyle)
    btn_sf.grid(column=0, row=2)


def runCalc(family):
    # if the user has chosen single family, we will calculate their water bill using single family rates. vice versa.
    frame1.destroy()
    if family == "Single Family":
        runSingleFamily()
    else:
        runMultiFamily()


def startProgram():
    # frame 1
    # This is the code that first runs. Asks the user if the home is a single or multi family house.
    # Depending on which option is chosen, monthly bill will be different.
    lbl_intro = tk.Label(frame1, text="Hello! Please select if your home is a Single Family or Multi Family home.", font=fontStyle)
    lbl_intro.grid(column=0, row=0)
    combo_intro = ttk.Combobox(frame1, values=["Single Family", "Multiple Family"], font=fontStyle)
    combo_intro.grid(column=0, row=1)
    btn_intro = tk.Button(frame1, text="Submit!", command= lambda: runCalc(combo_intro.get()), font=fontStyle)
    btn_intro.grid(column=0, row=2)


startProgram()

window.mainloop()
