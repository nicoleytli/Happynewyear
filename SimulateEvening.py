import Evening
from matplotlib import pyplot as plt

cashflow = []
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
        cash, profit = Evening.SimulateEvening(numroulette, numcraps, barman, wage, cash, total, returning, bachelor, freebudget)
        cashflow.extend([profit])

    plt.title('Cashflow of Casino')
    plt.ylabel('profit($)')
    plt.xlabel('Evening')
    plt.plot(range(1, len(cashflow) + 1), cashflow)
    plt.show()

print(Go(10, 10, 4, 200, 50000, 100, 0.5, 0.1, 200, 1000))
