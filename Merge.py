import random
# This is used to fix the random generator so we can test the output
random.seed(3456)

class Table:
    def __init__(self):
        self.weight = [36, 18, 12, 9, 7.2, 6, 7.2, 9, 12, 18, 36]

    def SimulateGame(self, bets, amounts, ttype):
        def AboveMinimum(amounts):
            result1 = []
            for amount in amounts:
                if ttype == "Roulette":                                                 # Choosing different minimal amounts in two cases
                    result1.append(bool(amount >= random.choice((50, 100, 200))))
                else:
                    result1.append(bool(amount >= random.choice((0, 25, 50))))
            return (result1)

        if ttype == "Roulette":                                                         # Roulette table

            def SpinTheWheel(bets):
                print(" Spinning the wheel...")
                truth = random.randint(0, 36)
                result2 = []
                number = 0
                for bet in bets:
                    result2.append(bool(bet == truth))
                    if bet == truth:
                        number += 1
                    else:
                        continue
                print("Ball lands on " + str(truth))

                if number != 0:
                    print("There are " + str(number) + " correct bet(s)")
                else:
                    print("No winners this round")
                return (result2)

            playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), SpinTheWheel(bets))]
            casinowin = sum(amounts) - sum(playerwin_temp)
            playerwin = [i * 30 for i in playerwin_temp]
            return [casinowin, playerwin]

        else:                                                                          # Craps table
            def Dices():
                return random.randint(1, 6) + random.randint(1, 6)

            def RollTheDices(bets):
                summ = Dices()
                print("The sum of dices is " + str(summ))
                number = 0
                result2 = []
                for bet in bets:
                    result2.append(bool(bet == summ))
                    if bet == summ:
                        number += 1
                    else:
                        continue

                if number > 0:
                    print("There are " + str(number) + " winner(s)")
                else:
                    print("No winners this round")
                return (result2), summ

            r, summ = RollTheDices(bets)

            playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), r)]
            playerwin = [0.9 * amount * self.weight[summ - 2] for amount in playerwin_temp]
            casinowin = sum(amounts) - sum(playerwin)
            return [casinowin, playerwin]




