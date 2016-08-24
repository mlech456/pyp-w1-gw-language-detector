# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

from languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    
    stats = {}
    for language in languages:
        name = language['name']
        stats[name] = 0
    
    for item in text.split(' '):    #iterate through each word in text
        for language in languages:  #iterates through each language
            name = language['name']
            for word in language.get('common_words'): #iterates through each common word
                # language
                if item == word:
                    stats[name] += 1
    
    return max(stats, key=stats.get)