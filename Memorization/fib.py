memo = {}

def fibRec(n) :
    if n in [1, 2] : return 1
    return fib(n-2) + fib(n-1)

def fib(n, memo) :
    if n <= 2 :
        return 1
    if n in memo :
        return memo[n]
    memo[n] = fib(n-2, memo) + fib(n-1, memo)
    return memo[n]

print(fib(10, memo))
