from stats import get_num_words
from stats import char_count
from stats import sort_dict
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path, "r") as file:
        book = file.read()
    num = get_num_words(book)
    char_dict = char_count(book)
    char_list = sort_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
