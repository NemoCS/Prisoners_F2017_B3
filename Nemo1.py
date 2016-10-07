team_name = 'Nemo1' # Only 10 chars displayed.
strategy_name = 'Betray then Tit for Tat'
strategy_description = 'Messes up the strategies that betray forever. Starts betraying forever if it gets fed up.'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'b'
    elif their_history[-1]=='b':
        return 'b'
    elif len(their_history) >3:
        if their_history[-4:] == 'bbbb':
            return 'b'
    else:
        return 'c'
