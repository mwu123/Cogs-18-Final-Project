"""A collection of function for doing my project."""

import string
import random
import nltk

# copied from Cogs 18 Assignment 3: Chatbots
def end_chat(message):
    """
    End the chat if user inputs certain words to signify the termination of the chat.
    
    Parameters
    ----------
    input_list: string
        User types words like 'quit' or 'give up' to end game.
        
    Returns
    -------
    ouput: boolean
        True or False to end game/chat
    """
    
    #if the word "quit" appears in user's input, the chat will end
    if 'quit' in message:
        return True
    else:
        return False

    
# copied from Cogs 18 Assignment 3: Chatbots
def selector(input_list, check_list, return_list):
    """
    Check a list of words to see if they appear as user's input and 
    return an output from a list of possible words in response to input
    
    Parameters
    ----------
    input_list: string
        The user's input 
    check_list: string
        A list of possible words in the system that user might input 
    return_list: string
        A list of possible words to respond to user's input 
        
    Returns
    -------
    output: string
        A random word from the response list will be return
    """
    
    output = None
    
    #check to see if input_list exists in check_list, if so return something from return_list 
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break
            
    return output


GREETING_INPUT = ['Hi','Hello','Hey','Sup'] #posible greeting inputs
GREETING_OUTPUT = ['Hello!','Hi, nice to meet you!','Welcome!'] #possible greeting outputs


def choose_word(message):
    """
    Randomize and choose words based on difficulty chosen by user
    
    Parameters
    ----------
        message: string
            The input to select level of difficulty
    
    Returns
    -------
        chosen_word: string
            The chosen word that the user will guess the letters 
    """
    
    #lists of words depending on difficulty 
    easy_words = ["strawberry", "orange", "watermelon"]
    medium_words = ["guava", "pineapple", "durian"]
    hard_words = ["mangosteen", "rambutan", "starfruit"]
    
    chosen_word = 'python'#default chosen word
    
    #return a word based on the level of difficulty chosen 
    if 'easy' in message:
        chosen_word = random.choice(easy_words)
    elif 'medium' in message:
        chosen_word = random. choice(medium_words)
    elif'hard' in message:
        chosen_word = random.choice(hard_words)
        
    return chosen_word


def game():
    """Convert the randomized chosen word, turn it into an unknown word, user had to guess the unknown word"""
    
    message = input()
    chosen_word = choose_word(message)
    num_tries = len(chosen_word) *2
    unknown_word = '*' * len(chosen_word) #convert chosen word to * symbol
    unknown = []
    
    #convert chosen word to unknown 
    for i in range(0, len(chosen_word)):
        unknown.append("*")
    chosen = list(chosen_word) #separated into array of letters
    
    print('Guess the unknown letters', unknown_word)
    
    #allow the user to play the game as long as the num of tries is not 0 
    while num_tries > 0:
        
        if '*' not in unknown:
            print(['Congratulation']) 
        else:
            print("Enter a letter") 
            
        message = input('INPUT :\t')
      
        if message in chosen:
            output = ['Correct']
            print(output)
            
            #find index of input letter and reveal the letter if it is correct 
            while ("".join(chosen)).find(message) != -1:
                char_index = ("".join(chosen)).find(message) 
                unknown[char_index] =  message 
                chosen[char_index] = '*'
            print("".join(unknown))
            
        else:
            output = ['Try Again']
            print(output)
            print ("".join(unknown))
        
        num_tries = num_tries - 1 
        
        
# modified from Cogs 18 Assignment 3: Chatbots
def conversation():
    """Converse with the user based on the input"""
    
    chat = True
    
    while chat:
        
        message = input('INPUT :\t')
        out_message = None
        
        #end the chat and say Bye to user
        if end_chat(message):
            out_message = 'Bye!'
            chat = False
            
        if not out_message: 
            output = []
            output.append(selector(message, GREETING_INPUT, GREETING_OUTPUT))
            output = ["Do you want to play a game?"]
            
            #if user want to play game, then ask to choose a difficulty
            if message == "yes":
                output = 'Choose level of difficulty: easy, medium, hard'
                print('OUTPUT:', output)
                choose_word(message)
                game() 
            # if user does not want to play game, end chat   
            elif message == 'no':
                chat = False
                output = ["No problem, see you next time!"]
                        
            options = list(filter(None, output))
            if options:
                out_message = random.choice(options)

        print('OUTPUT:', out_message)
     