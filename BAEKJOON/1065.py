#한수

# 세자리 수 부터 한수 인지 확인하는 함수
def check_num(num, length):
    sum = 0
    #첫째 자리 수와 둘째 자리수의 차를 확인 (공차를 구함)
    x = int(num[0]) - int(num[1])
    flag = True

    for i in range(1, length-1):
        #각 자리수와 다음자리수의 차를 확인 (공차와 같은지 확인)
        if x == int(num[i]) - int(num[i+1]):
            continue
        else:
            flag = False

    return flag


a = input()
cnt = 0

for i in range(1,int(a)+1):
    #1~99는 한 수
    if i < 100:
        cnt += 1
    else:
        #한 수인지 확인 하는 함수의 리턴 값이 True이면 cnt +=1
        if check_num(str(i), len(str(i))):
            cnt += 1

print (cnt)
