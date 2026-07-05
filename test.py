def second_runner_up():
    n = int(input())
    scores = list(map(int, input().split()))

    scores = sorted(set(scores))
    print(scores[-2])





def name_score_sort():
    student = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])

    scores = set()
    for i in range(len(student)):
        scores.add(student[i][1])

    scores = sorted(scores)
    sec_scr = scores[1]

    names = []

    for i in range(len(student)):
        if student[i][1] == sec_scr:
            names.append(student[i][0])

    names.sort()

    for name in names:
        print(name)
        
        
        
if __name__ == '__main__':
    n = int(input())
    total=0
    count=0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()  
    
    score=student_marks[query_name]
    avg=sum(score)/len(score)
    print(f"{avg:.2f}")