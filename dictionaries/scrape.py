f = open("wiki-100k.txt", "r", encoding="utf8").readlines()
censor = [line.strip("\n") for line in open("en_profane_words.txt", "r").readlines()]
out = open("wiki-100k-cleaned.txt", "w")

final = []

goods = 0
for line in f:
    line = line.strip("\n ").lower()
    if len(line) >= 3 and "#" not in line and line not in censor:
        good = True
        for char in line:
            if char not in "abcdefghijklmnopqrstuvwxyz":
                good = False
        if good:
            goods += 1
            final.append(line)

final = list(set(final))
final = sorted(final, key=lambda x: len(x))

for line in final:
    out.write(line + "\n")


print(len(f), goods)
out.close()