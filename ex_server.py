import socket

def handle_client(client_socket):
    while True:
        # 클라이언트로부터 데이터 수신
        data = client_socket.recv(1024)
        if not data:
            break  # 연결이 끊긴 경우 루프 종료

        message = data.decode()
        print(f"Received data: {message}")

        # 응답 결정
        if message.lower() == '참생도':
            response = '참생도입니다'
            client_socket.sendall(response.encode())
            client_socket.close()
            return True
        else:
            response = f"참생도가 아닙니다"

        # 클라이언트로 응답 전송
        client_socket.sendall(response.encode())

    # 클라이언트 소켓 닫기
    client_socket.close()

# TCP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 주소 재사용 옵션 설정
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 소켓을 localhost의 12345 포트에 바인드
server_socket.bind(('localhost', 12345))

# 연결 요청 대기
server_socket.listen()

print("Server waiting for connections...")
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connected by {addr}")
    handle_client(client_socket)

# 소켓 닫기 (일반적으로 서버는 계속 실행되므로 이 부분은 도달하지 않습니다)
server_socket.close()
