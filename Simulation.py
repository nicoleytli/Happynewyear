import random
# This is used to fix the random generator so we can test the output
random.seed(3456)

from matplotlib import pyplot as plt
import Roulette
import Craps

# Checking the output of two games
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

# Simulating 1000 times
for j in range(1000):
    # Playing the game 1000 times in each simulation
    for i in range(1000):
        numplayer = random.randint(1,10)                              # Randomly choosing number of players
        mini = random.choice(range(20))                               # Determining the minimal betted amount
        amount = random.sample(range(mini,200),numplayer)
        bet = random.sample(range(2,13),numplayer)
        testtable = Craps.Craps(mini)
        cwin += testtable.SimulateGame(bet, amount)[0]                # Sum of casino gains
        total += sum(amount)                                          # Total money on this table

    casinowin_per = 100 - (cwin / total) * 100                        # Computing percentage of money going to players
    casi.extend([casinowin_per])

# Plot the simulation result
plt.title("Percentage of Players' Gains")
plt.ylabel('percent(%)')
plt.xlabel('Simulation Time')
plt.plot(range(1, len(casi)+1), casi)
plt.show()

