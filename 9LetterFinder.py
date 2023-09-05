"""A simple script to open a dictionary,
   run through every word in t dictionary,
   and for every 9 letter word write that to a new file
   to produce a dictionary of all 9 letter words"""
with open("AllWords", "r") as all_words, open("9Letters", "w") as nine_letters:
    for word in all_words:
        # Every line ends in a '/n' character. rstrip removes tailing white space
        # to only count real letters.
        if len(word.rstrip()) == 9:
            nine_letters.write(word)