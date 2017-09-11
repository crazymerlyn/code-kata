
words = set()
with open("/usr/share/dict/words") as f:
    for line in f:
        words.add(line.strip())


j = 0
for word in words:
    for i in range(2, len(word) -1):
        left = word[:i]
        right = word[i:]
        if left in words and right in words:
            print "%s + %s = %s" % (left, right, word)

