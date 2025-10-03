from stats import num_of_words
from stats import character_count
from stats import sort_dictionary
import sys

def get_book_text(a):
    with open(a) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        text = get_book_text(book)
        sort = sort_dictionary(character_count(text))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        num_of_words(text)
        print("--------- Character Count -------")
        for item in sort:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    
    
    
    
    
    
    
main()