#간단한 에코 서버 만들기

import socket

HOST = ''   #IP
PORT = 5001 #포트번호

def runServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:     #TCP 소켓을 생성, socket 객체를 sock으로 지정
        sock.bind((HOST, PORT))     #소켓을 IP(프로그램이 구동되는 컴퓨터의 IP를 자동 할당)와 포트번호로 바인딩
        sock.listen(1)              #listen 상태로 서버가 한 번에 처리 가능 수는 1로 설정 (5까지 가능)
        print('클라이언트 연결 기다리는 중.......')
        conn, addr = sock.accept()  #클라이언트 연결되면 TCP 소켓과 클라이언트 주소를 리턴
        with conn:
            print('[%s]와 연결됨' %addr[0])
            while True:
                data = conn.recv(1024)  #conn.recv()는 데이터를 수신할 버퍼 (1024~4096 사이 값을 권장)
                if not data:
                    break
                print('메시지 수신 [%s]' %data.decode()) #수신한 데이터는 이진 바이트 스트림 이기때문에 decode()으로 문자열 변환
                conn.sendall(data)  #수신한 데이터를 다시 클라이언트로 전송

runServer()
