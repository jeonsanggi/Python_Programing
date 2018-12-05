#숫자의 개수
#문제 세 개의 자연수 A, B, C가 주어질 때 AxBxC를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
result = 1

count = [0 for i in range(10)]

for i in range(3):
    result *= int(input())

for i in range(len(str(result))):
    index = int(str(result)[i])
    count[index] += 1

for i in range(10):
    print(count[i])
