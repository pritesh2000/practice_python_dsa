def print_rangoli(size):
    # your code goes here
    width = ((size-1)+(size))*2 -1
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    
    for index in range(size):
        newLine = "-".join(alphabet[index:size])
        
        left = newLine[::-1]
        right = newLine[1:]
        lines.append(left+right)

    for i in range(size):
        for _ in range(i):
            print(" ", end=" ")
        else:
            print(lines[i])
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)