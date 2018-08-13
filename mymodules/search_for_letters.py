def search_for_letters(letters:str, phrase:str) -> set:
    return set(letters).intersection(set(phrase))
