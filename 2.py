#정수 리스트에서 소수만 걸러내기(filter)

#소수인지 확인하는 함수
def getPrime(x):
    #for~else문:  for문이 break에 의해 중담됨이 없이 정상적으로 모두 실행되면 else의 특정 코드를 실행
    for i in range(2,x-1):
        if x%i==0:
            break
    else:
        return x

listdata = [117,119,1113,11113,11119]
#fliter() : 리스트와 같이 반복 가능한 자료에서 특정 조건을 만족하는 값을 추출하는 방법을 제공해준다.
ret = filter(getPrime, listdata)
#list(): 리스트로 변환
print(list(ret))
