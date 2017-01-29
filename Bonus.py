#################### Question 1 ####################

import Evening
from matplotlib import pyplot as plt

cashflow = []
avgb = []
avgc = []
def Go(numroulette, numcraps, barman, wage, cash, total, returning, bachelor, freebudget, evenings):

    numroulette = numroulette
    numcraps = numcraps
    barman = barman
    wage = wage
    cash = cash
    total = total
    returning = returning
    bachelor = bachelor
    freebudget = freebudget

    for evening in range(evenings):
        print("Evening " + str(evening + 1))
        c, profit, avgbtips, avgctips = Evening.SimulateEvening(numroulette, numcraps, barman, wage, cash, total, returning, bachelor, freebudget)
        cashflow.extend([profit])
        cash = c
        avgb.extend([avgbtips])
        avgc.extend([avgctips])


    plt.title('Cashflow of Casino')
    plt.ylabel('profit($)')
    plt.xlabel('Evening')
    plt.plot(range(1, len(cashflow) + 1), cashflow)
    plt.show()

    # Plot average tips for Barmen
    plt.title('Average Tips for Barmen')
    plt.ylabel('Tips($)')
    plt.xlabel('Evening')
    plt.plot(range(1, len(avgb) + 1), avgb)
    plt.show()

    # Plot average tips for Croupiers
    plt.title('Average Tips for Croupiers')
    plt.ylabel('Tips($)')
    plt.xlabel('Evening')
    plt.plot(range(1, len(avgc) + 1), avgc)
    plt.show()

# # Result of all Roulette tables
print(Go(20, 0, 4, 200, 50000, 100, 0.5, 0.1, 200, 1000))

# # Result of all Craps tables
print(Go(0, 20, 4, 200, 50000, 100, 0.5, 0.1, 200, 1000))

# Result of average tips for Croupiers and Barmen
print(Go(10, 10, 4, 200, 50000, 100, 0.5, 0.1, 200, 1000))




