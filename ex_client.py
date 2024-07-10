import socket

# TCP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버의 주소와 포트로 연결
client_socket.connect(('localhost', 12345))

try:
    while True:
        # 키보드 입력을 통해 서버로 메시지 전송
        message = input("당신은 참생도입니까?: ").strip()
        if not message:
            continue  # 빈 입력은 무시

        client_socket.sendall(message.encode())

        # 서버로부터 응답 수신
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

        if message.lower() == '참생도':
            break
finally:
    # 소켓 닫기
    client_socket.close()
