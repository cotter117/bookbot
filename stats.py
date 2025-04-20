def get_book_text(args):
    """Reads the data from the text file in the specified filepath"""
    with open(args) as f:
        file_contents = f.read()
    return file_contents

def count_words(args):
    """Generates a count of the words in the text file in the specified path"""
    words_in_book = get_book_text(args).split()
    num_words = 0
    for word in words_in_book:
        num_words += 1
    return num_words

def count_chararcters(args):
    """Loops through all letters/symbols/spaces in the text and the checks if they are in the dictionary, if the are, adds one to the count, if they are not, adds to the dictionary with a value of one"""
    words_in_book = get_book_text(args)
    lower_case_words = words_in_book.lower()
    character_dict = {}
    for key in lower_case_words:
        if key in character_dict:
            character_dict[key] +=1
        else:
            character_dict[key] = 1
    return character_dict

def sort_characters(character_dict):
    """Takes all characters in the dictionary and converts to a list of individual dictionaries, then sorting them by highest to lowest"""
    character_dict_list = []
    for char, count in character_dict.items():
        character_dict_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    character_dict_list.sort(reverse=True, key=sort_on)

    return character_dict_list

