import random
# This is used to fix the random generator so we can test the output
random.seed(3456)

import Roulette
import Craps
#
amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
table1 = Roulette.Roulette(100)
print(table1.SimulateGame(bets1, amounts1))
print(table1.SimulateGame(bets1, amounts1))

amounts1 = [5, 85, 120, 65, 150, 122]
bets1 = [10, 4, 7, 11, 11, 3]
table1 = Craps.Craps(10)
print(table1.SimulateGame(bets1, amounts1))
print(table1.SimulateGame(bets1, amounts1))