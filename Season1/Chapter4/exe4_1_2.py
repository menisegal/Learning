

from re import search


dict_words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}



def translate(sentence, dict) -> list:
    sentence_list = sentence.split(' ')
    print(sentence_list)
    sentence_generator = (dict.get(w) for w in sentence_list)
    new_list = list()
    for i in range(len(sentence_list)):
        new_list.append(next(sentence_generator))

    print(new_list)
    return ' '.join(new_list)



    





print(translate("el gato esta en la casa", dict_words))