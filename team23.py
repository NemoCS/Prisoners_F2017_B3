#Team 23: Kris and Kyle
team_name = 'Obey' # Only 10 chars displayed.
strategy_name = 'given'
strategy_description = 'Messes up second place team from first game'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)%2 == 0:
        return 'c'
    else:
        return 'b'
 
        