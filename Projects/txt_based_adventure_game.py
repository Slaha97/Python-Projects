""" Welcome to text based adventure game.
    The game goes as follows:-
    
                 user
                  |
               ___|_______________________________________________________
         (left)|                                                         | (right)
               |                                                         |
             Bear                                                      Snake
               |                                                         |
           _____________________                                         |___________________________
           |                    |(hide and sneak past it)         (sneak)|                          |(fight)
    (fight)|                    |                                        |                          |
           You Die              |___________      _______________________|                       You die
                                            |    |
                                        You reach Honey Room                       
                                              |
                     You try to  _____________|________________
                     take it    |                             |
                                |
                            Honeybees attack you           You are honest and you 
                            and you die                    get a free bottle of honey
                                
                     
"""


print('Welcome to text based Adventure Game')
print("------------------------------------")
print('Start\n')
print('')

def snake():
    e=input('Choose fight(f) or sneak(s): ')
    if e=='f':
        print('The snake bit you.You died')
    elif e=='s':
        honey()
            
    else:
        print('Invalid Choice')

def bear():
    act=input('Choose attack(a) or hide and sneak past it(hs): ')
    if act=='a':
        print('The bear Killed you.')
    elif act=='hs':
        print('Reached Honey room')
        honey()
    else:
        print('Invalid Choice')

def honey():
    g=input('Choose take(t) or leave(le): ')
    if g=='t':
        print('You are greedy.The honeybees attacked you.You died')
    elif g=='le':
        print('You are honest.You get a free bottle of honey')
        print('You win')
    else:
        print('Invalid Choice.')

d=input('Choose left(l) or right(r): ')
if d=='l':
    snake()
    
elif d=='r':
    bear()
    
else:
    print('Invalid Choice')
print('Game over.')


        

        

