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
        
        
        
def avg_score():
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
    
# def mergeSortLst(lst):
#     if len(lst) <=1 :
#         return lst
    
#     mid=len(lst)//2
#     leftHalf=lst[:mid]
#     rightHalf=lst[mid:]
    
    
#     sortedLeft=mergeSortLst(leftHalf)
#     sortedRight=mergeSortLst(rightHalf)
    
#     return merge(sortedLeft,sortedRight)


# def merge(left,right):
#     result=[]
#     i=j=0
    
#     while i <len(left) and j <len(right):
#         if left[i] < right[j]:
#             result.append[left[i]]
#             i+=1
#         else:
#             result.append[right[j]]
#             j+=1
            
#         result.extend(left[i:])
#         result.extend(right[j:])
        
#         return result
        
            
# lst=[3,7,6,-10,15,23,55,-13]
# sortedList=mergeSortLst(lst)
# print(sortedList)


def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)