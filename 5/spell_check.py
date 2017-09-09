import mmh3
import array

class BloomFilter(object):
    """A bloom filter"""
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bits = array.array("B", b"\x00" * size)

    def _hashes(self, word):
        hash1 = mmh3.hash(word, 0)
        hash2 = mmh3.hash(word, 1)
        for i in range(self.hash_count):
            yield (hash1 + hash2 * i) % self.size

    def add(self, word):
        for h in self._hashes(word):
            self.bits[h] = 1

    def contains(self, word):
        for h in self._hashes(word):
            if not self.bits[h]:
                return False
        return True


if __name__ == '__main__':
    bloom = BloomFilter(10 ** 6, 10)
    with open("/usr/share/dict/words") as f:
        for line in f:
            bloom.add(line.strip())

    import sys
    print "Enter words"
    try:
        while True:
            word = raw_input()
            if not bloom.contains(word.strip()):
                print "Wrong"
            else:
                print "Right"
    except EOFError:
        pass

