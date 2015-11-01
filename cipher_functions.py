# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the 
# code that you submit.  Do not use break or continue statements.


def clean_message(msg):
    """ (str) -> str
    
    Return a copy of the message that includes only its alphabetical 
    characters, where each of those characters has been converted to uppercase.
    
    >>> clean_message(I like eat food.)
    'ILIKEEATFOOD'
    
    >>> clean_message(?>??!!!23123123)
    ''    
    """
    clean_msg = ''
    
    for character in msg:
        if character.isalpha():
            clean_msg += character.upper()
            
    return clean_msg


def encrypt_letter(letter, keystream_value):
    """ (str, int) -> str

    Apply the keystream value to the letter to encrypt the letter, and return the result.

    >>> encrypt_letter('A',0)
    'A'

    >>> encrypt_letter('X',23)
    'U' 
    """
    return chr(65 + (ord(letter) - 65 + keystream_value) % 26)
    
def decrypt_letter(letter, keystream_value):
    """ (str, int) -> str

    Apply the keystream value to the letter to decrypt the letter, and return the result.

    >>> decrypt_letter('B',23)
    'E'

    >>> decrypt_letter('L',8)
    'D'
    """
    letter_code = ord(letter) - 65 -keystream_value
    if letter_code >= 0:
        return chr(65 + letter_code % 26)
    else:
        return chr (65 + (letter_code + 26))


def swap_cards(deck, index):
    """ (list of int, int) -> NoneType
 
    Swap the card at the index with the card that follows it. 
    Treat the deck as circular: if the card at the index is on the bottom of the deck, 
    swap that card with the top card.

    >>> deck = [0,1,2,3,5,6,7]
    swap_cards(deck, 2)
    deck = [0,1,3,2,5,6,7]

    >>> deck = [0,1,2,3,5,6,7]
    swap_cards(deck, 6)
    deck = [7,1,2,3,5,6,0]
    """
    temp = deck[index]
    next_index = (index+1) % len(deck)# ensure the next index is in the range
    deck[index] = deck[next_index]
    deck[next_index] = temp

def get_small_joker_value(deck):
    """ (list of int) -> int

    Return the value of the small joker (value of the second highest card) 
    for the given deck of cards.

    >>> deck = [1,2,3,4,5,6]
    get_small_joker_value(deck)
    '5'

    >>> deck = [6,5,4,3,2,1]
    get_small_joker_value(deck)
    '5'
    """
    return max(deck) - 1

def get_big_joker_value(deck):
    """ (list of int) -> int

    Return the value of the big joker (value of the highest card) 
    for the given deck of cards.

    >>> deck = [1,2,3,4,5,6]
    get_big_joker_value(deck)
    '6'

    >>> deck = [6,5,4,3,2,1]
    get_big_joker_value(deck)
    '6' 
    """
    return max(deck)

def move_small_joker(deck):
    """ (list of int) -> NoneType

    Swap the small joker with the card that follows it. Treat the deck as circular.

    >>> deck = [1,2,3,4,5,6]
    move_small_joker(deck)
    deck = [1,2,3,4,6,5]

    >>> deck = [6,5,4,3,2,1]
    move_small_joker(deck)
    deck = [6,4,5,3,2,1]
    """
    index = deck.index(get_small_joker_value(deck))
    swap_cards(deck,index)


def move_big_joker(deck):
    """ (list of int) -> NoneType

    Move the big joker two cards down the deck. Treat the deck as circular.

    >>> deck = [1,2,3,4,5,6]
    move_big_joker(deck)
    deck = [2,6,3,4,5,1]

    >>> deck = [6,5,4,3,2,1]
    move_small_joker(deck)
    deck = [5,4,6,3,2,1]
    """
    #swap two times for the big joker
    for i in range (2):
        index = deck.index(get_big_joker_value(deck))
        swap_cards(deck,index)

def triple_cut(deck):
    """ (list of int) -> NoneType

    Do a triple cut on the deck.

    >>> deck = [1,2,3,9,5,6,8,4,7]
    triple_cut(deck)
    '4,7,9,5,6,8,1,2,3'

    >>> deck = [1,4,7,10,13,16,19,22,25,3,6,28,9,12,15,18,21,24,2,27,5,8,11,14,17,20,23,26]
    triple_cut(deck)
    '5,8,11,14,17,20,23,26,28,9,12,15,18,21,24,2,27,1,4,7,10,13,16,19,22,25,3,6'    
    """
    #find first and second joker index by comparing the index of the two joker
    big_joker_index = deck.index(get_big_joker_value(deck))
    small_joker_index = deck.index(get_small_joker_value(deck)) 
    first_joker_index = min(big_joker_index,small_joker_index)
    second_joker_index = max(big_joker_index,small_joker_index)

    upper_part = deck[:first_joker_index]
    middle_part = deck[first_joker_index:second_joker_index+1]
    lower_part = deck[second_joker_index+1:]
 
    #swap the position of the cards
    new_list = lower_part + middle_part +upper_part

    #change the postion in the deck
    for i in range(len(new_list)):
        deck[i] = new_list[i]


def insert_top_to_bottom(deck):
    """ (list of int) -> NoneType

    Examine the value of the bottom card of the deck; 
    move that many cards from the top of the deck to the bottom, 
    inserting them just above the bottom card. Special case: 
    if the bottom card is the big joker, 
    use the value of the small joker as the number of cards.

    >>> deck = [4,7,9,5,6,8,1,2,3]
    insert_top_to_bottom(deck)
    '5,6,8,1,2,4,7,9'

    >>> deck = [5,8,11,14,17,20,23,26,28,9,12,15,18,21,24,2,27,1,4,7,10,13,16,19,22,25,3,6]
    insert_top_to_bottom(deck)
    '23,26,28,9,12,15,18,21,24,2,27,1,4,7,10,13,16,19,22,25,3,5,8,11,14,17,20,6'

    """
    v = deck[-1]
    l = deck[-1] #the last value of array
    # v is equal to the big joker, then change it to small joker
    if v == get_big_joker_value(deck):
        v = get_small_joker_value(deck)

    top = deck[:v]
    rest_list = deck[v:-1]

    #put the top list to the bottom
    new_list = rest_list + top + [l] #use l in case we change the value of v

    #change the position in the deck
    for i in range(len(new_list)):
        deck[i] = new_list[i]


def get_card_at_top_index(deck):
    """ (list of int) -> int

    Using the value of the top card as an index, 
    return the card in the deck at that index. 
    Special case: if the top card is the big joker, 
    use the value of the small joker as the index.

    >>> deck = [4,7,9,5,6,8,1,2,3]
    get_card_at_top_index(deck)
    '6'

    >>> deck = [23,26,28,9,12,15,18,21,24,2,27,1,4,7,10,13,16,19,22,25,3,5,8,11,14,17,20,6]
    get_card_at_top_index(deck)
    '11'
    """
    index = deck[0]
    #if the card is the big joker change it to small joker
    if index == get_big_joker_value(deck):
        index = get_small_joker_value(deck)

    return deck[index]

def get_next_keystream_value(deck):
    """ (list of int) -> int

    This is the function that repeats all five steps of the algorithm 
    until a valid keystream value is produced.

    >>> deck = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,11,14,17,20,23,26]
    get_next_keystream_value(deck)
    '11'

    >>> deck = [23,26,28,9,12,15,18,21,24,2,27,1,4,7,10,13,16,19,22,25,3,5,8,11,14,17,20,6]
    get_next_keystream_value(deck)
    '9'
    """

    move_small_joker(deck)
    move_big_joker(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    keystream_value = get_card_at_top_index(deck)

    #keep find keystream value until a valid key value is found
    while keystream_value == get_small_joker_value(deck) or keystream_value == get_big_joker_value(deck):
        move_small_joker(deck)
        move_big_joker(deck)
        triple_cut(deck)
        insert_top_to_bottom(deck)
        keystream_value = get_card_at_top_index(deck)

    return keystream_value

def process_messages(deck, msg, command):
    """ (list of int, list of str, str) -> list of str

    Return a list of encrypted or decrypted messages, 
    in the same order as they appear in the given list of messages. 
    Note that the first parameter may also be mutated during a function call.

    >>> deck = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,11,14,17,20,23,26]
        msg = ['OXXIKQCPSZXWW']
        process_messages(deck,msg,'d')
        '['DOABARRELROLL']'

        deck = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,11,14,17,20,23,26]
        msg = ['THISISITTHEMASTERSWORD','NOTHISCANTBEITTOOBAD']
        process_messages(deck,msg,'e')
        '['EQFZSRTEAPNXLSRJAMNGAT','GLCEGMOTMTRWKHAMGNME']'
    """

    modified_msg = []
    if command == ENCRYPT:
        func = encrypt_letter
    else:
        func = decrypt_letter

    for sentence in msg:
        new_sentence = ''
        for c in sentence:
            new_sentence+=func(c,get_next_keystream_value(deck))
        modified_msg.append(new_sentence)

    return modified_msg


def read_messages(msg_file):
    """ (file open for reading) -> list of str

    Read and return the contents of the file as a list of messages, 
    in the order in which they appear in the file. Strip the newline from each line.
    """
    return [clean_message(line) for line in msg_file.readlines()]

def is_valid_deck(deck):
    """ (list of int) -> bool

    Return True if and only if the candidate deck is a valid deck of cards.

    >>> deck = [1,2,3,4,5,6,7,8]
    is_valid_deck(deck)
    'True'

    >>> deck == [2,15,64]
    is_valid_deck(deck)
    'False'
    """
    for i in range(1, get_big_joker_value(deck)):
        #encuse the cards are consecutive
        if i not in deck:
            return False

    return True

def read_deck(deck_file):
    """ (file open for reading) -> list of int

    Return True if and only if the candidate deck is a valid deck of cards.
    """
    return [int(i) for i in deck_file.read().split()]