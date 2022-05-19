unsorted = [33, 2, 3, 17]

q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

#print(q(unsorted))
#fibonacci = lambda n: 0 if n == 0 else 1 if n == 1 else fibonacci(n-1)+fibonacci(n-2) .

l = [1,2,3]

rb = len(l)-1
lb = 0
x = 3

bin_search = lambda lb, rb, x, l: -1 if (lb >= rb) else ((rb + lb) // 2 if l[(rb + lb) // 2] == x else bin_search(lb, l[(rb + lb) // 2]-1, x, l) if l[(rb + lb) // 2] > x else bin_search(l[(rb + lb) // 2]+1, rb, x, l))

   ## The Data
   l = [3, 6, 14, 16, 33, 55, 56, 89]
   x = 33
## The One-Liner
ubs = lambda l, x, lo, hi: -1 if lo>hi else \
v(lo+hi)//2 if l[(lo+hi)//2] == x else \
wbs(l, x, lo, (lo+hi)//2-1) if l[(lo+hi)//2] > x else \ xbs(l, x, (lo+hi)//2+1, hi)
   ## The Results
   print(bs(l, x, 0, len(l)-1))
