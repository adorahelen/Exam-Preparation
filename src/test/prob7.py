def is_adjacent_valid(numbers, k):
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) > k:
            return False
    return True

def swap_and_check(numbers, swaps, k):
    # 기본적으로 인접 원소의 차이가 k 이하인지 확인
    if is_adjacent_valid(numbers, k):
        return swaps
    
    n = len(numbers)
    min_swaps = float('inf')

    # 모든 쌍의 원소를 swap하여 새로운 배열을 생성
    for i in range(n):
        for j in range(i + 1, n):
            # Swap i와 j의 원소
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # 재귀 호출
            result = swap_and_check(numbers, swaps + 1, k)
            if result != -1:
                min_swaps = min(min_swaps, result)
            # Swap 복구
            numbers[i], numbers[j] = numbers[j], numbers[i]
    
    return min_swaps if min_swaps != float('inf') else -1

def solution(numbers, k):
    return swap_and_check(numbers, 0, k)

# 예제 사용
numbers1 = [10, 40, 30, 20]
k1 = 20
print(solution(numbers1, k1))  # 결과: 1

numbers2 = [3, 7, 2, 8, 6, 4, 5, 1]
k2 = 3
print(solution(numbers2, k2))  # 결과: 2