import socket
import tkinter as tk
from tkinter import messagebox
import pyperclip3

port = 16321
host = '0.tcp.sa.ngrok.io'
# crea una función para enviar la URL al servidor y recibir la respuesta
def send_url():
    url = url_entry.get()  # obtiene la URL ingresada por el usuario
    if url:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))  # conecta con el servidor
            s.sendall(url.encode())  # envía la URL al servidor
            data = s.recv(1024)  # recibe la respuesta del servidor
            response_label.configure(text=data.decode())  # actualiza la etiqueta de respuesta

def copy_to_clipboard():
    pyperclip3.copy(label_text.get())
    messagebox.showinfo("Copiado", "El texto ha sido copiado al portapapeles")


# crea una ventana principal para la interfaz gráfica
root = tk.Tk()
root.title('Cliente de URL')
root.geometry('300x500')

label_text = tk.StringVar()
label_text.set("Texto para copiar")


label = tk.Label(root, textvariable=label_text)
label.pack()

copy_button = tk.Button(root, text="Copiar", command=copy_to_clipboard)
copy_button.pack()


# crea un marco para los controles
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# crea un control de entrada para la URL
#url_entry = tk.Entry(frame, width=30 , height=5)
#url_entry.pack(side=tk.LEFT)
url_text = tk.StringVar()
url_entry = tk.Entry(frame, textvariable=url_text, width=30)
url_entry.config(font=('Arial', 20))  # Configura la fuente y el tamaño del texto
url_entry.pack(side=tk.TOP)


# crea un botón para enviar la URL al servidor
#send_button = tk.Button(frame, text='Enviar', font=('Arial',16),width=5,height=1,padx=10,pady=10,bd=9,relief=tk.RAISED,command=send_url)
send_button_color = '#BB8FCE'
send_button = tk.Button(frame, text='Enviar', font=('Arial',16),width=5,height=1,padx=10,pady=10,bd=9,relief=tk.RAISED,command=send_url, bg=send_button_color)
send_button.pack(side=tk.TOP, padx=70,pady=50)

# crea una etiqueta para la respuesta del servidor
response_label = tk.Label(root, text='')
response_label.pack(padx=10, pady=10)

# inicia el bucle principal de la interfaz gráfica
root.mainloop()
