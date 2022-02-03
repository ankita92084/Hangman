import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    # word_list = ["navgurukul", "learning", "kindness"]
    # word_list= "words.txt"
    word_list=open("hangman/words.txt","r")
        # data=file.read()
    print(word_list)
    line=word_list.readline()
    word_list=line.split()
    return word_list
    # word_list = ["navgurukul", "learning", "kindness"]
    # return word_list
load_words()

def choose_word():
    
    # word_list (list): list of words (strings)--
    # ye function ek word randomly return karega
    
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word
choose_word