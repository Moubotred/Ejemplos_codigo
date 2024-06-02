import socket
import requests
from webbrowser import open

def BuscarIp():
    try:
        # Obtener el nombre del host local
        nombre_host = socket.gethostname()
        # Obtener la dirección IP asociada con el nombre del host
        direccion_ip = socket.gethostbyname(nombre_host)
        return direccion_ip
    except socket.error as e:
        print(f"Error al obtener la dirección IP: {e}")
        return None

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as servidor:
    try:
        port = 23235
        host =  '0.tcp.sa.ngrok.io'
        servidor.bind((host, port))
        servidor.listen()
        print(f'conexion iniciada {host}')
        while True:
            serv,ip = servidor.accept()
            with serv:        
                while True:
                    print(f'conexion establecida desde {ip}')
                    mensaje = serv.recv(1024)
                    if not mensaje:
                        break
                    url = mensaje.decode()
                    open(url)
                    stado = requests.get(url)
                    msg_client = f'status: {stado.status_code}'
                    serv.sendall(msg_client.encode())
                    
    except KeyboardInterrupt as erro:
        print(erro)




