#https://www.acmicpc.net/problem/2096
import sys
input = sys.stdin.readline
import copy

def main() :
    dp = [ [[0,0,0],[0,0,0]], [[0,0,0],[0,0,0]] ] # 배열 초기화 dp[0] 최대값 dp[1] 최소값
    N = int(input())
    
    for _ in range(N) :
        narr = list(map(int, input().split()))

        # 최대값
        dp[0][0] = copy.deepcopy(dp[0][1]) # 배열 이동
        dp[0][1][0] = max(dp[0][0][0],dp[0][0][1]) + + narr[0] # 1번째를 선택한 최대값
        dp[0][1][1] = max(dp[0][0][0],dp[0][0][1],dp[0][0][2]) + narr[1] # 2번째를 선택한 최대값
        dp[0][1][2] = max(dp[0][0][1],dp[0][0][2]) + narr[2] # 3번째를 선택한 최대값

        #최소값
        dp[1][0] = copy.deepcopy(dp[1][1]) # 배열 이동
        dp[1][1][0] = min(dp[1][0][0],dp[1][0][1]) + + narr[0] # 1번째를 선택한 최소값
        dp[1][1][1] = min(dp[1][0][0],dp[1][0][1],dp[1][0][2]) + narr[1] # 2번째를 선택한 최소값
        dp[1][1][2] = min(dp[1][0][1],dp[1][0][2]) + narr[2] # 3번째를 선택한 최소값

    Max = max(dp[0][1])
    Min = min(dp[1][1])
    
    print(Max, Min)
    
    return 0;
        
main()
