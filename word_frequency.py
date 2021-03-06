#!/usr/bin/env python3
import re
import sys

COMMON_WORDS = (
    "a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,"
    "because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,"
    "for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,"
    "it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,"
    "not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,"
    "since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,"
    "twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,"
    "would,yet,you,your").split(',')


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
    """
    Opens filename and returns a list of all words, ignoring case/punctuation
    """
    word_list = []
    with open(filename) as my_file:
        for line in my_file:
            word_list.extend(chop_text(line))
    return word_list


def chop_text(a_string):
    """
    Takes a string and returns list of lowercased words
    minus punctuation, whitespace, and line endings
    """
    a_string = a_string.lower()
    a_string = re.sub(r'\n', ' ', a_string)  # Replace newlines with spaces
    a_string = re.sub(r'[^A-Za-z ]', '', a_string)
    return [item for item in a_string.split(' ') if item != ''] # Remove ''


def top_words(word_list, n=20, ignore_common=True):
    """
    Returns a sorted list of the n most frequent words in descending order
    Returns list of tuples of ('word', frequency)

    Setting ignore_common=True discards words present in COMMON_WORDS
    """
    top_words = sorted(word_list.items(), key=lambda x: x[1], reverse=True)

    if ignore_common:
        top_words = [item for item in top_words if item[0] not in COMMON_WORDS]

    return top_words[:n]


def display_top_words(word_list, n=20, display_mode='simple'):
    """
    Print out the `n` most frequent words in word_list,
    using the specified display_mode

    if display_mode ==
    'simple' :  display a list of words and their frequency, descending
    'histogram' : same as simple, but with bar chart histogram visible
    'normalized_histogram': same as histogram, but normalized to the max freq
    """
    top_word_list = top_words(word_list, n)

    if display_mode == 'simple':
        for item in top_word_list:
            print('{} {}'.format(*item))

    elif display_mode == 'histogram' or display_mode == 'normalized histogram':
        max_word_length = max([len(item[0]) for item in top_word_list])
        max_freq = top_word_list[0][1]

        for my_tuple in top_word_list:
            word, freq = my_tuple
            padding = ' ' * (max_word_length - len(word) + 1)
            bar = '#' * (freq // 6)  # scale to fit on screen

            if display_mode == 'normalized histogram':
                scale_factor = 50 / max_freq
                bar = '#' * int(freq * scale_factor)
            print('{}{}{} {}'.format(word, padding, bar, freq))
    else:
        print('Invalid display mode selected')


if __name__ == '__main__':
    word_list = (make_word_list('sample.txt'))
    if len(sys.argv) > 1:
        word_list = make_word_list(sys.argv[1])
    word_dict = (word_list_frequency(word_list))
    display_top_words(word_dict, n=20, display_mode='normalized histogram')
