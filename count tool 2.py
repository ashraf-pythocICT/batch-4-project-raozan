def count_line_word_character(text):
    # Count the number of lines
    line_count = text.count('\n') + 1
    
    # Split the text into words
    words = text.split()
    # Count the number of words
    word_count = len(words)
    
    # Count the number of characters
    character_count = len(text)
    
    return line_count, word_count, character_count

if __name__ == "__main__":
    # Example usage:
    text = "Raozan RRAC Model Govt High School."
    
    line_count, word_count, character_count = count_line_word_character(text)
    print("Number of lines:", line_count)
    print("Number of words:", word_count)
    print("Number of characters:", character_count)