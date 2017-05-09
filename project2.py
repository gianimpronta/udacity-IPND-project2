# -*- coding: utf-8 -*-
import time


def main():
    level = menu()
    clear()
    easy = ['''
    What was the name of R2-D2's sidekick? [__1__].
    What was the name of Han solo's partner? [__2__].
    Who was Luke's father? [__3__].
    Who was Leia's brother? [__4__].''', ['C3PO', 'Chewbacca', 'Darth Vader', 'Luke']]
    medium = ['''
    What was the real name of Darth Vader? [__1__].
    Anakin Skywalker used to compete in [__2__] races when he was a kid.
    What was the name of the anakin's archi-rival when he was a kid? [__3__].
    What was the name of planet which Anakin lived? [__4__]
    ''', ['Anakin Skywalker', 'Pod', 'Sebulba', 'Tatooine']]
    hard = ['''
    What was the color of Luke's lightsaber? [__1__].
    Who defeated Darth Maul? [__2__].
    What was the name of Anakin' owner when he was still a slave? [__3__]. 
    Who slavered princess Leia? [__4__].''', ['Blue', 'Obi Wan', 'Watto', 'Jabba the Hutt']]
    difficulties = [easy, medium, hard]
    questions(difficulties[int(level)])
    congrats()


def menu():
    """
    Prints the level selector and receives the player choice.
    :return: level
    :rtype: string
    """
    print '''
     _______.___________.    ___      .______         
    /       |           |   /   \     |   _  \        
   |   (----`---|  |----`  /  ^  \    |  |_)  |       
    \   \       |  |      /  /_\  \   |      /        
.----)   |      |  |     /  _____  \  |  |\  \----.   
|_______/       |__|    /__/     \__\ | _| `._____|   
____    __    ____  ___      .______          _______.
\   \  /  \  /   / /   \     |   _  \        /       |
 \   \/    \/   / /  ^  \    |  |_)  |      |   (----`
  \            / /  /_\  \   |      /        \   \    
   \    /\    / /  _____  \  |  |\  \----.----)   |   
    \__/  \__/ /__/     \__\ | _| `._____|_______/    
                                                      
         Welcome to the Star Wars Trivia!    
    '''
    time.sleep(2)
    while True:
        print '''   
###################################
Please choose your quiz level:
0 - easy
1 - medium
2 - hard

Your choice:'''
        level = raw_input()
        if level in ('0', '1', '2'):
            difficulties = ['easy', 'medium', 'hard']
            print '''
###################################
This the %s level. May the Force be with you!''' % difficulties[int(level)]
            break

    return level


def questions(level):
    """
    Receives a list that contains the questions and answers for the chosen level. 
    :param level: level of difficulty chosen by the player
    :type level: list
    """
    question = level[0]
    answers = level[1]
    guessed = 0
    while guessed < 4:
        if guessed != 0:
            question = question.replace('[__%d__]' % guessed, answers[guessed - 1])
        while True:
            print question + '\n' + '-' * 60
            if guessed == 0:
                print 'What\'s the answer for the 1st question?'
            else:
                print 'What\'s the answer for the next question?'
            user_answer = raw_input().lower()
            if user_answer == answers[guessed].lower():
                guessed += 1
                print 'Nice!'
                time.sleep(0.5)
                break
            else:
                print 'Wrong!\nTry again!'
                time.sleep(1)
        clear()


def clear():
    """
    Clears the screen.
    :return: 
    :rtype: 
    """
    print '\n' * 1000


def congrats():
    """
    Congratulates player, end the game.
    :return: 
    :rtype: 
    """
    print 'YOU WON!!'
    time.sleep(0.5)
    print '''
.___________.__    __       ___      .__   __.  __  ___    ____    ____  ______    __    __            
|           |  |  |  |     /   \     |  \ |  | |  |/  /    \   \  /   / /  __  \  |  |  |  |           
`---|  |----|  |__|  |    /  ^  \    |   \|  | |  '  /      \   \/   / |  |  |  | |  |  |  |           
    |  |    |   __   |   /  /_\  \   |  . `  | |    <        \_    _/  |  |  |  | |  |  |  |           
    |  |    |  |  |  |  /  _____  \  |  |\   | |  .  \         |  |    |  `--'  | |  `--'  |           
    |__|    |__|  |__| /__/     \__\ |__| \__| |__|\__\        |__|     \______/   \______/            
 _______   ______   .______         .______    __          ___   ____    ____  __  .__   __.   _______ 
|   ____| /  __  \  |   _  \        |   _  \  |  |        /   \  \   \  /   / |  | |  \ |  |  /  _____|
|  |__   |  |  |  | |  |_)  |       |  |_)  | |  |       /  ^  \  \   \/   /  |  | |   \|  | |  |  __  
|   __|  |  |  |  | |      /        |   ___/  |  |      /  /_\  \  \_    _/   |  | |  . `  | |  | |_ | 
|  |     |  `--'  | |  |\  \----.   |  |      |  `----./  _____  \   |  |     |  | |  |\   | |  |__| | 
|__|      \______/  | _| `._____|   | _|      |_______/__/     \__\  |__|     |__| |__| \__|  \______| 
                                                                                                       
    '''


if __name__ == '__main__':
    main()
