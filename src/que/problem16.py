import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)

    # 각 작업이 완료되기까지 남은 일수를 계산
    days_left = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(n)]

    count = 0
    max_day = days_left[0]

    for i in range(n):
        # 현재 작업이 현재 배포의 최대 일수보다 일찍 완료될 수 있다면 함께 배포
        if days_left[i] <= max_day:
            count += 1
        else:
            # 그렇지 않다면 지금까지의 배포 기능 수를 저장하고 새로운 배포 묶음 시작
            answer.append(count)
            count = 1
            max_day = days_left[i]

    # 마지막으로 남은 기능들에 대해 처리
    answer.append(count)
    return answer

# print(solution([93, 30, 55], [1, 30, 5]))  # 출력: [2, 1]

