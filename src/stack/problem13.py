def soultion(board, moves):
    lanse = [[] for _ in range(len(board[0]))]

    for i in range(len(board) -1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanse[j].append(board[i][j])
    
    buket = []
    answer = 0

    for m in moves:
        if lanse[m-1]:
            doll = lanse[m-1].pop()

            if buket and buket[-1] == doll:

                buket.pop()
                answer += 2

            else:
                buket.append(doll)

    return answer

# # 예시 1
# board = [[0,0,0,0,0],
#          [0,0,1,0,3],
#          [0,2,5,0,1],
#          [4,2,4,4,2],
#          [3,5,1,3,1]]

# moves = [1,5,3,5,1,2,1,4]
# print(solution(board, moves))  # 출력: 4