# 평균은 넘겠지
# 문제 : 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

C = int(input())
avg = []
for i in range(C):
    N = list(map(int, input().split()))

    sum = 0
    for j in range(N[0]):
        sum += N[j+1]

    cnt = 0
    for j in range(N[0]):
        if N[j+1] > sum/N[0]:
            cnt += 1
    avg.append(cnt/N[0]*100)
    N.clear()

for i in range(C):
    print('%.3f%%' %avg[i])
