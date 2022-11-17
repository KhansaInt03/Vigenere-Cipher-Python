import string

def ascii_to_ordo():

    ascii_dig = list(string.digits) 
    ascii_letters = list(string.ascii_letters)
    ascii_punctuation = list(string.punctuation)
    ascii_whitespace = list(string.whitespace)

    ord_dict = {}
    count_dig = 0
    for i in ascii_dig:
        ord_dict[i] = count_dig
        count_dig+=1
    for i in ascii_letters:
        ord_dict[i] = count_dig
        count_dig+=1
    for i in ascii_punctuation:
        ord_dict[i] = count_dig
        count_dig+=1
    ord_dict.update({ascii_whitespace[0]:count_dig})

    return ord_dict