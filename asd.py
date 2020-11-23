a= [15, 2, 9, 4, 5, 6, 11, 1]


def max_profit(options):
    profits = []
    for i, buy_num in enumerate(options):
        for j, sell_num in enumerate(options[i:]):
            profits.append(sell_num - options[i])
    return max(set(profits))

print(max_profit(a))
