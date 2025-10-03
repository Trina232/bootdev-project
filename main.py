
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


from stats import get_num_words
from stats import character_counter
from stats import character_sort


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    count = get_num_words(text)
    sorting = character_sort(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for item in sorting:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
main()












    
    




    

