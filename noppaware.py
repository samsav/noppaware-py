"""A simple phrase generator script for the Finnish Noppaware list"""

import secrets
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--phrases",
        type=int,
        help="Number of phrases to generate",
        default=4)
    parser.add_argument(
        "-w",
        "--words",
        type=int,
        help="Number of words per phrase",
        default=7)
    args = parser.parse_args()

    # SystemRandom() uses the best available OS-specific source for generating
    # random numbers. On Unix-based systems, dev/urandom is used; on Windows,
    # CryptGenRandom() is used. See https://docs.python.org/3/library/secrets.html
    # and https://docs.python.org/3/library/os.html#os.urandom
    RND = secrets.SystemRandom()

    # Open the Noppaware list and read the contents into a dictionary with the
    # number IDs as keys and words as values
    with open("noppaware.txt", 'r') as fp:
        WORDS = {line.split()[0]: line.split()[1] for line in fp.readlines()}

    N_PHRASES = args.phrases
    PHRASE_LENGTH = args.words
    PHRASES = list()

    # Loops for generating phrases
    for i in range(N_PHRASES):
        phrase = list()
        for j in range(PHRASE_LENGTH):
            # Emulate the dice rolling process by randomly generating 5 numbers in
            # range 1–6 and concatenating them into a number ID
            key = ''.join([str(RND.randint(1, 6)) for k in range(5)])
            phrase.append(WORDS[key])
        PHRASES.append(phrase)

    # Loop for printing out the phrases
    for phrase in PHRASES:
        print(' '.join(w for w in phrase))
