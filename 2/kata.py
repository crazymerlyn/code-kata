def chop(n, ar):
    if not ar: return -1
    i = len(ar) // 2
    if ar[i] == n: return i
    elif ar[i] < n:
        off = chop(n, ar[i+1:])
        return off if off == -1 else i + 1 + off
    else:
        return chop(n, ar[:i])
