# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/python

def anagrams(word, list_words):
    w_dict, w_len = counter(word)
    res_list = []
    for word_from_list in list_words:
        el_dict, el_len = counter(word_from_list)
        if el_len == w_len and el_dict == w_dict:
            res_list.append(word_from_list)
        else:
            continue
    return (res_list)

def counter(word):
    word_dict = {}
    for latter in word:
        if latter not in word_dict.keys():
            word_dict[latter] = word.count(latter)
    return word_dict, len(word)



if __name__ == '__main__':
    anagrams('laser', ['lazing', 'lazy', 'lacer'])