team_name = 'Nemo2' # Only 10 chars displayed.
strategy_name = 'Generous Tit for Tat'
strategy_description = 'Tit for Tat with a chance of forgiving betray.'

import random

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    #repeated betray: betray back
    #elif len(their_history) >3:
    #    if their_history[-4:] == 'bbbb':
    #        return 'b'
    elif their_history[-1]=='b':
        if random.choice(range(15)) == 0:
            return 'c'
        else:
            return 'b'
    else:
        return 'c'
