class AlphabetTree:
    def __init__(self):
        self.letter={
            'a': None,
            'b': None,
            'c': None,
            'd': None,
            'e': None,
            'f': None,
            'g': None,
            'h': None,
            'i': None,
            'j': None,
            'k': None,
            'l': None,
            'm': None,
            'n': None,
            'o': None,
            'p': None,
            'q': None,
            'r': None,
            's': None,
            't': None,
            'u': None,
            'v': None,
            'w': None,
            'x': None,
            'y': None,
            'v': None,
            'v': None,
            'z': None 
        }
    
    def add_word(self, word, letter_index=0, count=1):
        next_letter = word[letter_index].lower()
        if count < 3: 
            # this is not the third letter to organize
            next_node = self.letter[next_letter]
            if next_node is None: 
                #this is the firt time this letter has been sorted
                #so create the next node for it
                next_node = AlphabetTree()
            next_node.add_word(word, letter_index+1, count+1)
            self.letter[next_letter] = next_node
        else:
            #this is the third letter to organize
            #so the entire word should be stored.
            word_dict = self.letter[next_letter]
            if word_dict is None: 
                #this is the firt time this letter has been sorted
                #so create the next node for it
                word_dict = {"front":[], "middle":[]}
            if letter_index == 2:
                word_dict["front"].append(word.rstrip())
            else:
                word_dict["middle"].append(word.rstrip())
            self.letter[next_letter] = word_dict
            

    #Follow a three letter path through the alphabet tree
    #and return the dictionary at the end of it.
    #None will be returned if there are no words with the search key in [0:3] or [3:6]
    #if a match is found a dictionary of format {"front":[], "middle":[]} will be returned
    #where front indicates the search key exists in [0:3]
    #and middle indicates the search key exists in [3:6]
    def get_words_with(self, three_letters, count=1):
        if count == 3:
            return self.letter[three_letters[2].lower()]
        else:
            next_node = self.letter[three_letters[count-1].lower()]
            if next_node is not None:
                return next_node.get_words_with(three_letters, count+1)
            else:
                return None