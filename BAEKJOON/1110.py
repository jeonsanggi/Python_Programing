# 더하기 사이클
# 문제 : 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 마늘고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.

n = input()

if int(n) < 10:
    n = n + '0'

cnt = 0
sum = 0
tmp = n
while True:
    cnt += 1
    sum = int(tmp[0]) + int(tmp[1])

    if sum < 10:
        new = tmp[1]+str(sum)
    else :
        new = tmp[1] + str(sum)[1]

    if new == n:
        break
    else:
        tmp = new

print (cnt)
