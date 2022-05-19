array = [3, 6, 14, 16, 33, 55, 56]
wanted = -10

# binary search one-liner

bs = lambda l, x, lo, hi: -1 if lo >= hi else (lo + hi) // 2 if l[(lo + hi) // 2] == x else bs(l, x, lo, (lo + hi) // 2 - 1) if l[(lo + hi) // 2] > x else bs(l, x, (lo + hi) // 2 + 1, hi)
print(bs(array, wanted, 0, len(array)))


