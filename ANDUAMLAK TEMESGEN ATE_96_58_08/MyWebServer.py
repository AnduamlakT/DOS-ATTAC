import socket

HOST = ''
PORT = 7070

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))

print("Serving HTTP on port ", PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(7070)
    print(request)

    http_response = """\HTTP/1.1 200 OK SUCCESSFUL """

    client_connection.sendall(http_response)
    client_connection.closse()
                         
