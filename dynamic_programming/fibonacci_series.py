def fib_memoization(n,cache={0:1, 1:1}):
   if n<2:
       return n
   if n in cache:
        return cache[n]
   
   if n<2:
    cache[n] = n
   else:
    cache[n] = fib_memoization(n-1,cache) + fib_memoization(n-2,cache)
   print(cache[n])
   return cache[n]

fib_memoization(9)

min_sum = float('inf')
min_sum = 323.3
print(min_sum)