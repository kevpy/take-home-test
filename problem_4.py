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
    B = stock_list.index(min(stock_list))
    buy_value = min(stock_list)

    sell_value = -1
    if buy_value > 1:
        for sell_indx in range(B, len(stock_list)):
            if sell_value < stock_list[sell_indx]:
                sell_value = stock_list[sell_indx]
                S = sell_indx
    else:
        return 'Buy stock first'
    return [B, S]


P = [30, 20, 10, 15, 17, 25, 20, 23]

recomendation = stock_analyst(P)
if isinstance(recomendation, list):
    print('B = {}' .format(recomendation[0]))
    print('S = {}' .format(recomendation[1]))
else:
    print(recomendation)
