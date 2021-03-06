import random
# This is used to fix the random generator so we can test the output
random.seed(3456)

class Roulette:
    def __init__(self, min):
        self.min = min

    def SimulateGame(self, bets, amounts):
        def AboveMinimum(amounts):
            result1 = []
            for amount in amounts:
                result1.append(bool(amount >= self.min))
            return (result1)

        def SpinTheWheel(bets):
            print(" Spinning the wheel...")
            truth = random.randint(0, 36)              # The correct bet
            result2 = []
            number = 0                                 # Used to indicate the number of correct bets
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

        # If bet=correct bet and amount>=minimal amount, player wins
        playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), SpinTheWheel(bets))]
        casinowin = sum(amounts) - sum(playerwin_temp)
        playerwin = [i * 30 for i in playerwin_temp]
        return [casinowin, playerwin]
