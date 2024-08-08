import numpy as np

with open("lemmas.txt", "r") as f:
    lemmas = np.array([line.replace('\t', ',').strip("\n").split(',') for line in f.readlines()])


with open("lemmas-clean.txt", 'w') as f, open('en_profane_words.txt', 'r') as p:
    profane = [line.strip("\n") for line in p.readlines()]
    for l in lemmas[:, 1]:
        if len(l) > 2 and l not in profane:
            if '-' not in l and "'" not in l and '/' not in l:
                f.write(l.upper() + '\n')