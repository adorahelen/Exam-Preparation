# def solution(n):
#     lenth = 1
#     count = 9
#     start = 1

#     while n > lenth * count:
#         n -= lenth * count
#         lenth += 1
#         count *= 10
#         start *= 10

#     num = start + (n - 1)// lenth
#     digit = (n-1) % lenth

#     return int(str(num)[digit])
# 시간초과

