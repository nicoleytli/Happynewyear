import random
# This is used to fix the random generator so we can test the output
# random.seed(3456)
from matplotlib import pyplot as plt
import Roulette
import Craps
#
amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
table1 = Roulette.Roulette(100)
print(table1.SimulateGame(bets1, amounts1))
print(table1.SimulateGame(bets1, amounts1))

amounts1 = [25, 85, 120, 65, 150, 122]
bets1 = [10, 4, 7, 11, 11, 3]
table1 = Craps.Craps(10)
print(table1.SimulateGame(bets1, amounts1))
print(table1.SimulateGame(bets1, amounts1))


# Simultaion for Craps
cwin = 0
total = 0
casi = []

for j in range(1000):
    for i in range(1000):
        numplayer = random.randint(1,10)
        mini = random.choice(range(20))
        amount = random.sample(range(mini,200),numplayer)
        bet = random.sample(range(2,13),numplayer)
        testtable = Craps.Craps(mini)
        cwin += testtable.SimulateGame(bet, amount)[0]
        total += sum(amount)

    casinowin_per = 100 - (cwin / total) * 100
    casi.extend([casinowin_per])

plt.title("Percentage of Players' Gains")
plt.ylabel('percent(%)')
plt.xlabel('Simulation Time')
plt.plot(range(1, len(casi)+1), casi)
plt.show()

