#entry value
from main_formated_output import *

entry = ''

def entry_func():
    keyword = ['now @ ', 'IT @ ', 'now at ', 'now ', 'SELL @ ', 'BUY ', 'SELL ', 'limit @ ', 'BUY @ ']
    cnt = 0
    for str in strg:
        cnt += 1
        print(cnt)
        for keywrd in keyword:
            if str.find(keywrd) == -1:
                continue
            else:
                for i in range(0, len(str), 1):
                    if str[i:i+len(keywrd)] == keywrd:
                        
                        index = i + len(keywrd)
                        user_input = str[index:].split()[0]

                        if is_float(user_input):   #'SL @ 0.9585(31 pips)'
                            entry = (clean_float_string(user_input))
                            return(entry)
                        else:
                            pass
        

