# Features to be tracked, per card basis
'''
Data collected:

    Difficulty - 1 to 5
    Forgot - t/f, 1/0
    total Number of tests (NoT)- positive integer
    Time Reviewed at (TR)- string in datatime format
    Time Passed since last review (TP)- number of hours since last completion
    Answered Correctly this review (AC0) - t/f, 1/0
    Answered Correctly last review (AC1)- t/f, 1/0 
    Answered Correctly two reviews ago (AC2)- t/f, 1/0 
    word- collected for indexing purposes
'''
import pandas as pd
import numpy as np
from os.path import exists
import random
import datetime

class App:

    def __init__(self):
        # add cards to deck
        self.deck = dict()
        self.deck['vergessen'] = 'forget'
        self.deck['irgendwelche'] = 'any'
        self.deck['geschichten'] = 'stories'
        self.deck['wahrscheinlich'] = 'probably'
        self.deck['irgendetwas'] = 'anything'
        self.deck['schaffen'] = 'create'
        self.deck['erfahren'] = 'experienced'

        self.df = pd.DataFrame(columns=['diff', 'forgot', 'NoT', 'TR', 'TP', 'AC0', 'AC1', 'AC2', 'word'])

    # displays all the cards
    def review(self):
        print('Review Mode')
        print('*' * 30)
        for key, val in self.deck.items():
            print(key, '=', val)

    # tests user on all words in deck
    def test(self):
        self.df = pd.DataFrame(columns=['diff', 'forgot', 'NoT', 'TR', 'TP', 'AC0', 'AC1', 'AC2', 'word'])
        print('*\n'*50)                   # print new lines in case cards were just reviewed to get them out of eye view
        print('Flashcard Deck Test Mode\n')
        words = random.sample(self.deck.keys(), len(self.deck.keys()))

        for word in words:
            print('flashcard:', word)
            ans = input('Answer: ')
            if ans == self.deck[word]:
                print('Nice, you got that one right')
                self.log(word, 1)
            else:
                print('sorry, not right')
                self.log(word, 0)
            print( '*'*30)


    # save metrics before leaving session
    def exit(self):
        self.df.set_index(['word', 'TR'], inplace=True)
        self.df.sort_index(inplace=True)

        if not exists('./metrics.csv'): 
            self.df.to_csv('./metrics.csv')
        else:
            data = pd.read_csv('./metrics.csv')
            data.set_index(['word', 'TR'], inplace=True)
            data = pd.concat([data, self.df], levels=['word', 'TR'])
            data.sort_index(inplace=True)
            data.to_csv('./metrics.csv')

        print('Goodbye.')


    # collects data by concatenating self.df  w/ one row of new data
    def log(self, word: str, correct: bool):
        diff = input(f'How difficult was {word}? (answer w/ a number 1-5): ')
        forgot = input(f'Did you forget {word}? (y/n): ')
        forgot = 1 if forgot == 'y' else  0                  # convert from string to int

        date = datetime.datetime.now()

        entry = pd.DataFrame({'diff': [diff], 'forgot': [forgot], 'TR': [date], 'AC0': [correct], 'word': [word]})    
        self.df = pd.concat([self.df, entry], ignore_index=True)    

'''
        x = {'diff': [1, 0], 'forgot': [1, 0], 'NoT': [1, 0], 'TR': [1, 0], 'TP': [1, 0], 'AC0': [1, 0], 'AC1': [1, 0], 'AC2':[1, 0], 'word': ['wahnsinnig', 'irgendetwas']} 
        test = pd.DataFrame(x)                    # include index b/c instatiating one row w/ values that are scalars, not lists.

        test2 = pd.DataFrame({'diff': [2, 5], 'forgot': [2, 5], 'NoT': [2, 5], 'TR': [2, 5], 'TP': [2, 5], 'AC0': [2, 5], 'AC1': [2, 5], 'AC2':[2, 5], 'word': ['wahnsinnig', 'irgendetwas']})
        self.df = pd.concat([self.df, test, test2], ignore_index=True)

        self.df.set_index(['word', 'TR'], inplace=True)
        self.df.sort_index(inplace=True)
        print(self.df)

        test3 = pd.DataFrame({'diff': [8], 'forgot': [8], 'NoT': [8], 'TR': [8], 'TP': [8], 'AC0': [8], 'AC1': [8], 'AC2': [8], 'word': ['irgendetwas']})
        test3.set_index(['word', 'TR'], inplace=True)
        self.df = pd.concat([self.df, test3], levels=['word', 'TR'])


        test4 = pd.DataFrame({'diff': [9], 'forgot': [9], 'NoT': [9], 'TR': [9], 'TP': [9], 'AC0': [9], 'AC1': [9], 'AC2': [9], 'word': ['irgendetwas']})
        test4.set_index(['word', 'TR'], inplace=True)
        self.df = pd.concat([self.df, test4], levels=['word', 'TR'])

        self.df.sort_index(inplace=True)
        print(self.df)
'''
