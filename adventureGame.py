print ('Welcome! Adventure Awaits!')
name = input ('What is your name? ')
print (name)
age = int(input('What is your age? '))


health = 10



if age >= 13:
    print ('you are old enough to play!')

    wants_to_play = input ('Do you want to play?').lower()
    if wants_to_play == 'yes':
        print('You are starting with', health, 'health')
        print ('Lets play!')

        left_or_right = input ('First choice. Left or Right (left/right)? ')
        if left_or_right == 'left':
            ans = input(' Follow the path and reached a lake. Do you swim across or go around (across/around)? ')
        
            if ans == 'around':
                print ('You went around and reached the other side of the lake')
            elif ans == 'across':
                print('You managed to get across, but were bit by a piranha and lost 5 health.')
                health -=5
            
            ans = input ('You see a house and a path. Which do you choose (house/path)? ')
            if ans == 'house':
                print ('You go into the house. You lose 5 health')
                health -=5

                if health <=0 
                    print ('Health is at 0, so you lose the game')
                else:
                    print('You Survived! You Win!')

            else:
                print ('You chose the path. You lost!')

        else:
            print ('You fell into a hole and lost!')

    else:
        print ('See you later!')
else:
    print ('You are not old enought to play!')
