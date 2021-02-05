import random

#list of possible inputs
choices = ['rock','paper','scissor']
#condition
game = 'True'

#if condition is True
while game == 'True' :
    comp = random.choice(choices)
    player = input('enter your choice : rock,paper or scissor ?')
    
    print('The computer chooses :',comp)
    #putting conditions
    if comp == player:
        print('Ties')
    elif player == 'rock' and comp == 'scissor':
        print('player wins')
    
    elif player == 'rock' and comp == 'paper':
        print('computer wins')

    elif player == 'paper' and comp == 'rock':
        print('player wins')

    elif player == 'paper' and comp == 'scissor':
        print('computer wins')

    elif player == 'scissor' and comp == 'paper':
        print('player wins')

    elif player == 'scissor' and comp == 'rock':
        print('computer wins')
    else :
        print('invalid input')
        exit()
    

