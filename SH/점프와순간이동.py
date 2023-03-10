#현재까지 온 거리*2==순간이동 거리
#따라서, 순간이동 거리//2==현재까지 온 거리(짝수일 경우) or 현재까지 온 거리+1(거리가 홀수일 경우)


def solution(n):    
    cnt=0
    while n//2!=0:
        # 2로 나눈 나머지 값이 1이면  해당 값은 점프가 필요한 것으로 판단하고 cnt+=1 해줌
        if n%2==1:
            cnt+=1
            n=n//2
        else:
            n=n//2

    #처음위치는 0이므로 최소 1칸은 점프를 해야함 (return 값에 cnt+1)
    return cnt+1

'''
<다른 코드>
4=100(2) 8=1000(2) 처럼 2의 n제곱이면 처음 0->1빼고 순간이동으로 갈 수 있다. 이를 이진수로 표현하면 1이 하나인 이진수이다.
즉, 건전지 사용량은 이진수로 변환했을 때 1의 개수와 같다.

def solution(n):
    return bin(n).count('1')
    
'''

    
print(solution(5))



