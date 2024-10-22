# def solution(n):
#     min_day = float('inf')
#     max_day = float('-inf')

#     for start_day in range(7):
#         holidays = 0
#         for i in range(n):
#             day = (start_day + i )% 7
#             if day == 5 or day == 6:
#                 holidays += 1
        
#         min_day = min(min_day, holidays)
#         max_day = max(max_day, holidays)

#     return (min_day, max_day)

def solution(n):
    include_day = n // 7
    exclude_day = n % 7

    min_day = include_day * 2
    if exclude_day > 5:
        min_day += exclude_day - 5 

    max_day = include_day * 2
    if exclude_day >= 2:
        max_day += 2

    elif exclude_day == 1:
        max_day += 1 


    return (min_day, max_day)

# 효율성 때문에 실패 => 다시 작성 

