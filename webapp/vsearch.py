def search_for_vowels(phrase:str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase:str, letters:str='aeiou') -> set:
    return sorted(set(phrase).intersection(set(letters)))
