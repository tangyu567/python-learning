def searchForVowels(word):
    '''Return a bool based on any vewols found'''
    vowels = set('aeiou')
    #word = input('Provide a word to search for vowels:')
    i=vowels.intersection(set(word))
    return bool(i)
