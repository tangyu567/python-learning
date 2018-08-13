vowels = {"a", "e", "i", "o", "u"}
word = input('Provide a word to search for vowels:')
i=vowels.intersection(set(word))
print(i)
