import socket

def ConexionLocal():

    HOST = '0.tcp.sa.ngrok.io'
    PORT = 16273

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            msg = input("Ingrese plataforma: ")
            data = s.recv(1024)
            msg = data.decode()

            # start_log_thread(msg)

            if msg == "kion":
               break

            s.sendall(bytes(msg, 'utf-8'))
