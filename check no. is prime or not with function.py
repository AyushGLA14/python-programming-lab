def prime(x):
    c = 0
    for i in range(1, x + 1):
        if x % i == 0:
            c = c + 1
    if c == 2:
        print('prime')
    else:
        print('not prime')

x = int(input())
prime(x)
