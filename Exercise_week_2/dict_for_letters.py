def count_chars(word):
    """
    Count appearence of a characters.
    """
    dict_for_chars = {}

    for letters in sorted(word):
        if letters in dict_for_chars:
            dict_for_chars[letters] += 1
        else:
            dict_for_chars[letters] = 1

    print(dict_for_chars)


def main():
    string_name = str(input('Enter a word: '))
    count_chars(string_name)


if __name__ == "__main__":
    main()
