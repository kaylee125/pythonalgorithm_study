#주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

from itertools import combinations

def solution(nums):
    answer = 0
    sum_val=list(combinations(nums,3))
  
    #소수인지 판별
    for n in sum_val:
        chk_prim=sum(n)
        prime=True
        for i in range(2,chk_prim):
            if chk_prim%i==0: #하나라도 나누어 떨어지는 케이스가 있으면 소수가 아니다
                prime=False
        if prime:
            answer+=1    
    return answer

print(solution([1, 2, 3, 7, 8] ))