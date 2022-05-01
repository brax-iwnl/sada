##-----------------------------------IMPORTACOES--------------------------------------------
# Importação de bibliotecas ou módulos
from tkinter import *
import serial
from PIL import ImageTk, Image
import time

##--------------------------------DEFINICOES INICIAIS------------------------------------
# inicia a inteface
menu = Tk()
menu.title("S.A.P.A.P.D.A.")
menu["bg"] = "black"

# Configurando a tela
app_width = 640
app_height = 480
tela_width = menu.winfo_screenwidth()
tela_height = menu.winfo_screenheight()
x = (tela_width / 2) - (app_width / 2)
y = (tela_height / 2) - (app_height / 2)
menu.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
menu.resizable(1, 1)
# inicia a Comunicacao Serial
comunicacaoSerial = serial.Serial('/dev/ttyACM0', 2000000)

##-------------------------------------IMAGENS----------------------------------------------
# Configurando imagens
# Carro
carro1 = Image.open("imagens/carro.png")
resized1 = carro1.resize((290, 300), Image.ANTIALIAS)
car = ImageTk.PhotoImage(resized1)

#Esquerda
esquerda1 = Image.open("imagens/esquerda/1.png")
resized2 = esquerda1.resize((175, 120), Image.ANTIALIAS)
left1 = ImageTk.PhotoImage(resized2)
esquerda2 = Image.open("imagens/esquerda/5.png")
resized3 = esquerda2.resize((175, 120), Image.ANTIALIAS)
left2 = ImageTk.PhotoImage(resized3)

#Direita
direita1 = Image.open("imagens/direita/1.png")
resized4 = direita1.resize((175, 120), Image.ANTIALIAS)
right1 = ImageTk.PhotoImage(resized4)
direita2 = Image.open("imagens/direita/5.png")
resized5 = direita2.resize((175, 120), Image.ANTIALIAS)
right2 = ImageTk.PhotoImage(resized5)

#Traseira
traseira1 = Image.open("imagens/traseira/1.png")
resized6 = traseira1.resize((175, 120), Image.ANTIALIAS)
back1 = ImageTk.PhotoImage(resized6)
traseira2 = Image.open("imagens/traseira/5.png")
resized7 = traseira2.resize((175, 120), Image.ANTIALIAS)
back2 = ImageTk.PhotoImage(resized7)

carro = Label(menu, image=car, borderwidth=0)
carro.grid(row=1, column=1)
esquerda = Label(menu, image=left1, borderwidth=0)
esquerda.grid(row=1, column=0)
direita = Label(menu, image=right1, borderwidth=0)
direita.grid(row=1, column=2)
traseira = Label(menu, image=back1, borderwidth=0)
traseira.grid(row=2, column=1)


# --------------------------------------FUNCOES------------------------------------------
def Iniciar():
    valor_recebido1 = comunicacaoSerial.readline()
    valor_recebido = valor_recebido1.decode("utf-8")
    lista1 = valor_recebido.split('\r')
    lista2 = lista1[0].split('|')
    sensor1 = lista2[0].split(',')
    sensor2 = lista2[1].split(',')
    sensor3 = lista2[2].split(',')
    s1a = sensor1[0]
    s1d = sensor1[1]
    s2a = sensor2[0]
    s2d = sensor2[1]
    s3a = sensor3[0]
    s3d = sensor3[1]
    lb1["text"] = s1a
    lb2["text"] = s1d
    lb3["text"] = s2a
    lb4["text"] = s2d
    lb5["text"] = s3a
    lb6["text"] = s3d
    if int(s1d) == 1 & int(s2d) == 1 & int(s3d) == 1:
        esquerda["image"] = left2
        direita["image"] = right2
        traseira["image"] = back2
    elif int(s1d) == 1:
        esquerda["image"] = left2
    elif int(s2d) == 1:
        direita["image"] = right2
    elif int(s3d) == 1:
        traseira["image"] = back2
    else:
        esquerda["image"] = left1
        direita["image"] = right1
        traseira["image"] = back1
    # print(s1a)
    menu.after(1, Iniciar)


# --------------------------------------INTERFACE---------------------------------------

lb1 = Label(menu, text="label")
lb1.grid(row=1, column=0)
lb2 = Label(menu, text="label")
lb2.grid(row=0, column=0)
lb3 = Label(menu, text="label")
lb3.grid(row=1, column=2)
lb4 = Label(menu, text="label")
lb4.grid(row=0, column=2)
lb5 = Label(menu, text="label")
lb5.grid(row=2, column=1)
lb6 = Label(menu, text="label")
lb6.grid(row=2, column=0)
menu.after(1, Iniciar)
menu.mainloop()
