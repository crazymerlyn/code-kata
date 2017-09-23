def sort_chars(s):
    count = [0 for _ in range(26)]

    for c in s:
        if c.isalpha():
            count[ord(c.lower()) - 97] += 1

    return "".join(chr(i + 97) * n for i, n in enumerate(count))

