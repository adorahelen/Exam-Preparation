def solution(answers):
    # 각 수포자의 패턴
    patterns = [
        [1, 2, 3, 4, 5],              # 1번 수포자
        [2, 1, 2, 3, 2, 4, 2, 5],     # 2번 수포자
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자
    ]

    scores = [0] * 3  # 3명의 점수 초기화

    # 정답을 비교해 점수 계산
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1

    max_score = max(scores)  # 가장 높은 점수

    highest_score = []  # 가장 높은 점수를 받은 수포자
    for i, score in enumerate(scores):
        if score == max_score:
            highest_score.append(i + 1)  # 1번부터 시작하므로 i + 1

    return highest_score