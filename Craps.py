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
            sum = Dices()
            print("The sum of dices is " + str(sum))
            number = 0
            result2 = []
            for bet in bets:
                result2.append(bool(bet == sum))
                if bet == sum:
                    number += 1
                else:
                    continue

            if number > 0:
                print("There are " + str(number) + "winners")
            else:
                print("All players lost")