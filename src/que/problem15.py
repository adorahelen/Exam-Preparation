from collections import deque

def solution(N, K):
    queue = deque(range(1, N + 1))

    while len(queue) > 1:
        for _ in range(K - 1):
            queue.append(queue.popleft())  # K번째 이전까지 회전시킴
        
        queue.popleft()  # K번째 사람 제거
    
    return queue[0]

print(solution(5, 2))  # 결과: 3