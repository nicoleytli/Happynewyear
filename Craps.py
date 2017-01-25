import random
# This is used to fix the random generator so we can test the output
random.seed(3456)

class Craps:
    def __init__(self, min):
        self.min = min

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

        if summ == 2 or summ == 12:
            Playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), r)]
            Casinowin = sum(amounts) - sum(Playerwin_temp)
            return [Casinowin, [0.9 * amount / (1 / 36) for amount in Playerwin_temp]]
        elif summ == 3 or summ == 11:
            Playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), r)]
            Casinowin = sum(amounts) - sum(Playerwin_temp)
            return [Casinowin, [0.9 * amount / (1 / 18) for amount in Playerwin_temp]]
        elif summ == 4 or summ == 10:
            Playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), r)]
            Casinowin = sum(amounts) - sum(Playerwin_temp)
            return [Casinowin, [0.9 * amount / (1 / 12) for amount in Playerwin_temp]]
        elif summ == 5 or summ == 9:
            Playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), r)]
            Casinowin = sum(amounts) - sum(Playerwin_temp)
            return [Casinowin, [0.9 * amount / (1 / 9) for amount in Playerwin_temp]]
        elif summ == 6 or summ == 8:
            Playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), r)]
            Casinowin = sum(amounts) - sum(Playerwin_temp)
            return [Casinowin, [0.9 * amount / (5 / 36) for amount in Playerwin_temp]]
        else:
            Playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), r)]
            Casinowin = sum(amounts) - sum(Playerwin_temp)
            return [Casinowin, [0.9 * amount / (1 / 6) for amount in Playerwin_temp]]
