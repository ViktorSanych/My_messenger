import socket

HOST = ''  # Адрес сервера
PORT = 8888  # Порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Подключение к серверу

    while True:
        message = input('Введите сообщение: ')
        s.sendall(message.encode())  # Отправка сообщения на сервер

        response = s.recv(1024)  # Получение ответа от сервера
        print(response.decode())  # Вывод ответа на экран
