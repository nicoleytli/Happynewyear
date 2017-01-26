import random
# This is used to fix the random generator so we can test the output
random.seed(3456)

class Craps:
    def __init__(self, min):
        self.min = min
        self.weight = [36, 18, 12, 9, 7.2, 6, 7.2, 9, 12, 18, 36]

    def SimulateGame(self, bets, amounts):
        def AboveMinimum(amounts):
            result1 = []
            for amount in amounts:
                result1.append(bool(amount >= self.min))
            return (result1)

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
