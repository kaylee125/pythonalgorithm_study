def solution(participant, completion):
    answer = {}
    for i in participant:
        answer[i] = answer.get(i, 0) +1
    for j in completion:
        answer[j] -= 1
    for k in answer:
        if answer[k] : return k

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
