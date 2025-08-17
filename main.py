from stats import count_the_words, count_letter_usage, sort_letter_usage
import sys

def get_book_text(filepath):
    # opening the file then returning the filetext
    with open(filepath) as f:
        filetext = f.read()
        return filetext

def main():

    # Setting file path
    book_path = sys.argv[1]
    # Running get_book_text with file path as
    # an arugment"
    text = get_book_text(book_path)

    # count the words and print it.
    word_count = count_the_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    letter_count = count_letter_usage(text)
    ordered_letter_count = sort_letter_usage(letter_count)
    #print(ordered_letter_count)
    for line in ordered_letter_count:
        if line[0].isalpha():
            print(f"{line[0]}: {line[1]}")
    print("============= END ===============")
    pass


if len(sys.argv) != 2:
    print(f"You submited {len(sys.argv) - 1} arguments with the call.")
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()