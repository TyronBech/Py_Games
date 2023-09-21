import random
import os

class Hangman(object):
    HANGINGMAN = [
        '''
        +---+
        |   |
        |   
        |
        |
        [========]''',
        '''
        +---+
        |   |
        |   O
        |
        |
        [========]''',
        '''
        +---+
        |   |
        |   O
        |   |
        |
        [========]''',
        '''
        +---+
        |   |
        |   O
        |  /|
        |
        [========]''',
        '''
        +---+
        |   |
        |   O
        |  /|\\
        |
        [========]''',
        '''
        +---+
        |   |
        |   O
        |  /|\\
        |  /
        [========]''',
        '''
        +---+
        |   |
        |   O
        |  /|\\
        |  / \\
        [========]'''
    ]
    WORDBANK = ['HAPPY', 'BIRTHDAY', 'HYDROPHOBIC', 'COMPUTER', 'MOUSE', 'LAPTOP', 'PILLOWS',
                'SNOWMAN', 'ABOVE', 'ABOUT', 'AFTER', 'AGAIN', 'AGREE', 'ALL', 'ALONE',
                'ALONG', 'ALMOST', 'ALSO', 'PYTHON', 'JAVA', 'ROBUST', 'ANY', 'ARE', 
                'OUTSTANDING', 'KEYBOARD', 'AWAY']
    def __init__(self):
        self.Word_to_Guess = random.choice(self.WORDBANK)
        self.Gameplay()
    def Dict_word(self, GOTWORD):
        dict_count = dict()
        for index, charac in enumerate(GOTWORD):
            if charac in dict_count:
                dict_count[charac].append(index)
            else:
                dict_count[charac] = [index]
        return dict_count
    def Check_guess(self, underscores, guess, dict_coll):
        list_underscores = [char for char in underscores]
        if guess.isdigit():
            print('The entered guess was a digit')
            return (underscores, False)
        elif guess in underscores:
            print("The letter is already been selected")
            return (underscores, False)
        elif len(guess) == 1 and guess in dict_coll:
            for index in dict_coll[guess]:
                list_underscores[index] = guess
            underscores = ''.join(list_underscores)
            return (underscores, True)
        elif len(guess) > 1 and guess == self.Word_to_Guess:
            return (self.Word_to_Guess, True)
        else:
            if len(guess) == 1:
                print('The guessed letter does not exist in the word')
            else:
                print('The guessed word is wrong')
            return (underscores, False)
    def Gameplay(self):
        print('HANGMAN GAME!!!')
        i = 0
        underscore_word = '_' * len(self.Word_to_Guess)
        char_locations = self.Dict_word(self.Word_to_Guess)
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
            print(self.HANGINGMAN[i])
            print()
            print('\t' + underscore_word)
            print()
            user_guess = input('Enter a letter or word if you know the answer: ')
            underscore_word, flag = self.Check_guess(underscore_word, user_guess.upper(), char_locations)
            if not flag:
                i += 1
            elif underscore_word == self.Word_to_Guess:
                print(underscore_word)
                print('Congratulations! You guessed the word and\nsaved the man')
                break
            if i == len(self.HANGINGMAN):
                print('Sorry, you lose the game')
                print('The correct word is: ' + self.Word_to_Guess)
                break
            input('Press Enter to continue...')

if __name__ == '__main__':
    Game = Hangman()
