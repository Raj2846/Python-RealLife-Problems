arr = [10, 1, 3, 4, 2, 5, 9, 7, 6, 8]

def bubble_sort(arr):
    for i in range(len(arr)):
        for k in range(len(arr) - 1):
            if arr[i] < arr[k]:
                arr[i], arr[k] = arr[k], arr[i]

    print(arr)

# bubble_sort(arr)


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        key = i

        for j in range(i + 1, n):
            if arr[j] < arr[key]:
                key = j

        arr[i], arr[key] = arr[key], arr[i]

    print(arr)

selection_sort(arr)



marks = [45, 56, 76, 23, 90, 99, 100]
# selection_sort(marks)

"The Lost Student (Attendance Register)"

def search_student(arr, name):
    if name in arr:
        print(f"{name} is present")
    else:
        print(f"{name} is absent")

stu_name = ["Desai", "Rajkumar", "Vishal", "Raj"]
search_student(stu_name, "Raj")


def binary_search(start, end, arr, name):
    if start > end:
        return f"{name} not found."

    mid = (start + end) // 2

    if arr[mid] == name:
        return f"{name} found at {mid} position."

    elif arr[mid] > name:
        return binary_search(start, mid - 1, arr, name)

    else:
        return binary_search(mid + 1, end, arr, name)


# Sorted list
stu_name = ["Desai", "Raj", "Rajkumar", "Vishal"]

print(binary_search(0, len(stu_name) - 1, stu_name, "Raj"))