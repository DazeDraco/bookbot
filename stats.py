def get_word_count(filename):
    
	# Calls filepath to set f to file contents and print to terminal
    with open(filename) as f:
        
        # Sets f to actual file variable
        file_contents = f.read()
        
        # Sets all contents to lowercase to prevent overwrites
        lower_contents = file_contents.lower()
        
        # Splits contents into readable list
        split_contents = lower_contents.split()
        
        # Finds word count from listed contents
        word_count = len(split_contents)
        
    # 5/25/25
    # Same day fixed sloppiness by implimenting dict
        # Prints header with base information including filepath and wordcount
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {f.name}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        
        # Initialize blank dictionary
        dict = {}
        
        # Writes into blank dictionary with all valid characters
        for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','æ','â','ê','ë','ô']:
            # Counts all instances of each letter within the file text given
            dict[letter] = lower_contents.count(letter)
        
        # Sorts dictionary by most common letter first
        for letter in sorted(dict, key=dict.get, reverse=True):
            
            # Prints variables by letter then it's number called by %s as string and %d as decimal number
            print('%s: %d' % (letter, dict[letter]))
        print("============= END ===============")
