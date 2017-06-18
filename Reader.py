""" vowels except y """
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

"""Dolch preprimer list"""
preprimer = ["a", "and", "away", "big", "blue", "can" "come", "down",
             "find", "for", "funny", "go", "help", "here", "i", "in", "is",
             "it", "jump", "little", "look", "make", "me", "my", "not", "one",
             "play", "red", "run", "sand", "see", "the", "three", "to", "two",
             "up", "we", "where", "yellow", "you"]

""" Dolch primer list """
primer = ["all", "am", "are", "at", "ate", "be", "black", "brown", "but",
          "came", "did", "do", "eat", "four", "get", "good", "have", "he",
          "into", "like", "must", "new", "no", "now", "on", "our", "out",
          "please", "pretty", "ran", "ride", "saw", "say", "she", "so",
          "soon", "that", "there", "they", "this", "too", "under", "want",
          "was", "well", "went", "what", "white", "who", "will", "with",
          "yes"]

""" Initial Consonant Blends and Digraphs """
initial_consonants = ["bl", "cl", "fl", "gl", "pl", "sc", "sk", "sm", "sl",
                      "sn", "sp", "st", "sw", "sh", "th", "ch", "wh", "br",
                      "cr", "dr", "fr", "gr", "pr", "tr", "tw"]

""" Final Consonant Blends, Digraphs, and Double letters """
final_consonants = ["ck", "ft", "lk", "lp", "lt", "mp", "nd", "nt", "sk",
                    "st", "ts", "xt", "ch", "sh", "th", "ss", "ck", "ff", "ll"]


def is_CVC(text):
    """ Check if a word is CVC: consonant-vowel-consonant. """
    has_three_characters = len(text) == 3
    if not has_three_characters:
        return False

    first, second, third = text[:3]
    first_is_consonant = first not in vowels
    second_is_vowel = second in vowels
    third_is_consonant = third not in vowels
    return first_is_consonant and second_is_vowel and third_is_consonant


def is_CVCE(text):
    """ Check if word is CVCE: consonant-vowel-consonantt-E. """
    has_four_characters = len(text) == 4
    if not has_four_characters:
        return False

    ends_with_e = text[-1] == 'e'
    begins_with_cvc = is_cvc(text[:3])

    return ends_with_e and begins_with_cvc


def check_initial_consonants(text):
    """ Treat common 2-letter combos at beginning as one letter """
    first_two = text[:2]

    if len(text) > 3 and first_two in initial_consonants:
        text_as_list = list(text)
        del text_as_list[0]
        without_first_letter = "".join(text_as_list)
        return without_first_letter

    return text


def check_final_consonants(text):
    """ Treat common 2-letter combos at end as one letter """
    last_two = text[-2:]

    if len(text) >= 3 and last_two in final_consonants:
        text_as_list = list(text)
        del text_as_list[-1]
        without_last_letter = "".join(text_as_list)
        return without_last_letter

    return text


def no_punct(text):
    """ Strip off any punctuation at the end of a word. """
    punct = ["!", ".", "?", ",", ";", ":"]

    if text[-1] in punct:
        text_as_list = list(text)
        del text_as_list[-1]
        without_punctuation = "".join(text_as_list)
        return without_punctuation

    return text


def check_readable(text):
    """ Check if a word is preprimer, primer, or easily decodable """
    word = no_punct(text)
    lower_case = word.lower()
    merge_start = check_initial_consonants(lower_case)
    merge_end = check_final_consonants(merge_start)
    CVC = is_CVC(merge_end)
    CVCE = is_CVCE(merge_end)

    if CVC or CVCE:
        return True
    elif lower_case in preprimer or lower_case in primer:
        return True
    else:
        return False


def flag(text):
    """ Flag hard-to-read words """
    word_list = text.split()
    count = 0

    while count < len(word_list):
        current_is_readable = check_readable(word_list[count])

        if not current_is_readable:
            word_list[count] = "*" + word_list[count] + "*"
            count += 1
        else:
            count += 1

    text_with_flags = " ".join(word_list)
    return text_with_flags
