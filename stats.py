


def get_num_words(text):
    words = text.split()
    counter = len(words)
    return counter

from collections import Counter


def character_counter(text):
    lowercase = text.lower()
    return Counter(lowercase)

def character_sort(text):
    lowercase_sort = text.lower()
    my_counter = Counter(lowercase_sort)
    filtered_items = [(char, count) for char, count in my_counter.items() if char.isalpha()]
    filtered_items.sort(key=lambda item: item[1], reverse=True)
    result_list = [{"char": char, "num": count} for char, count in filtered_items]
    return result_list
  




    
    


    



    





