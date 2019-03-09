"""A simple phrase generator script for the Finnish Noppaware list"""

import secrets

rnd = secrets.SystemRandom()

with open("noppaware.txt", 'r') as fp:
    words = {line.split()[0]: line.split()[1] for line in fp.readlines()}

n_phrases = 4
phrase_length = 7
phrases = list()

for i in range(n_phrases):
    phrase = list()
    for j in range(phrase_length):
        key = ''.join([str(rnd.randint(1,6)) for k in range(5)])
        phrase.append(words[key])
    phrases.append(phrase)

for phrase in phrases:
    print(' '.join(w for w in phrase))
