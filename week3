# coding=utf-8

# L is reducing leaks
# B is recommending good behavior
# H is hot water.
L = 1
B = 2
H = 3
savedWater = L + B + H #hcf saved by saya
savedMoney = 0 #amount of money saved based on water rates

def solve(x, y, tier, singleF):
    #orange county
    print("Current profits: $" + str(y-x))
    if singleF:
        savedMoney = singleFamilyCalculator(tier)
    else:
        savedMoney = multiFamilyCalculator(tier)

    print("Saving $" + str(savedMoney))
    print("Resulting profits: $" + str(y-x + savedMoney))


def singleFamilyCalculator(tier):
    singleRates = [2.55, 2.61, 2.71]
    savedMoney = savedWater * singleRates[tier-1]
    return savedMoney


def multiFamilyCalculator(tier):
    multiRates = [2.54, 2.58, 2.63]
    savedMoney = savedWater * multiRates[tier-1]
    return savedMoney


solve(110, 100, 1, True)
# solve(Utility Cost, Paid Bill, Tier, singleFamily?)
