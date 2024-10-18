# def solution(s):
#     stack = []
#     for c in s:
#         if c == "(":
#             stack.append(c)
#         elif c == ")":
#             if not stack:
#                 return False
#         else:
#             stack.pop()

#     if stack:
#         return False
    
#     else :
#         return True

def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:  # 스택이 비어 있으면 잘못된 짝
                return False
            stack.pop()  # 스택에 값이 있으면 pop

    return not stack  # 스택이 비어 있으면 True, 비어 있지 않으면 False