if __name__ == '__main__':
    n = int(input())
    t = tuple(int(i) for i in input().strip().split(" "))
    print(hash(t))
