def soultion(prices):
    n = len(prices)
    answer = [0] * n 

    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = n -1 -j

    return answer

# 이해못함


# # 예시 1
# prices = [1, 2, 3, 2, 3]
# print(solution(prices))  # 출력: [4, 3, 1, 1, 0]

# # 예시 2
# prices = [5, 4, 3, 2, 1]
# print(solution(prices))  # 출력: [1, 1, 1, 1, 0]