import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        port = 19185
        host = '0.tcp.sa.ngrok.io'  # Ingresar la direcciÃ³n de Ngrok proporcionada por el servidor
        s.connect((host,port))

        # espera a que el usuario ingrese una URL y la envía al servidor
        while True: 
            url = input('Ingrese una URL (o presione Enter para salir): ')
            if not url:
                break  # si no se ingresa ninguna URL, finaliza el programa

            s.sendall(url.encode())  # codifica y envía la URL al servidor
            data = s.recv(1024)  # recibe la respuesta del servidor

                # decodifica y muestra la respuesta del servidor
            print('Respuesta del servidor:', data.decode())
                

    except KeyboardInterrupt as error:
        print(error)
