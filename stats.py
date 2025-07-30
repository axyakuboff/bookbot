def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path):
    text = get_book_text(path).split()
    word_num = 0
    for word in text:
        word_num += 1 
    return word_num


def count_letters(path):
    text = get_book_text(path).lower()
    letter_count = {}
    for char in text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count
    


def sort_char_count(char_count_dict):
    """
    Transforms a character count dictionary into a sorted list of dictionaries.

    Args:
        char_counts_dict (dict): A dictionary mapping characters to their counts
                                 (e.g., {'a': 100, 'b': 50}).

    Returns:
        list: A list of dictionaries, where each dictionary has "char" and "num" keys.
              The list is sorted in descending order by "num".
              Non-alphabetical characters are excluded.
    """
    report_list = []

    for char, count in char_count_dict.items():
        if char.isalpha():
            report_list.append({"char": char, "num": count})

    # Define the key function for sorting
    def get_num_value(item_dict):
        return item_dict["num"]

    # Sort the list in-place based on the 'num' key in descending order
    report_list.sort(key=get_num_value, reverse=True)

    return report_list

