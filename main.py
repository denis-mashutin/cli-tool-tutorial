import random

import typer


def read_words(file_name):
    with open(file_name, 'r') as f:
        words = f.readlines()
        words = [word.strip() for word in words]
    return words


def main(
        capitalize: bool = typer.Option(False, '--caps', '-c', help='Capitalize each word.'),
        separator: str = typer.Option('', '--separator', '-s', help='Separate words with the given symbol.'),
        long: bool = typer.Option(False, '--long', '-l', help='Make the passphrase longer by including an adverb.')
):
    # Reading words from files
    sub_nouns = read_words('sub_nouns.txt')
    verbs = read_words('verbs.txt')
    adjectives = read_words('adjectives.txt')
    obj_nouns = read_words('obj_nouns.txt')
    word_bank = [sub_nouns, verbs, adjectives, obj_nouns]
    # Adding an adverb to make the passphrase longer
    if long:
        adverbs = read_words('adverbs.txt')
        word_bank.append(adverbs)
    # Selecting random words to include in the passphrase
    phrase_words = []
    for word_list in word_bank:
        random_word = random.SystemRandom().choice(word_list)
        phrase_words.append(random_word)
    # Capitalizing each word in the passphrase
    if capitalize:
        phrase_words = [phrase_word.capitalize() for phrase_word in phrase_words]
    # Inserting the separator if specified
    passphrase = separator.join(phrase_words)
    print(passphrase)


if __name__ == "__main__":
    typer.run(main)
