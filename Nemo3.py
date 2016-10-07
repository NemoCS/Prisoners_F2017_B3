team_name = 'Nemo3' # Only 10 chars displayed.
strategy_name = 'Succeed stay, fail switch'
strategy_description = 'Tit for Tat with a chance of forgiving betray.'

import random

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'c'
    #suckered: switch to betray
    elif their_history[-1]=='b' and my_history[-1] =='c':
        return 'b'
    #repeated betray: betray back
    elif len(their_history) >3:
        if their_history[-4:] == 'bbbb':
            return 'b'
    #mutual betray: switch to collude
    elif their_history[-1]=='b' and my_history[-1] =='b':
        return 'c'
    #betrayed successfully: betray again
    elif my_history[-1]=='b' and their_history[-1]=='c':
        return 'b'
    #else if colluding successfully, continue colluding.
    else:
        return 'c'