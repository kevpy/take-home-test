def stock_analyst(stock_list):
    """This function accepts a list of data P and outputs the best day to
    buy(B) and sell(S) stock.

    Args:
        stock_list: expects a list of stocks as a parameter

    Returns:
        a string promting to buy stock if one has not bought stock i.e the
        value of stock is less than 1
        If the value of stock is > 0 it returns the best days to stock at
        value and sell stock at maximum value
    """
    buy_date = stock_list.index(min(stock_list))
    B = min(stock_list)

    S = -1
    if B < 1:
        for sell_indx in range(buy_date, len(stock_list)):
            if S < stock_list[sell_indx]:
                S = stock_list[sell_indx]
    return [B, S]


P = [30, 20, 10, 15, 17, 25, 20, 23]

recomendation = stock_analyst(P)
if isinstance(recomendation, list):
    print('B = {}' .format(recomendation[0]))
    print('S = {}' .format(recomendation[1]))
else:
    print(recomendation)
