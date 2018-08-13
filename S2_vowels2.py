vowels = ["a", "e", "i", "o", "u",
          "A", "E", "I", "O", "U"]
word = input("Provide a word to search for vowels:")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)

