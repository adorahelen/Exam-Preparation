# def solution(decimal):
#     stack = []
#     while decimal > 0:
#         reminder = decimal % 2
#         stack.append(str(reminder))
#         decimal //=2

#     binary = ""
#     while stack:
#         binary += stack.pop()


#     return binary


def solution(decimal):
    if decimal == 0:
        return "0"  # 입력이 0이면 2진수는 "0"
    
    stack = []
    while decimal > 0:
        reminder = decimal % 2
        stack.append(str(reminder))
        decimal //= 2

    binary = ""
    while stack:
        binary += stack.pop()

    return binary