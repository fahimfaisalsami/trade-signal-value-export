#SL Stop Loss value
from main_formated_output import *

tp1 = ''

def tp1_func():
    keyword = ['Take profit ', 'Take profit @ ', 'tp @ ', 'TP: ', 'TP ', 'tp ', 'target ', 'Target ', 'target:', 'Target:', 'TP1 ']
    cnt = 0

    for str in strg:
        cnt += 1
        print(cnt)
        found_tp = False
        for keywrd in keyword:
            if str.find(keywrd) == -1:
                continue
            else:
                for i in range(0, len(str), 1):
                    if str[i:i+len(keywrd)] == keywrd:
                        index = i + len(keywrd)
                        user_input = str[index:].split()[0]

                        if is_float(user_input):
                            tp1 = (clean_float_string(user_input))
                            return(tp1)
                            found_tp = True
                            break  # Break out of the loop once the first TP value is found
                        else:
                            pass
            if found_tp:
                break  # Break out of the outer loop once the first TP value is found

