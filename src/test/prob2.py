def solution(arr, n):
    saved = set()
    for num in arr:
        complement = n-num
        if complement in saved:
            return True
        saved.add(num)
    return False
