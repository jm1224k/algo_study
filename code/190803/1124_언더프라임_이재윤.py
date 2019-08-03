#https://www.acmicpc.net/problem/1124
import sys
input = sys.stdin.readline

def prime_list(n):
    n = n + 1
    sieve = [0] * n # index 값으로 소수임을 바로 확인하기 위해 배열 생성 만약 소수라면 값은 0
    sieve[0],sieve[1] = 1,1 # 0과 1은 소수가 아님

    for i in range(2, n):
        if sieve[i] == 0:
            for j in range(i+i, n, i): # 2i ~ n 까지 i 를 더해가며
                nn = j
                while nn % i == 0 : # j가 i의 배수일때
                    nn //= i
                    sieve[j] += 1 # index의 값을 1 증가
    return sieve

def main() :
    pl = prime_list(100000)
    cnt = 0
    A,B = map(int, input().split())
    
    for i in range(A,B+1) :
        if (pl[pl[i]] == 0) : # i의 index 값이 소수인지 확인
            cnt += 1
            
    print(cnt)
        
main()
