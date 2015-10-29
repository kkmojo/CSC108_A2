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
    
    >>> clean_message(Is today hot?)
    'ISTODAYHOT'
    
    """
    clean_msg = '';
    
    for letters in msg:
        if letters.isalpha():
            clean_msg = clean_msg + letters.upper()
            
    return clean_msg


def encrypt_letter(letter, keystream_value):
    return chr(65+(ord(letter)-65 + keystream_value) % 26)
    
def decrypt_letter(letter, keystream_value):
    if (ord(letter) - 65 - keystream_value) >= 0:
        return chr(65 + (ord(letter) - 65 - keystream_value) % 26)
    else:
        return chr (65 + ((ord(letter) - 65 - keystream_value) + 26))


def swap_cards(deck, index):
    temp = deck[index]
    next_index = (index+1) % len(deck)# ensure the next index is in the range
    deck[index] = deck[next_index]
    deck[next_index] = temp

def get_small_joker_value(deck):
    return max(deck) - 1

def get_big_joker_value(deck):
    return max(deck)

def move_small_joker(deck):
    index = deck.index(get_small_joker_value(deck))
    swap_cards(deck,index)


def move_big_joker(deck):
    #swap two times for the big joker
    for i in range (0,2):
        index = deck.index(get_big_joker_value(deck))
        swap_cards(deck,index)

def triple_cut(deck):
    #find first and second joker index by comparing the index of the two joker 
    first_joker_index = min(deck.index(get_small_joker_value(deck)),deck.index(get_big_joker_value(deck)))
    second_joker_index = max(deck.index(get_small_joker_value(deck)),deck.index(get_big_joker_value(deck)))

    upper_part = []
    middle_part = []
    lower_part = []

    for i in range(0, first_joker_index):
        lower_part.append(deck[i])

    for i in range(first_joker_index, second_joker_index+1):
        middle_part.append(deck[i])

    for i in range(second_joker_index+1, len(deck)):
        upper_part.append(deck[i])

    new_list = upper_part + middle_part +lower_part

    for i in range(0, len(new_list)):
        deck[i] = new_list [i]


def insert_top_to_bottom(deck):
    v = deck[-1]
    # v is equal to the big joker, then change it to small joker
    if v == get_big_joker_value(deck):
        v = get_small_joker_value(deck)

    top = []
    rest_list = []
    for i in range(0,v):
        top.append(deck[i])

    for i in range(v, len(deck)-1):
        rest_list.append(deck[i])

    #put the top list to the bottom
    new_list = rest_list + top
    new_list.append(v)

    for i in range(0, len(new_list)):
        deck[i] = new_list[i]


def get_card_at_top_index(deck):
    index = deck[0]
    if index == get_big_joker_value(deck):
        index = get_small_joker_value(deck)

    return deck[index]

def get_next_keystream_value(deck):

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
    if command == ENCRYPT:
        keystream_values = []
        encrypt_msg = []
        for i in range(0, len(msg)):
            keystream_values.append(get_next_keystream_value(deck))
            encrypt_msg.append(encrypt_letter(msg[i],keystream_values[i]))
        return encrypt_msg
    else:
        keystream_values = []
        decrypt_msg = []
        for i in range(0, len(msg)):
            keystream_values.append(get_next_keystream_value(deck))
            decrypt_msg.append(decrypt_letter(msg[i], keystream_values[i]))
        return decrypt_msg

def read_messages(file):
    return clean_message(file.read())

def is_valid_deck(deck):
    for i in range(1, get_big_joker_value(deck)):
        if i not in deck:
            return False

    return True

def read_deck(file):
    content = file.read()
    content = content.split()
    deck = [int(i) for i in content]
    return deck

'''
def main():
    msg = 'Python Type "help", "copyright", "credits" or "license" for more information.'
    deck = [1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,5,8,11,14,17,20,23,26]

    for i in range(1,29):
        deck.append(i)
        
    print(deck)
    #swap_cards(deck,0)
    #move_small_joker(deck)
    #move_big_joker(deck)
    #deck = triple_cut(deck)
    #insert_top_to_bottom(deck)
    #print(get_small_joker_value(deck))
    #print(get_big_joker_value(deck))
    #print(clean_message(msg))
    print(get_next_keystream_value(deck))
    print(get_next_keystream_value(deck))
    print(encrypt_letter('Y', 14))
    print(decrypt_letter(encrypt_letter('Y',14),14))
    file1 = open('deck2.txt', 'r')
    read_deck(file1)
    file2 = open('message_file1.txt', 'r')
    print(read_messages(file2))

if __name__ == "__main__":
    main()
 '''   