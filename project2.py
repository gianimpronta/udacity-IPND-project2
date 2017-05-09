# -*- coding: utf-8 -*-
import time


def main():
    level = menu()
    clear()
    easy = ["What was the name of R2-D2's sidekick? [__1__].\nWhat was the name of Han solo's partner? [__2__].\n"
            "Who was Luke's father? [__3__].\nWho was Leia's brother? [__4__].",
            ['C3PO', 'Chewbacca', 'Darth Vader', 'Luke']]
    medium = [
        "What was the real name of Darth Vader? [__1__].\nAnakin Skywalker used to compete in [__2__] races when he was a kid.\n"
        "What was the name of the anakin's archi-rival when he was a kid? [__3__].\nWhat was the name of planet which Anakin lived? [__4__]",
        ['Anakin Skywalker', 'Pod', 'Sebulba', 'Tatooine']]
    hard = [
        "What was the color of Luke's lightsaber? [__1__].\nWho defeated Darth Maul? [__2__].\nWhat was the name of Anakin' owner when he was still a slave? [__3__].\nWho slavered princess Leia? [__4__].",
        ['Blue', 'Obi Wan', 'Watto', 'Jabba the Hutt']]
    difficulties = [easy, medium, hard]
    questions(difficulties[int(level)])
    congrats()


def menu():
    """
    Prints the level selector and receives the player choice.
    :return: level
    :rtype: string
    """
    logo()
    time.sleep(2)
    while True:
        print "###################################\nPlease choose your quiz level:\n- easy\n- medium\n- hard\n\nYour choice:"
        level = ['easy', 'medium', 'hard'].index(raw_input().lower())
        if level in [0, 1, 2]:
            print "###################################\nThis the %s level. May the Force be with you!" % \
                  ['easy', 'medium', 'hard'][level]
            break
    time.sleep(1)
    return level


def logo():
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

def questions(level):
    """
    Receives a list that contains the questions and answers for the chosen level. 
    :param level: level of difficulty chosen by the player
    :type level: list
    """
    question, answers = level[0], level[1]
    guessed = 0
    while guessed < len(answers):
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
