from AlphabetTree import AlphabetTree

def build_full_tree(file_name):
    dictionary_tree = AlphabetTree()
    with open(file_name, "r") as NineLetterWords:
        for word in NineLetterWords:
            dictionary_tree.add_word(word,0) #place the word by its starting three letters
            dictionary_tree.add_word(word,3) #place the word by its middle three letters
    return dictionary_tree

def find_candidates(search_for, alphabet_tree, pos):
    word_search = alphabet_tree.get_words_with(search_for)
    if word_search is None:
        return []
    else:
        return word_search[pos]


def find_watskygram(word, alphabet_tree):

    watskygrams = []

    mid_three = word[3:6]
    end_three = word[6:9]

    first_word_second_candidates = find_candidates(mid_three, alphabet_tree, "front")
    first_word_third_candidates = find_candidates(end_three, alphabet_tree, "front")

    for second_word in first_word_second_candidates:
        
        end_three = second_word[6:9]
        
        second_word_third_candidates = find_candidates(end_three, alphabet_tree, "middle")    
        
        in_both = set(first_word_third_candidates) & set(second_word_third_candidates)
        
        if len(in_both) > 0:
            for third in in_both:
                watskygrams.append((word, second_word, third))
    
    return watskygrams

found = 0
word_tree = build_full_tree("9Letters")
with open("9Letters", "r") as nine_letter_words, open("watskygrams", "w") as grams:
    for word in nine_letter_words:
        watskygrams = find_watskygram(word, word_tree)

        for gram in watskygrams:
            found += 1
            grams.write(f"{gram[0][0:3]} {gram[1][0:3]} {gram[2][0:3]}\n")
            grams.write(f"{gram[0][3:6]} {gram[1][3:6]} {gram[2][3:6]}\n")
            grams.write(f"{gram[0][6:9]} {gram[1][6:9]} {gram[2][6:9]}\n\n")
print(f"Found {found} Watskygrams in the given dictionary.")