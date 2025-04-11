import sys
from stats import get_word_count, get_char_count, sort_char_dict

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1] # use the second argument passed as the filename
    
    book_text = get_book_text(filepath)
    num_words = get_word_count(book_text)
    char_counts = get_char_count(book_text)
    sorted_chars = sort_char_dict(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['count']}")


main()
