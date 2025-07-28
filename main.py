import sys
from stats import word_count #imports function
from stats import character_count
from stats import sorted_dictonary 

def get_book_text (filepath):
    
    with open(filepath) as f: #opens file
        text = f.read() #reads file
    return text

def main():
    if len(sys.argv) < 2: #checks if filepath is provided
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    get_book = get_book_text(filepath) #pulls text from file using get_book_text function
    print ("============ BOOKBOT ============")
    print (f'analysing book found at {filepath}')
    print ("----------- Word Count ----------")
    print (f'Found {word_count(get_book)} total words') #count words in the document pulling text from file using get_book_text function
    print ("---------- Character Count -------")
    final_char_data = sorted_dictonary(character_count(get_book)) #pulls text from file using get_book_text function
    for char_dict in final_char_data:
      character_string = char_dict['char'] 
      character_count_num = char_dict['num']

      if character_string.isalpha():
          print(f"{character_string}: {character_count_num}") 
    print ("============= END ===============")



main()
