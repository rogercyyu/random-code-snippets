# Russian Roulette

import random
import time, sys

print('Russian Roulette'.center(75, '-'))

#Set up game.
gun =   r"""                    ,                                               ,
                     @"===,                                  ,_____cctI
                     "?AAAAAAAAAAAAAAAA,,,,,,,,,,,,,,,,,,,,,;LLLLLLLLLL
           ~",,,      1"'''''''''''###OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
            '"EEEEE, !'"***"~~~~~~"OOOIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
               ,EEEEE)>"'''???????"WWW!MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                "E.,)+="WWW~~~~~~#"OOO1OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
             ,~:#")LLL!"+++???????"$$$1==========##/
              &LLLLLLLLL;;;;;;;;;;;;,,,/
              1#LLLLLLLLLLLLLLLLLLLLLL!
            ,!###LLLLLL"'EEEE,'"LLLLL!
            !######LLL"  "EEE"  "LLLL"
           !#########L!   "EEJ. "LL!
          !##########1      "JJ*,l"
         !############"!       ,l"
         1##########"  1"~~,~~"
        !##########"
       !###########!
       !###########1
      !############!
      1#############
     !"#############"
     !##############!
     1##########"'                             
     1#####"'

"""
print(gun)




def gungame():
    print('You put the gun to your head.')
# ask the player to pull the trigger.
    input('Do you dare pull the trigger? (Press ENTER)')
    
##    for i in range(5):
##        sys.stdout.write("   ")
##        x = i % 4
##        sys.stdout.write('\r' + "." * x )
##        time.sleep(0.5)y
##        sys.stdout.flush()
    tries = 0
    click = random.randint(0,6)
    while click > 0:
        print('*click*')
        print('You live for now. ')
        click -= 1
        tries += 1
    else:
        print('Bang! You have died.')
        print('You have lived, ' + str(tries) + ' times.')
        tires = 0
 
    
#play game.
while True:
    gungame()
    while True:
        answer = input('Would you like to try again? (y/n):')
        if answer in ('y','n'):
            break
    if answer == 'n':
        print('Too bad, you must play this game.')

    

    
    
