def searchForVowels():
    '''display any vewols in an asked-for word'''
    vowels = set('aeiou')
    word = input('Provide a word to search for vowels:')
    i=vowels.intersection(set(word))
    print(i)
