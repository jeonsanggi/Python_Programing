#간단한 에코 클라이언트 만들기

import socket

HOST = 'localhost'  #서버 IP주소
PORT = 5001         #서버의 포트번호

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # TCP 소켓 생성, socket 객체를 sock으로 지정
    sock.connect((HOST,PORT))   #원격 호스트로 연결 시도
    msg = input('입력 : ')
    sock.sendall(msg.encode())  #메시지를 바이트 스트림으로 인코딩후 소켓 서버로 전송
    data = sock.recv(1024)      #서버로 부터 수신할 데이터


print('에코 서버로부터 받은 메시지 [%s]' %data.decode())    #수신한 데이터는 이진 바이트 스트림이기 때문에 decode()으로 문자열 변환 후 출력
