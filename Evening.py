import random


# This is used to fix the random generator so we can test the output
random.seed(3456)

# A function for simulation
def SimulateEvening(numroulette, numcraps, barman, wage, cash, total, returning, bachelor, freebudget):

    numroulette = numroulette
    numcraps = numcraps
    barman = barman
    wage = wage
    cash = cash
    total = total
    returning = returning
    bachelor = bachelor
    freebudget = freebudget


################ Step 1: Initializing Players ################

# Step 1.1: Defining class of player
    class Player:
        def __init__(self, budget, gain, ptype, amount, bet, out):
            self.budget = budget
            self.gain = gain
            self.ptype = ptype
            self.amount = amount
            self.bet = bet
            self.out = out                                             # Using out to decide the player can enter the next round or not

# Step 1.2: Computing budget and decide type of every player
    # A function to assign player type
    def GetPtype(total, returning, bachelor):
        numreturn = int(total * returning)
        numbachelor = int(total * bachelor)
        numonetime = total - (numreturn + numbachelor)
        temp = []
        temp.extend(["returning" for i in range(numreturn)])
        temp.extend(["onetime" for i in range(numonetime)])
        temp.extend(["bachelor" for i in range(numbachelor)])
        return (temp)                                                # A list of player type, e.g: ['returning', 'returning', 'onetime', 'bachelor']

    # A function to get initial budget for each players
    def GetBudget(ptype, freebudget):
        budget = []
        for item in ptype:
            if item == "returning":
                budget.extend([random.randint(100, 300)])
            elif item == "onetime":
                budget.extend([random.randint(200, 300)])
            else:
                budget.extend([random.randint(200, 500) + freebudget])
        return budget                                               # A list of budget

    # Step 1.3: Class instantiation
    ptype = GetPtype(total, returning, bachelor)
    P = []
    budget = GetBudget(ptype, freebudget)
    for i in range(0, total):
        P.append(Player(budget[i], 0, ptype[i], 0, 0, 0))           # Setting the initial numbers of gain, amount, bet, out all equal to 0


################ Step 2: Initializing Tables ################

    # Step 2.1: creating a list of table number arranging from the first to the last table, and length of this list is equal to number of all players
    def WhichTable(total, numroulette, numcraps):
        table = []
        for i in range(total):
            table.extend([random.randint(1, (numroulette + numcraps))])
        return table                                               # A list of table numbers, e,g: [1, 2, 1, 5, 6, 3]

    # Step 2.2: A function to decide minimal betted amount for every table
    def TableMin(numroulette, numcraps):
        tablemin = []
        for i in range(0, (numroulette + numcraps)):
            if i < numroulette:                                    # i.e: Roulette table
                tablemin.extend([random.choice((50, 100, 200))])
            else:                                                  # Craps table
                tablemin.extend([random.choice((0, 25, 50))])
        return tablemin                                            # A list of minimal betted amount for each tables

    tablemin = TableMin(numroulette, numcraps)

    # Step 2.3: Winning rules and results for each tables
    class Table:
        def __init__(self, min):
            self.min = min
            self.weight = [36, 18, 12, 9, 7.2, 6, 7.2, 9, 12, 18, 36]

        def SimulateGame(self, bets, amounts, tnum):
            def AboveMinimum(amounts):
                result1 = []
                for amount in amounts:
                    result1.append(bool(amount >= self.min))
                return (result1)

            if tnum < numroulette:

                def SpinTheWheel(bets):
                    truth = random.randint(0, 36)
                    result2 = []
                    number = 0
                    for bet in bets:
                        result2.append(bool(bet == truth))
                        if bet == truth:
                            number += 1
                        else:
                            continue
                    return (result2)

                playerwin_temp = [i * j * k for i, j, k in zip(amounts, AboveMinimum(amounts), SpinTheWheel(bets))]
                casinowin_temp = (sum(amounts) - sum(playerwin_temp))
                if casinowin_temp > 0:                                             # If casino gains money on one table
                    casinowin = casinowin_temp * 0.995
                    croupiergain = casinowin_temp * 0.005                          # Croupier tips
                else:
                    casinowin = casinowin_temp
                    croupiergain = 0
                playerwin = [i * 30 for i in playerwin_temp]
                return [casinowin, croupiergain, playerwin]

            else:
                def Dices():
                    return random.randint(1, 6) + random.randint(1, 6)

                def RollTheDices(bets):
                    summ = Dices()
                    number = 0
                    result2 = []
                    for bet in bets:
                        result2.append(bool(bet == summ))
                        if bet == summ:
                            number += 1
                        else:
                            continue
                    return (result2), summ

                r, summ = RollTheDices(bets)

                playerwin_temp = [amount * abovemin * bet for amount, abovemin, bet in zip(amounts, AboveMinimum(amounts), r)]
                playerwin = [0.9 * amount * self.weight[summ - 2] for amount in playerwin_temp]
                casinowin_temp = sum(amounts) - sum(playerwin)
                if casinowin_temp > 0:                                              # If casino gains money on one table
                    casinowin = casinowin_temp * 0.995
                    croupiergain = casinowin_temp * 0.005
                else:                                                               # Croupier tips
                    casinowin = casinowin_temp
                    croupiergain = 0
                return [casinowin, croupiergain, playerwin]


################ Step 3: Setting up function for drink ################

    # A function for drink
    def Drink(budget):
        time = random.randint(1, 3)                                                 # Using to compute probability of times for buying drinks
        if time <= 2:                                                               # P(time <= 2) = 2/3
            if budget >= 60:
                drink = 2 * 20                                                      # Player buys drinks for two times
                tips1 = random.randint(0, 20)
                if (budget - drink - tips1) < 20:                                   # After two drinks and one tip, it's possible that his budget is less than 20
                    tips2 = random.randint(0, (budget - drink - tips1))
                else:                                                               # If budget is still more than 20
                    tips2 = random.randint(0, 20)
            else:
                drink = 0
                tips1 = 0
                tips2 = 0
        else:
            if budget >= 60:
                drink = 20
                tips1 = random.randint(0, 20)
                tips2 = 0
            else:
                drink = 0
                tips1 = 0
                tips2 = 0
        cost = drink + tips1 + tips2
        return drink, cost, tips1, tips2


################ Step 4: Initialize Employees ################

    # A class for croupier
    class Croupier:
        def __init__(self, wage):
            self.wage = wage
            self.balance = wage
    # Class instantiation
    Cp = []
    for i in range(0, (numroulette + numcraps)):
        Cp.append(Croupier(wage))

    # A class for barman
    class Barman:
        def __init__(self, wage):
            self.wage = wage
            self.balance = wage
    # Class instantiation
    B = []
    for i in range(0, barman):
        B.append(Barman(wage))


################ Step 5: Setting Up Casino ################

    # A class for Casino
    class Casino:
        def __init__(self, cash):
            self.cash = cash
            self.balance = cash - (bachelor * total * 200)                         # The actual cash is initial one minus budgets gave to bachelors
    # Class instantiation

    C = Casino(cash)

################ Step 6: Game Begin ################
    for round in range(0, 3):                                                      # 3 rounds per evening

        print("Round " + str(round+1))

        # Step 6.1: Deciding how many players are allowed to play
        Pp = []
        for player in range(0, total):
            if P[player].out == 0:                                                 # out = 0 means budget = 0
                Pp.append(P[player])                                               # A list for qualified players
            else:
                continue

        total = len(Pp)                                                            # New total number of players
        table = WhichTable(total, numroulette, numcraps)


        # Step 6.2: Every player getting either 1 or 2 drinks
        for player in range(0, total):
            drink, pcost, tips1, tips2 = Drink(Pp[player].budget)
            C.balance += drink                                                    # Casino gains from selling drinks
            B[random.randint(0, (barman - 1))].balance += tips1                   # Barman 1
            B[random.randint(0, (barman - 1))].balance += tips2                   # Barman 2
            Pp[player].budget -= pcost                                            # Cost of player



        # Step 6.3: Determining betted numbers and betted amounts for all players, and assigning them to different tables
        amount = []
        bet = []
        P_new = []
        for tnum in range(0, (numroulette + numcraps)):                          # The first stage: looking at every table
            amount_temp = []
            bet_temp = []
            if tnum < numroulette:                                               # If it is Roulette table
                for i, num in enumerate(table):                                  # The second stage: assigning players to each tables
                    if num == (tnum + 1):                                        # Choosing corresponding table number for players
                        if Pp[i].ptype == "returning":                           # The third stage: deciding betted amount according to player's type
                            if Pp[i].budget >= tablemin[tnum]:
                                Pp[i].amount = tablemin[tnum]
                            else:                                                # If returning player's budget < minimal amount on Roulette tables
                                Pp[i].amount = 0
                        elif Pp[i].ptype == "onetime":
                            Pp[i].amount = random.randint(0, int(Pp[i].budget / 3))
                        else:
                            Pp[i].amount = random.randint(0, int(Pp[i].budget))
                        Pp[i].bet = random.randint(0, 36)                        # Choosing betted numbers
                        amount_temp.extend([Pp[i].amount])
                        bet_temp.extend([Pp[i].bet])
                        P_new.append(Pp[i])                                      # A new list of players in the right order
                    else:
                        continue
            else:
                for i, num in enumerate(table):
                    if num == (tnum + 1):
                        if Pp[i].ptype == "returning":
                            Pp[i].amount = tablemin[tnum]
                        elif Pp[i].ptype == "onetime":
                            Pp[i].amount = random.randint(0, int(Pp[i].budget / 3))
                        else:
                            Pp[i].amount = random.randint(0, int(Pp[i].budget))
                        Pp[i].bet = random.randint(2, 12)
                        amount_temp.extend([Pp[i].amount])
                        bet_temp.extend([Pp[i].bet])
                        P_new.append(Pp[i])
                    else:
                        continue
            amount.append(amount_temp)
            bet.append(bet_temp)

        amount_new = []

        for i in range(0, len(amount)):                                          # Merging into one list
            for j in range(0, len(amount[i])):
                amount_new.extend([amount[i][j]])


        # Step 6.4: Run every table
        past = 0                                                                 # Indicating table number

        for tnum in range(0, (numroulette + numcraps)):
            t = Table(tablemin[tnum])
            casinowin, croupiergain, playerwin = t.SimulateGame(bet[tnum], amount[tnum], tnum)        # Getting game results
            C.balance += casinowin                                               # Adjusting casino's balance
            Cp[tnum].balance += croupiergain                                     # Adjusting Croupier's balance
            for player in range(0, len(playerwin)):
                P_new[(player + past)].gain += playerwin[player]                 # Player's gains, should be added to budget after all rounds
                P_new[(player + past)].budget -= amount_new[(player + past)]     # Adjusting budget
                if P_new[(player + past)].budget == 0:                           # Checking if player should be ruled out for next round
                    P_new[(player + past)].out = 1
                else:
                    continue
            past += len(playerwin)
        P = P_new


################ Step 7: Calculating results for one evening ################

    profit = C.balance - C.cash                                                  # casino's profit for one evening

    btips = 0
    for b in range(0, len(B)):                                              # Computing sum of tips for barmen
        btips += (B[b].balance - B[b].wage)
    avgbtips = btips / barman                                                     # The average of tips


    ctips = 0
    for c in range(0, len(Cp)):                                           # Computing sum of tips for croupiers
        ctips += (Cp[c].balance - Cp[c].wage)
    avgctips = ctips / (numroulette + numcraps)                                   # The average of tips


    return C.balance, profit, avgbtips, avgctips





