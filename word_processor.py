from functools import reduce
from typing import Text


def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def char_lower(char:str) :
    """
    Converts an alphabet character to lowercase

    Args:
        char (str): single character string 

    Returns:
        str: lowercase char
    """
    try:
        char[0]
    except:
        return '' 
    return  (
                chr(ord(char) + 32)
                if 64 < ord(char) < 91
                else char
            )


def lower(text:str):
    """
    Converts text to lowercase

    Args:
        text (str): text to be converted

    Returns:
        str: lowercase text
    """
    try:
        text[0]
    except:
        return ''
    return  str(
                reduce(
                    lambda c1, c2:
                        c1 + char_lower(c2),
                    char_lower(text[0])+text[1:]
                )
            )           


def leng(iterable):
    """
    Finds the length of a given iterable object

    Args:
        iterable (iterable object): the iterable to be counted

    Returns:
        int: the length of the iterable,
             0 if not an iterable or empty
    """
    try:
        return [*enumerate(iterable)][-1][0]+1
    except:
        return 0
    

def convert_to_word_list(text:str, delimeters:list = [',',';',' ','?',"."]):
    """
    Converts a string of words into a list of lower case words
    stripped of delimeters.


    Args:
        text (str): string to convert to list.
        delimeters (list, optional): strings to separate by.
        Defaults to [',',';',' ','?',"."].

    Returns:
        list: list of stripped lowercase words.
    """
    return  [
                *filter(
                    lambda word : 
                        word != '',
                    map(
                        lambda word : 
                            (lower(word)[:-1]
                            if word[-1] in delimeters 
                            else lower(word))
                            if word != '' 
                            else '',
                        split(
                            delimeters,
                            text)
                        )
                    )
            ]


def words_longer_than(length:int, text:str):
    """
    Filters text to be a list of all the words of length.

    Args:
        length (int): length of words in list.
        text (str): string to convert to list.

    Returns:
        list: list of strings, all have length of length.
    """
    return  [
                *filter(
                    lambda word :
                        leng(word) >= length,
                    convert_to_word_list(text) 
                    )
            ]


def words_lengths_map(text):
    """
    Returns how many words occur of each length.

    Args:
        text (str): string to map lengths of.

    Returns:
        dict: maps a word length.
            * Key (int): represents the length of the word.
            * Value (int): how many words of of that length there are.
    """
    words = convert_to_word_list(text)
    my_dictionary = dict()
    return  dict(
                map(
                    lambda key :
                        (
                            key,
                            leng(
                                [
                                *filter(
                                    lambda word :
                                        leng(word) == key,
                                        words
                                    )
                                ]
                            )
                        ),
                    set(
                        map(
                        lambda word :
                            leng(word),
                            words
                        )
                    )
                )
            )
    

def letters_count_map(text, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    return  dict(
                map(
                    lambda key :
                        (
                            key,
                            leng(
                                [
                                *filter(
                                    lambda char :
                                        char == key,
                                        lower(text)
                                    )
                                ]
                            )
                        ),
                    alphabet
                )
            )


def most_used_character(text:str):
    char_map =  letters_count_map(text)
    max_char =  reduce(
                    lambda char1, char2:
                        char1 
                        if char_map[char1] > char_map[char2] 
                        else char2,
                    [*char_map]
                )
    return  (
                max_char
                if char_map[max_char] > 0 
                else None
            )   


# print(convert_to_word_list("Hello World! I'm bob, your uncle."))
# print(words_lengths_map("Hello World! I'm bob, your uncle."))
# print(*letters_count_map("Hello World! I'm bob, your uncle.").items(), sep = "\n")
# print(most_used_character("Hello World! I'm bob, your uncle."), sep = "\n")
# print(most_used_character("H"), sep = "\n")
# import time
# str = 1000000*'s'
# start_time = time.time()
# for _ in  range(100):
#     # len("abced")
#     # words_lengths_map("Hello World! I'm bob, your uncle.")
#     leng(str)
#     # lower("Hello World! I'm bob, your uncle. h")
# print ("Mine took", time.time() - start_time, "to run")

# start_time = time.time()
# for _ in  range(100):
#     len(str)
# print ("Theirs took", time.time() - start_time, "to run")
# print(leng("abced"))
# print(lower("Hello World! I'm bob, your uncle. h"))


# def leng(iterable):
    #enumerate + error checking - not necessary - 2nd fastest
    # try:
    #     return [*enumerate(iterable)][-1][0]
    # except:
    #     return 0

    # reduce function - slowest
    # try:
    #     iterable[0]
    # except:
    #     return 0
    
    # try:
    #     iterable[1]
    # except:
    #     return 1

    # return  int(
    #             reduce(
    #                 lambda f, _: 
    #                     (f if isinstance(f, int) 
    #                     else 1) + 1,
    #                 iterable
    #             )
    #         )

    #recursion - 3rd fastest
#def leng(iterable, index = 0):
    # try:
    #     iterable[index]
    #     return leng(iterable, index+1)
    # except:
    #     return index