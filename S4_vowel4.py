def searchForVowels(word: str) -> set: 
    '''Return any vewols found'''
    vowels = set('aeiou')
    #word = input('Provide a word to search for vowels:')
    i=vowels.intersection(set(word))
    return i
