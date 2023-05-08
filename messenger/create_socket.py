import socket

# Создаем сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Указываем адрес и порт сервера
server_address = ('192.168.1.55', 65432)

# Привязываем сокет к заданному адресу и порту
sock.bind(server_address)

# Начинаем прослушивать входящие соединения
sock.listen(1)

# Ожидаем соединение
connection, client_address = sock.accept()

# Получаем данные от клиента
data = connection.recv(1024)

# Отправляем данные клиенту
connection.sendall(data)

# Закрываем соединение
connection.close()
