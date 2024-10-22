# # 동적 계획법

# def rabbit_escape(n, k):
#     MOD = 1000000007

#     # dp[j][i]는 j번 점프를 사용하여 i 위치에 도달하는 방법의 수
#     dp = [[0] * (n + 1) for _ in range(k + 1)]
    
#     # 초기 조건: 0번 점프에서 0위치에 도달하는 방법은 1가지
#     dp[0][0] = 1

#     # 점프 횟수
#     for j in range(1, k + 1):
#         # 현재 위치
#         for i in range(1, n + 1):
#             # 마지막 점프 거리
#             for x in range(1, i + 1):
#                 if j == 1 or x < i:  # 첫 점프 또는 이전 점프보다 짧은 경우
#                     dp[j][i] = (dp[j][i] + dp[j - 1][i - x]) % MOD

#     return dp[k][n]

# # 테스트
# print(rabbit_escape(9, 3))   # 결과: 3
# print(rabbit_escape(10, 2))  # 결과: 4
# print(rabbit_escape(9, 4))   # 결과: 0
# print(rabbit_escape(10, 2))  # 결과: 4

#### 반복문 사용 최소로 => 통과 

def solution(n, k):
    limit = 1000000007
    memo = {}

    def ways(jump, position, last):
        if jump == k:
            return 1 if position == n else 0
        
        if position > n :
            return 0
        
        key = (jump, position, last)
        if key in memo:
            return memo[key]
        
        total_ways = 0

        for jump_distance in range(1, last): 
            total_ways += ways(jump +1, position + jump_distance, jump_distance)
            total_ways %= limit
        
        memo[key] = total_ways
        return total_ways

    return ways(0, 0, n + 1)

    
    
