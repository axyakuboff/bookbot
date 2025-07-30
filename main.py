from stats import get_num_words, count_letters, sort_char_count
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with an error code

    book_file_path = sys.argv[1]

    number = get_num_words(book_file_path)
    character_count = sort_char_count(count_letters(book_file_path))
    character_lines = []
    for entry in character_count:
        # Format each line (e.g., "e: 44538") and add it to the list
        character_lines.append(f"{entry['char']}: {entry['num']}")

    # Join all the lines in the list into one big string, separated by newline characters
    character_details_string = "\n".join(character_lines)
    final_report_output = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {number} total words
--------- Character Count -------
{character_details_string}
============= END ===============
    """
    print(final_report_output)



main()

