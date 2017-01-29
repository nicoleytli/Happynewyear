import Evening
from matplotlib import pyplot as plt

cashflow = []
cc = []
# A function for simulating
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
        cc.extend([c])
        cash = c


    # Plot the cashflow
    plt.title('Cashflow of Casino')
    plt.ylabel('profit($)')
    plt.xlabel('Evening')
    plt.plot(range(1, len(cashflow) + 1), cashflow)
    plt.show()

    # Plot the evolution of cash
    plt.title('Evolution of Cash')
    plt.ylabel('profit($)')
    plt.xlabel('Evening')
    plt.plot(range(1, len(cc) + 1), cc)
    plt.show()

# Evening
print(Go(10, 10, 4, 200, 50000, 100, 0.5, 0.1, 200, 1000))
