def _fibo(n):
    if n <=0:
        return 0
    if n == 1 or n == 2: 
        return 1
    return _fibo(n-1) + _fibo(n-2)

def fibo(n):
    for i in range(n+1):
        print(_fibo(i),end=' ')

print(fibo(6))