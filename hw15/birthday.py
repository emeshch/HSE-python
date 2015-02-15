from numpy import *
# import matplotlib.pyplot as plt

def mean_hits(n, e):
    """

    """
    days = 10  # 365
    days_exp = zeros((e, days))
    for i in range(n):
        birthdays = random.random_integers(0, days-1, e)
        # bd = birthdays.shape
        days_exp[arange(e), birthdays] += 1  # table
        # print('ind ', birthdays, '=========')
    print('array\n', days_exp)
    hits = (days_exp > 1).sum(1)
    mean_hits = mean(hits)
    print('!', hits, '\n', mean_hits)

# mean_hits(2, 30)
def parad(n, e):
    """

    """
    days = 10  # 365
    days_exp = zeros((e, days))
    for i in range(n):
        birthdays = random.random_integers(0, days-1, e)
        days_exp[arange(e), birthdays] += 1
    print('array\n', days_exp)
    days_exp[days_exp <= 1] *= 0
    days_exp[days_exp > 1] = (days_exp[days_exp > 1])*(days_exp[days_exp > 1] - 1)/2
    hits = days_exp.sum(1)
    print('!', days_exp)
    print('======')
    print(hits)

parad(23, 10)





















