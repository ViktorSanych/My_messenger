import socket
import threading

HOST = ''  # Локальный адрес сервера
PORT = 8888  # Выбранный порт


def handle_client(conn, addr):
    """Обработка подключения клиента"""
    print(f'Подключение клиента {addr}')

    while True:
        data = conn.recv(1024)  # Получение данных от клиента
        if not data:
            break
        message = data.decode()  # Преобразование данных в строку
        print(f'Клиент {addr}: {message}')  # Вывод сообщения клиента на сервер

        # Отправка сообщения клиенту
        response = f'Сервер: Получено сообщение "{message}"'
        conn.sendall(response.encode())

    # Закрытие соединения с клиентом
    print(f'Отключение клиента {addr}')
    conn.close()


def start_server():
    """Запуск сервера"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Сервер запущен на {HOST}:{PORT}')

        while True:
            conn, addr = s.accept()  # Ожидание подключения клиента
            threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == '__main__':
    start_server()
