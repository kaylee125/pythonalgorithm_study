def solution(s):
    a = len(s)//2 
    b = len(set(s))
    if a < b: return a 
    else: return b

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
