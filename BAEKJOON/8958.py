# OX 퀴즈

#def sum_score

n = int(input())

# 리스트 초기화
list = ['' for i in range(n)]
count = [0 for i in range(n)]

for i in range(n):
    list[i] = input()

for i in range(n):
    an = 1
    for j in range(len(list[i])):
        if list[i][j] == 'O':
            count[i] += an
            an += 1
        else:
            an = 1

for i in range(n):
    print(count[i])
