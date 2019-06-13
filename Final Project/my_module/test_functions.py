"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import random
import string
import nltk
from my_module.functions import choose_word
from my_module.functions import game
    
    
#test choose_word function 
def test_choose_word():
    
    message == 'hard'
        assert chosen_word in ["mangosteen", "rambutan", "starfruit"]
    message == 'medium'
        assert chosen_word in ["guava", "pineapple", "durian"]

    
#test game function
def test_game():
    
    chosen_word = 'strawberry'
        assert num_tries == 20
    
    if message == 'a':
        assert 'Correct' in output
    elif message == 'c':
        assert 'Try Again' in output