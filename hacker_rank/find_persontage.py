if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i, j in student_marks.items():
        if query_name == i:
            avg = sum(j)/3
            print(format(avg, '.2f'))