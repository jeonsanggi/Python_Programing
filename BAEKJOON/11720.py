#숫자의 합
#문제 : N개의 숫자가 공백 없이 쓰여있따. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

n = int(input())
a = input()

sum = 0
for i in range(n):
    sum += int(a[i])

print(sum)
