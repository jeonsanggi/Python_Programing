#시퀀스 자료 슬라이싱 이해하기
# [시작 인덱스:끝 인덱스: 스텝]
# 스텝: 자료를 취하는 간격 (디폴트 값은 1)


strdata = "Time is money!!"
print(strdata[1:5]) #'ime'가 출력
print(strdata[:7]) #'Time is'가 출력
print(strdata[9:]) #'oney!!'가 출력
print(strdata[:-3]) #'Time is mone'가 출력
print(strdata[-3:]) #'y!!'이 출력
print(strdata[:]) #'Time is money!!'가 출력됨
print(strdata[::2]) #'Tm smmy!'가 출력됨
