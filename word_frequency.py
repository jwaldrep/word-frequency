
#Read text of sample.txt, and return top words with frequency each word occurs
#    ignore case and punctuation
#Then ouput 20 most frequent words in descending order


from pprint import pprint as pprint
import re


def word_list_frequency(word_list):
    """Returns a dictionary of word: frequency for a provided list of words"""
    word_frequencies = {}
    for word in word_list:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies

def word_frequency(a_string):
    """Returns frequency of words in a string"""
    word_list = chop_text(a_string)
    return word_list_frequency(word_list)

def make_word_list(filename):
    """Opens filename and returns a list of all words, ignoring case/punctuation

    """
    word_list = []
    with open(filename) as my_file:
        for line  in my_file:
            word_list.extend(chop_text(line))
    return word_list

def chop_text(a_string):
    """Takes a string and returns list of lowercased words
       minus punctuation, whitespace, and line endings
    """
    a_string = a_string.lower()
    a_string = re.sub(r'\n', ' ', a_string) #Replace newlines with spaces
    a_string = re.sub(r'[^A-Za-z ]', '', a_string) #Allow spaces
    return [item for item in a_string.split(' ') if item != '']
        #Remove '' and split on \n without


def top_words(word_list, n=20):
    """Returns a sorted list of the n most frequent words in decending order
       Returns list of tuples of ('word', frequency)
    """
    top_words = sorted(word_list.items(), key=lambda x: x[1], reverse=True)
    return top_words[:n]

def display_top_words(word_list, n=20, display_mode='simple'):
    top_word_list = top_words(word_list, n)
    if display_mode == 'simple':
        for item in top_word_list:
            print('{} {}'.format(*item))
    else:
        pass

if __name__ == '__main__':
    #print(chop_text('this is a %#^$&    test \n'))
    word_list = (make_word_list('sample.txt'))
    word_dict = (word_list_frequency(word_list))
    #pprint(top_words(word_dict, n=5 ))
    display_top_words(word_dict, n=20, display_mode='simple')
