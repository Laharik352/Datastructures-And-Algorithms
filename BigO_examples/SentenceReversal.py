'''In this problem, The spaces if any must be removed and the words in the sentence must be reversed'''
def Sentence_reversal():
    s = input("Enter the string:")  # Bruteforrce method
    s = s.strip().split(" ")
    s = list(filter(None, s))      # THis is to remove empty elements in the list
    l1 = []
    k = ''
    for i in range(len(s)-1,-1,-1):
        l1.append(s[i])

    for m in range(len(l1)):
        k += l1[m]+' '
    print(k)
Sentence_reversal()

# def rev_word(s):
#     return " ".join(reversed(s.split()))
# print(rev_word("I drink coffee"))
#
# def rev_word1(s):
#     return " ".join(s.split()[::-1])
# print(rev_word1("I drink coffee"))

'''Another method to solve using while loops in succession'''
def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))

def rev_string(string):
    print(" ".join(string.split()[::-1]))
rev_string("Did you have tea today")