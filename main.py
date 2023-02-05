import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

cor0 = '#000000' #preto
cor1 = '#ffffff' #branco
cor2 = '#91b7bf' #azul framde de cima
cor3 = '#cadce0' # azul frame debaixo
cor4 = '#4e8a96' # azul faixa
cor5 = '#1e8a40' #verde botao
cor6 = '#a31826' #vermelho botao

janela = Tk()
janela.geometry("450x380")
janela.title('Tela Login')
janela.resizable(width=False, height=False)





icon_login = tk.PhotoImage(file="login.png")
icon_login = icon_login.subsample(10, 10)


# criando frames
frame_cima = Frame(janela, width=500, height=100, bg=cor2,)
frame_cima.grid(column=0, row=0)

logo = Label(frame_cima, image=icon_login)
logo.place(x=40, y=30)

frame_meio = Frame(janela, width=500, height=10, bg=cor4)
frame_meio.grid(column=0, row=1)

frame_debaixo = Frame(janela, width=500, height=400, bg=cor3)
frame_debaixo.grid(column=0, row=2)

label_login = Label(frame_cima, text='Login', font=('Verdana 22 bold'), bg=cor2 )
label_login.place(x=120, y=40)


#criando labels
l_nome = Label(frame_debaixo, text='Usuario:',font=('Verdana 15'), bg=cor3, )
l_nome.place(x=35, y=30)

l_senha = Label(frame_debaixo, text='Senha:',font=('Verdana 15'), bg=cor3, )
l_senha.place(x=35, y=100)



#criando Entry
e_nome = Entry(frame_debaixo, width=30,)
e_nome.place(x=130, y=38)

e_senha = Entry(frame_debaixo, width=30, show='*')
e_senha.place(x=130, y=108)




#funcao login e senha
def verificar_senha():
    if e_nome.get() == "admin" and e_senha.get() == "admin":
        messagebox.showinfo('Info', 'login realizado com sucesso!')
    else:
        messagebox.showerror('Error', 'Usuario ou senha invalidos, verifique e tente novamente!')


def cancelar():
    messagebox.showinfo('Info', 'Obrigado por usar o nosso sistema!')




#importando imagens

icon_entrar = tk.PhotoImage(file="entrar.png")
icon_entrar = icon_entrar.subsample(25, 25)

icon_sair = tk.PhotoImage(file="sair.png")
icon_sair = icon_sair.subsample(40, 40)




#criando Botoes
bt_entrar = Button(frame_debaixo, text=' Entrar', command=verificar_senha, width=70, font=('verdana, 11 '), image = icon_entrar, compound = LEFT)
bt_entrar.place(x=125, y=170)

bt_cancelar = Button(frame_debaixo, text=' Cancelar', command=cancelar, width=80, font=('verdana, 11 '), image = icon_sair, compound = LEFT)
bt_cancelar.place(x=225, y=170)



janela.mainloop()
