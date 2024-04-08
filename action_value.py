#action buy or sell
from main_formated_output import *

action = ''

def action_func():
    keyword = ['BUY', 'SELL', 'Buy', 'Sell', 'buy', 'sell']

    cnt = 0

    for str in strg:
        cnt += 1
        print(cnt)
        for keywrd in keyword:
            if str.find(keywrd) == -1:
                continue
            else:
                action = keywrd.title()
                return(action)

