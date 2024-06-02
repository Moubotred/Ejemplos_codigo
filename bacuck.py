import tkinter as tk
import socket

root = tk.Tk()
root.geometry('289x470')
root.title('cliente')

label_cliente = tk.Label(root,text='CLIENTE',width=10,height=2,font=('Arial',15))
label_cliente.pack()

enlace = tk.Entry(root,width= 16 ,font=('Arial',20))
enlace.pack()

puerto = tk.Entry(root,width=5,font=('Arial',20))
puerto.place(relx=0.6,rely=0.3,anchor='center')

label_port = tk.Label(root,text='PORT',font=('Arial',15),bg='red')
label_port.place(relx=0.23,rely=0.27)

enviar = tk.Button(root,text='ENVIAR',font=('Arial',12))
enviar.place(relx=0.5,rely=0.6,anchor='center')

label_corriendo = tk.Label(root,text='',font=('Arial',15),borderwidth=0)
label_corriendo.place(relx=0.45,rely=0.30,anchor='center')

save = tk.Button(root,text='SAVE PORT',bg='green',font=('Arial',12))
save.place(relx=0.5,rely=0.44,anchor='center')

root.mainloop()