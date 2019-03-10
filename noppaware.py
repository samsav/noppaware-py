"""A simple phrase generator script for the Finnish Noppaware list"""

import secrets

RND = secrets.SystemRandom()

with open("noppaware.txt", 'r') as fp:
    WORDS = {line.split()[0]: line.split()[1] for line in fp.readlines()}

N_PHRASES = 4
PHRASE_LENGTH = 7
PHRASES = list()

for i in range(N_PHRASES):
    phrase = list()
    for j in range(PHRASE_LENGTH):
        key = ''.join([str(RND.randint(1, 6)) for k in range(5)])
        phrase.append(WORDS[key])
    PHRASES.append(phrase)

for phrase in PHRASES:
    print(' '.join(w for w in phrase))
