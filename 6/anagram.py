from collections import defaultdict

anagrams = defaultdict(list)
with open("/usr/share/dict/words") as f:
    for line in f:
        word = line.strip()
        anagrams["".join(sorted(word))].append(word)

print max(anagrams.values(), key=len)
print max([l for l in anagrams.values() if len(l) > 1], key=lambda l: len(l[0]))
