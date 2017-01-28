import random
from functools import reduce

# This is used to fix the random generator so we can test the output
random.seed(3456)

def SimulateEvening(numroulette, numcraps, barman, wage, cash, total, returning, bachelor, freebudget, totalround):

    numroulette = numroulette
    numcraps = numcraps
    barman = barman
    wage = wage
    cash = cash
    total = total
    returning = returning
    bachelor = bachelor
    freebudget = freebudget
    totalround = totalround

# Step 1: initialize player
# Step 1.1: class
    class Player:
        def __init__(self, budget, gain, ptype, amount, bet, out):
            self.budget = budget
            self.gain = gain
            self.ptype = ptype
            self.amount = amount
            self.bet = bet
            self.out = out

    # Step 1.2: fix budget and type
    def GetPtype(total, returning, bachelor):
        numreturn = int(total * returning)
        numbachelor = int(total * bachelor)
        numonetime = total - (numreturn + numbachelor)
        temp = []
        temp.extend(["returning" for i in range(numreturn)])
        temp.extend(["onetime" for i in range(numonetime)])
        temp.extend(["bachelor" for i in range(numbachelor)])
        return (temp)

    def GetBudget(ptype, freebudget):
        budget = []
        for item in ptype:
            if item == "returning":
                budget.extend([random.randint(100, 300)])
            elif item == "onetime":
                budget.extend([random.randint(200, 300)])
            else:
                budget.extend([random.randint(200, 500) + freebudget])
        return budget

    # Step 1.3: 实例化
    ptype = GetPtype(total, returning, bachelor)
    P = []
    budget = GetBudget(ptype, freebudget)
    for i in range(0, total):
        P.append(Player(budget[i], 0, ptype[i], 0, 0, 0))

    # Step 2: initialize table
    # Step 2.1: 生成和player人数相等的table数，用于分配player到各个table
    def WhichTable(total, numroulette, numcraps):
        table = []
        for i in range(total):
            table.extend([random.randint(1, (numroulette + numcraps + 1))])
        return table


    # Step 2.2: 返回所有table的最小amount
    def TableMin(numroulette, numcraps):
        tablemin = []
        for i in range(0, (numroulette + numcraps)):
            if i < numroulette:
                tablemin.extend([random.choice((50, 100, 200))])
            else:
                tablemin.extend([random.choice((0, 25, 50))])
        return tablemin

    tablemin = TableMin(numroulette, numcraps)

    # Step 2.3: 制定每个table的规则
    class Table:
        def __init__(self, min):
            self.min = min
            self.weight = [36, 18, 12, 9, 7.2, 6, 7.2, 9, 12, 18, 36]


        def SimulateGame(self, bets, amounts, tnum):                     # tnum 可以分辨ttype
            def AboveMinimum(amounts):
                result1 = []
                for amount in amounts:
                    result1.append(bool(amount >= self.min))
                return (result1)

            if tnum < numroulette:

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

                playerwin_temp = [i * j * k for i, j, k in zip(amounts, AboveMinimum(amounts), SpinTheWheel(bets))]
                casinowin_temp = (sum(amounts) - sum(playerwin_temp))
                if casinowin_temp > 0:
                    casinowin = casinowin_temp * 0.995
                    croupiergain = casinowin_temp * 0.005
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
                casinowin_temp = sum(amounts) - sum(playerwin)
                if casinowin_temp > 0:
                    casinowin = casinowin_temp * 0.995
                    croupiergain = casinowin_temp * 0.005
                else:
                    casinowin = casinowin_temp
                    croupiergain = 0
                return [casinowin, croupiergain, playerwin]

    # Step 3: set up drink, 每一个player买drink的情况, 返回值是数字
    def Drink(budget):
        if budget >= 60:
            drink = random.randint(1, 2) * 20
            tips = random.randint(0, 20)
        else:
            drink = 0
            tips = 0
        cost = drink + tips
        return drink, cost, tips


    # Step 4: set up employee
    class Croupier:
        def __init__(self, wage):
            self.wage = wage
            self.balance = wage
    #实例化
    Cp = []
    for i in range(0, (numroulette + numcraps)):
        Cp.append(Croupier(wage))       #这里的wage是外部输入的

    class Barman:
        def __init__(self, wage):
            self.wage = wage
            self.balance = wage
    #实例化
    B = []
    for i in range(0, barman):      # barman 是输入的barman数量
        B.append(Barman(wage))         #这里的wage是外部输入的

    # Step 5: set up casino
    class Casino:
        def __init__(self, cash):
            self.cash = cash
            self.balance = cash
    #实例化
    C = Casino(cash)

    # Step 6: game begin
    for round in range(0, totalround):

        print("Round " + str(round+1))

        table = WhichTable(total, numroulette, numcraps)
        # Step 6.0: decide how many player are allowed to play
        Pp = []
        for player in range(0, total):
            if P[player].out == 0:
                Pp.append(P[player])
            else:
                continue


        # Step 6.1: every player goes get either 1 or 2 drinks
        for player in range(0, total):
            drink, pcost, tips = Drink(Pp[player].budget)
            C.balance += drink   # 赌场从饮料中赚的钱
            B[random.randint(0, (barman - 1))].balance += tips    # barman从小费中赚的钱
            Pp[player].budget += pcost    # player花费的钱


        # Step 6.2: 决定player和bet，分配player到桌子上

        amount = []
        bet = []
        P_new = []
        for tnum in range(0, (numroulette + numcraps)):
            amount_temp = []
            bet_temp = []
            if tnum < numroulette:
                for i, num in enumerate(table):  # 是这个函数的返回值
                    if num == (tnum + 1):
                        if Pp[i].ptype == "returning":
                            Pp[i].amount = tablemin[tnum]  # return of this function
                        elif Pp[i].ptype == "onetime":
                            Pp[i].amount = random.randint(0, int(Pp[i].budget / 3))
                        else:
                            Pp[i].amount = random.randint(0, int(Pp[i].budget))
                        Pp[i].bet = random.randint(0, 36)
                        amount_temp.extend([Pp[i].amount])
                        bet_temp.extend([Pp[i].bet])
                        P_new.append(Pp[i])
                    else:
                        continue
            else:
                for i, num in enumerate(table):  # 是这个函数的返回值
                    if num == (tnum + 1):
                        if Pp[i].ptype == "returning":
                            Pp[i].amount = tablemin[tnum]  # return of this function
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


        bet_new = reduce(lambda x, y: x.extend(y) or x, [ i if isinstance(i, list) else [i] for i in bet])

        # Step 6.3: run every table
        for tnum in range(0, (numroulette + numcraps)):
            t = Table(tablemin[tnum])
            casinowin, croupiergain, playerwin = t.SimulateGame(bet[tnum], amount[tnum], tnum)
            C.balance += casinowin
            Cp[tnum].balance += croupiergain
            for player in range(0, len(playerwin)):
                P_new[player].gain += playerwin[player]
                P_new[player].budget -= bet_new[player]
                if P_new[player].budget == 0:
                    P_new[player].out = 1
                else:
                    continue
        P = P_new
        total = len(P)
        print(C.balance)
    return C.balance