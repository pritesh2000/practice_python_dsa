def decimal_to_binary(n):
    if n >= 1:
        decimal_to_binary(n//2)
        print(n%2, end='')
decimal_to_binary(4)

def dec_to_bin(x):
    return sum(list(map(int, bin(x)[2:])))

m = [dec_to_bin(i) for i in range(4+1)]
print(m)