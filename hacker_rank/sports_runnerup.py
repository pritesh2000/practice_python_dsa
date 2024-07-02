# n = int(input())
# list1 = [int(input()) for i in range(n)]
# print(max(list1))

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print (sorted(set(arr))[-2])

    # n = int(input())
    # l = [(int(input())) for i in range(n)]
    # print(list(set(l))[-2])

if __name__ == '__main__':
    # n = int(input())
    arr = map(int, input().split())
    # l = [(int(input())) for i in range(n)]
    print(sorted(list(set(arr)))[-2])