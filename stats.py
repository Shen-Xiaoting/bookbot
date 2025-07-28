def word_count(book_text):
    words = book_text.split() #splits text into words
    number_or_words = len(words) #counts number of words
    return number_or_words

def character_count(book_text):
    characters = {} #creates empoty dict
    convert_to_lower = book_text.lower() #converts text to lower case
    for char in convert_to_lower: # iterates thorugh characters in text
        if char in characters: # if character already exists in dictionary
            characters[char] += 1
        else: #if character does not exist in dictionary add to dictionary
            characters[char] = 1
    return characters

def sort_on(items):
    return items['num']  # returns the value for sorting

def sorted_dictonary(characters):
    char_list = []
    for key, value in characters.items():
        sort_dict = {"char": key , "num" : value}
        char_list.append(sort_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list  # returns sorted list of dictionaries
        
    