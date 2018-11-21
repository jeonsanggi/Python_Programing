#세 수
#세 정수 A, B, C가 주어진다. 이때, 두번째로 큰 정수를 출력하는 프로그램을 작성하시오.

N = list(map(int, input().split()))

N.sort(reverse = True)

print(N[1])
