import random

class LetsBegin(object):
    def __init__(self, numroulette, numcraps, Barman, Fixedwage, Cash, Total, Return, Bachelor, Free):
        self.numroulette = numroulette
        self.Crapstable = numcraps
        self.Croupier = numroulette + numcraps
        self.Barman = Barman
        self.Fixedwage = Fixedwage
        self.Cash = Cash
        self.Total = Total
        self.Return = Return
        self.Bachelor = Bachelor
        self.Free = Free

    # # 输入总数和三个type的百分比, 得到随机之后的customer
    # def Customertype(self):
    #     numreturn = int(self.Total * self.Return)
    #     numbachelor = int(self.Total * self.Bachelor)
    #     numonetime = self.Total - (numreturn + numbachelor)
    #     temp = []
    #     temp.append(["Return" for i in range(numreturn)])
    #     temp.append(["Onetime" for i in range(numonetime)])
    #     temp.append(["Bachelor" for i in range(numbachelor)])
    #     customer = random.shuffle(temp)
    #     return (customer)
    #
    # c = Customertype(self)

class Casino:
    def __init__(self, cash):
        self.cash = cash
        self.balance = cash

C = Casino(cash)

# class Employee(object):
#     def __init__(self, fixedwage, type, other):
#         self.wage = fixedwage
#         self.type = type
#         if self.type == "Croupier":
#             self.wage += other*0.005
#         else:
#             self.wage += other


class Croupier:
    def __init__(self, wage, gain):
        self.wage = wage
        self.gain = gain
Cp = []
for i in range(0, (numroulette + numcraps)):
    Cp[i] = Croupier.wage(wage, 0)       #这里的wage是外部输入的

class Barman:
    def __init__(self, wage, tips):
        self.wage = wage
        self.tips = tips

B = []
for i in range(0, (numroulette + numcraps)):
    B[i] = Barman.wage(wage, 0)         #这里的wage是外部输入的

# class Employee(object):
#     def __init__(self, wage):
#         self.wage = wage
#
# class Croupier(Employee):
#     def Wage(self, fixedwage, tablewin):
#         self.wage = fixedwage + tablewin*0.005
#         return self.wage
#
# class Barman(Employee):
#     def Wage(self, fixedwage, tips):
#         self.wage = fixedwage + tips
#         return self.wage

# class Customer(object):
#     def __init__(self, budget, type):
#         self.type = type
#         if self.type == "Returning":
#             self.budget = budget
#             self.balance = budget
#         elif self.type == "Onetime":
#             self.budget = random.randint(200,300)
#         else:
#             self.budget = random.randint(200,500)



class Player:
    def __init__(self, budget, ptype, amount, bet):
        self.budget = budget
        self.balance = budget
        self.ptype = ptype
        self.amount = amount
        self.bet = bet


def GetCtype(total, returning, bachelor):
    numreturn = int(total * returning)
    numbachelor = int(total * bachelor)
    numonetime = total - (numreturn + numbachelor)
    temp = []
    temp.append(["returning" for i in range(numreturn)])
    temp.append(["onetime" for i in range(numonetime)])
    temp.append(["bachelor" for i in range(numbachelor)])
    return (temp)

def GetBudget(ptype):
    budget = 0
    for item in ptype:
        if item == "returning":
            budget = random.randint(100,300)
        elif item == "onetime":
            budget = random.randint(200,300)
        else:
            budget = random.randint(200,500) + freebudget              # freebudget 需要敲定
    return budget

# First, initialize all the customers
ptype = GetPtype(total, returning, bachelor)
P = []
for i in range (0, total):
    budget = GetBudget(ptype)
    P[i] = Player(budget, ptype[i])

# Second, initialize all the tables and decide which table to go for each customer

# 生成和player人数相等的table数，用于分配player到各个table
def WhichTable(total, numroulette, numcraps):
    table = []
    for i in total:
        table[i] = random.choice(range(1, (numroulette + numcraps + 1)))
    return table

# #返回一个player的amount
# def MoneytoBet(tnum, ptype):
#     if ptype == "returing":
#         amount = TableMin(tnum)
#     elif ptype == "onetime":
#         amount = random.randint(0, int(P[i].balance/3))
#     else:
#         amount = random.randint(0, P[i].balance)
#     return amount
#
# # 返回一个player的bet
# def NumtoBet(tnum):
#     if tnum <= numroulette:
#         bet = random.randint(0, 36)
#     else:
#         bet = random.randint(2, 12)
#     return bet

# 每一个player买drink的情况
def Drink(balance):
    if balance >= 60:
        drink = random.randint(1, 2) * 20
        tips = random.randint(0, 20)
    else:
        drink = 0
        tips = 0
    cost = drink + tips
    return drink, cost, tips


class Table:
    def __init__(self, min):
        self.min = min
        self.weight = [36, 18, 12, 9, 7.2, 6, 7.2, 9, 12, 18, 36]
        self.casinowin = 0

    def SimulateGame(self, bets, amounts, tnum):                     # tnum 可以分辨ttype
        def AboveMinimum(amounts):
            result1 = []
            for amount in amounts:
                result1.append(bool(amount >= self.min))
            return (result1)

        if tnum <= numroulette:

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

# 返回所有table的最小amount
def TableMin(numroulette, numcraps):
    tablemin = []
    for i in range(1, (numroulette + numcraps +1)):
        if i <= numroulette:
            tablemin[i] = random.choice(50, 100, 200)
        else:
            tablemin[i] = random.choice(0, 25, 50)
    return tablemin

def TableResult(bet, amount, tnum):  #这里的tnum是指bet和amount来源的list里的位置
    if tnum <= numroulette:
        T = Table(tablemin)
        result = T.SimulateGame(bet, amount, tnum)
    else:
        T = Table(tablemin)
        result = T.SimulateGame(bet, amount,  tnum)
    return result[0], result[1], result[2]

cresult, cgain, presult = TableResult(bet, amount, tnum)
C.balance += cresult  # 赌场从赌博来的收入
C.balance += drink  # 赌场从饮料来的收入

for i in range(0, total):
    P[i].balance += presult[i]  #赌博的收入
    P[i].balance -= cost  #从drink函数里来，买饮料的支出

for i in range(0, (numroulette + numcraps + 1)):
    Cp[i].wage += cgain
    Cp[i].gain += cgain




# 决定player和bet，分配player到桌子上
amount_temp = []
amount = []
bet_temp = []
bet = []
for tnum in range(1, (numroulette + numcraps + 1)):
    if tnum <= numroulette:
        for i, num in enumerate(WhichTable(total, numroulette, numcraps)):  #是这个函数的返回值
            if num == tnum:
                if P[i].ptype == "returning":
                    P[i].amount = TableMin(numroulette, numcraps)[tnum]    #return of this function
                elif P[i].ptype == "onetime":
                    P[i].amount = random.randint(0, int(P[i].balance/3))
                else:
                    P[i].amount = random.randint(0, int(P[i].balance))
                P[i].bet = random.randint(0, 36)
                amount_temp = amount_temp.append(P[i].amount)
                bet_temp = bet_temp.append(P[i].bet)
            else:
                continue
    else:
        for i, num in enumerate(WhichTable(total, numroulette, numcraps)):  #是这个函数的返回值
            if num == tnum:
                if P[i].ptype == "returning":
                    P[i].amount = TableMin(numroulette, numcraps)[tnum]    #return of this function
                elif P[i].ptype == "onetime":
                    P[i].amount = random.randint(0, int(P[i].balance/3))
                else:
                    P[i].amount = random.randint(0, int(P[i].balance))
                P[i].bet = random.randint(2, 12)
                amount_temp = amount_temp.append(P[i].amount)
                bet_temp = bet_temp.append(P[i].bet)
            else:
                continue
    amount = amount.append([amount_temp])
    bet = bet.append([bet_temp])









