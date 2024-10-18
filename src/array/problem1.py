# sort array

def solution(arr):
    arr.sort()

    return arr

def solution(arr):
    sorted_list = list(sorted(arr))
    return sorted_list

import time

def bubble_sort(arr): 
    lenth = len(arr)
    for i in range(lenth):
        for j in range(lenth - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j + 1], arr[i]

                return arr
            
def do_sort(arr):
    arr.sort()
    return arr


def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result

arr = list(range(10000))


bubble_time, bubble_result = measure_time(bubble_sort, arr)
print(" 첫번째 코드 실행시간 ㅣ ",format(bubble_time, ".10f"))

arr = list(range(10000))
rever_time,  rever_result = measure_time(do_sort, arr)
print("두 번째 코드 실행 시간 : ", format(rever_time, ".10f"))

print("두 개의 코드 결과가 동일한지 확인 : ", bubble_result == rever_result)

