from functools import reduce


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


def lower(text:str):
    return  str(
                reduce( lambda c1, c2: c1+c2,
                        map(
                            lambda char:
                                chr(ord(char) + 32)
                                if 64 < ord(char) < 91
                                else char,
                            text
                        )
                )
            )


def length(iterable):
    return  int(
                reduce(
                    lambda x, y : x + y,
                    map(
                        lambda _: 1,
                        iterable
                    )
                )
            )


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
                            (word.lower()[:-1]
                            if word[-1] in delimeters 
                            else word.lower())
                            if word != '' 
                            else '',
                        split(
                            delimeters,
                            text)
                        )
                    )
            ]


def words_longer_than(length:str, text:int):
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
                        len(word) >= length,
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
                            len(
                                [
                                *filter(
                                    lambda word :
                                        len(word) == key,
                                        words
                                    )
                                ]
                            )
                        ),
                    map(
                        lambda word :
                            len(word),
                            words
                    ) 
                )
            )
    

def letters_count_map(text, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    return  dict(
                map(
                    lambda key :
                        (
                            key,
                            len(
                                [
                                *filter(
                                    lambda char :
                                        char == key,
                                        text.lower()
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
print(length("abced"))
print(lower("Hello World! I'm bob, your uncle."))


