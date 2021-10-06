#Telas
from tkinter import *

#------------TELA 4-------------

class GenerosP(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Escolha o conteúdo')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Escolha o genero ', bg='#7030A0', fg = '#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.1, rely = 0.07)

        self.imaG7 = PhotoImage(file='p1.png')
        self.imaG8 = PhotoImage(file='p2.png')
        self.imaG9 = PhotoImage(file='p3.png')

        self.botao1 = Button(self, image = self.imaG7, height = 75, width = 75, command = self.Cbtn1).place(relx=0.02, rely=0.18, width=140, height=195)

        self.botao2 = Button(self, image = self.imaG8, width = 10, height = 10, command = self.Cbtn2).place(relx=0.52, rely=0.18, width=140, height=195)

        self.botao3 = Button(self, image = self.imaG9, command = self.Cbtn3).place(relx=0.28, rely=0.5, width=140, height=195)

        self.botaovoltar = Button(self, text='← Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.82,relwidth=0.7, relheight = 0.1)

    def Cbtn1(self):
        self.hide()
        self.abrir = Drama(self)

    def Cbtn2(self):
        self.hide()
        self.abrir = Infantil(self)

    def Cbtn3(self):
        self.hide()
        self.abrir = Cultural(self)

    def voltar(self):
        self.hide()
        self.volta = Escolha(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Drama(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Dramatico')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Dramatico', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.28, rely = 0.03)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def voltar(self):
        self.hide()
        self.volta = GenerosP(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Infantil(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Infantil')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Infantil', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.35, rely = 0.03)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def voltar(self):
        self.hide()
        self.volta = GenerosP(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()


class Cultural(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Cultural')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Cultural', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.3, rely = 0.03)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def voltar(self):
        self.hide()
        self.volta = GenerosP(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()




class Escolha(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('História ou Poema?')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Escolha', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.32, rely = 0.20)

        self.imghistoria = PhotoImage(file='historia.png')
        self.imgpoema = PhotoImage(file='poema.png')


        self.botaoH = Button(self, image = self.imghistoria,command=self.historia).place(relx=0.02, rely=0.38, width=140, height=195)

        self.botaoP = Button(self, image = self.imgpoema,command=self.poema).place(relx=0.52, rely=0.38, width=140, height=195)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def voltar(self):
        self.hide()
        self.volta = Tela7(self)

    def historia(self):
        self.hide()
        self.proxtela = GenerosH(self)

    def poema(self):
        self.hide()
        self.proxtela = GenerosP(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Aventura(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Aventura')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Aventura', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.28, rely = 0.03)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def voltar(self):
        self.hide()
        self.volta = GenerosH(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()
        
class Fantasia(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Fantasia')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Fantasia', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.28, rely = 0.03)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def voltar(self):
        self.hide()
        self.volta = GenerosH(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class Fabula(Toplevel): #Tela escolha de conteudo
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Fabulas')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")

        text = Label(self, text='Fabulas', bg='#7030A0', fg='#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.3, rely = 0.03)

        self.botao = Button(self, text='Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.85,relwidth=0.7, relheight = 0.1)

    def voltar(self):
        self.hide()
        self.volta = GenerosH(self)

    def hide(self):  # Esconde a janela root
        self.withdraw()

class GenerosH(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Escolha o conteúdo')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0") 

        text = Label(self, text='Escolha o genero ', bg='#7030A0', fg = '#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.1, rely = 0.07)

        self.imaG4 = PhotoImage(file='h1.png')
        self.imaG5 = PhotoImage(file='h2.png')
        self.imaG6 = PhotoImage(file='h3.png')

        self.botao1 = Button(self, image = self.imaG4, height = 75, width = 75, command = self.Cbtn1).place(relx=0.02, rely=0.18, width=140, height=195)

        self.botao2 = Button(self, image = self.imaG5, width = 10, height = 10, command = self.Cbtn2).place(relx=0.52, rely=0.18, width=140, height=195)

        self.botao3 = Button(self, image = self.imaG6, command = self.Cbtn3).place(relx=0.28, rely=0.5, width=140, height=195)

        self.botaovoltar = Button(self, text='← Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.17,rely=0.82,relwidth=0.7, relheight = 0.1)

    def Cbtn1(self):
        self.hide()
        self.abrir = Aventura(self)

    def Cbtn2(self):
        self.hide()
        self.abrir = Fantasia(self)

    def Cbtn3(self):
        self.hide()
        self.abrir = Fabula(self)

    def Cbtn4(self):
        self.hide()
        self.abrir = Drama(self)

    def voltar(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Escolha(self)
    def hide(self):  # Esconde a janela root
        self.withdraw()

class Tela7(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('Escolha o conteúdo')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0") 

        text = Label(self, text='Escolha o conteúdo ', bg='#7030A0', fg = '#ffffff', font=('Poppins', 20, 'bold'))
        text.place(relx=0.04, rely = 0.07)

        self.imaG4 = PhotoImage(file='1.png')
        self.imaG5 = PhotoImage(file='2.png')
        self.imaG6 = PhotoImage(file='3.png')


        botao5 = Button(self, image = self.imaG4, command = self.abrirBotao5).place(relx=0.02, rely=0.18, relwidth=0.46, relheight=0.3)

        botao6 = Button(self, image = self.imaG5).place(relx=0.52, rely=0.18, relwidth=0.46, relheight=0.3)

        botao7 = Button(self, image = self.imaG6).place(relx=0.29, rely=0.5, relwidth=0.46, relheight=0.3)

        '''self.botaovoltar = Button(self, text='← Voltar', font = 'Poppins-Regular.ttf', command=self.voltar).place(relx=0.15,rely=0.82,relwidth=0.7, relheight = 0.1)'''

    def abrirBotao5(self):
        self.hide()
        self.abrir = Escolha(self)

    def voltar(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Tela7(self)
    def hide(self):  # Esconde a janela root
        self.withdraw()


'''class Tela4(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('MENU PRINCIPAL')       # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0") 

        text = Label(self, text='Escolha o conteúdo ', bg='#7030A0', font=('Poppins', 20, 'bold'))
        text.place(relx=0.055, rely = 0.1)

        self.imaG = PhotoImage(file='1.png')
        self.imaG = self.imaG.subsample(2, 2)
        self.imag = Label(self, image=self.imaG, bd=1, bg = '#7030A0' ).place(relx=0.02, rely=0.23, relwidth=0.46, height=0.3)

        self.imaG1 = PhotoImage(file='2.png')
        self.imaG1 = self.imaG1.subsample(2, 2)
        self.imag = Label(self, image=self.imaG1, bd=1, bg = '#7030A0' ).place(relx=0.52, rely=0.23, relwidth=0.46, relheight=0.3)

        self.imaG2 = PhotoImage(file='3.png')
        self.imaG2 = self.imaG2.subsample(2, 2)
        self.imag = Label(self, image=self.imaG2, bd=1, bg = '#7030A0' ).place(relx=0.02, rely=0.55, relwidth=0.46, relheight=0.3)

        self.imaG3 = PhotoImage(file='4.png')
        self.imaG3 = self.imaG3.subsample(2, 2)
        self.imag = Label(self, image=self.imaG3, bd=1, bg = '#7030A0' ).place(relx=0.52, rely=0.55, relwidth=0.46, relheight=0.3)'''

#------------TELA 3----------------
class Tela3(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('CADASTRO')             # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0") 
        # Inserindo texto
        Label(self, text='Nome de usuário: ', bg='#7030A0').place(relx=0.1, rely=0.67)
        Label(self, text='Senha:', bg='#7030A0').place(relx=0.1, rely=0.75)
        # Comando para mudar escrita inserida na lacuna
        self.senha = StringVar()
        # Inserindo lacunas
        self.entra = Entry(self, bd=2).place(relx=0.1, rely=0.70, relwidth = 0.78)
        self.entra2= Entry(self, textvariable = self.senha, show = '*', bd=2).place(relx=0.1, rely=0.78, relwidth = 0.78)
        #Inserindo botão
        self.avancar = Button(self, text='ENTRAR', font=('Arial', 10, 'bold'),bg = '#7030A0', command= self.onClose).place(relx=0.35,rely=0.93,relwidth=0.3,)
        
        
        self.buton = Button(self, text='⇦', bg='#7030A0', bd=5, command=self.onbotao
        ).place(relx=0.05, rely=0.027,relwidth=0.088,relheight=0.037)
        #Inserindo imagem
        self.imaG = PhotoImage(file='cleber.png')
        self.imaG = self.imaG.subsample(4, 4)
        self.imag = Label(self, image=self.imaG, bd=1, bg = '#7030A0' ).place(relx=0.064, rely=0.12, relwidth=0.85, relheight=0.5)
    def onClose(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Tela7(self)
    def onbotao(self): # Comando para ir voltar a tela anterior
        self.hide()
        self.frame_original.show()
    def hide(self):  # Esconde a janela root
        self.withdraw()
#------------TELA 2-----------
class Tela2(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('CADASTRO')             # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")       # Inserindo cor da tela
        # Inserindo texto
        Label(self, text='Nome de usuário: ', bg='#7030A0').place(relx=0.1, rely=0.67)
        Label(self, text='Senha:', bg='#7030A0').place(relx=0.1, rely=0.75)
        Label(self, text='Confirmar senha:', bg='#7030A0').place(relx=0.1, rely=0.83)
        # Comando para mudar escrita inserida na lacuna
        self.senha = StringVar()
        self.senha1 = StringVar()
        # Inserindo lacunas
        self.entra = Entry(self, bd=2).place(relx=0.1, rely=0.70, relwidth = 0.78)
        self.entra2= Entry(self, textvariable = self.senha, show = '*', bd=2).place(relx=0.1, rely=0.78, relwidth = 0.78)
        self.entra3 = Entry(self, textvariable = self.senha1, show = '*', bd=2).place(relx=0.1, rely=0.86, relwidth = 0.78)
        #Inserindo botão
        self.avancar = Button(self, text='LOGAR', font=('Arial', 10, 'bold'),bg = '#7030A0', command= self.onClose).place(relx=0.35,rely=0.93,relwidth=0.3,)
        
        self.buton = Button(self, text='⇦', bg='#7030A0', bd=5, command= self.voltar).place(relx=0.05, rely=0.027,relwidth=0.088,relheight=0.037)
        #Inserindo imagem
        self.imaG = PhotoImage(file='cleber.png')
        self.imaG = self.imaG.subsample(4, 4)
        self.imag = Label(self, image=self.imaG, bd=1, bg = '#7030A0' ).place(relx=0.064, rely=0.12, relwidth=0.85, relheight=0.5)
    def onClose(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Tela7(self)

    def voltar(self): # Comando para ir para a proxima tela
        self.hide()
        self.frame_original.show()


    def hide(self):  # Esconde a janela root
        self.withdraw()


#------------------TELA 1---------------
class Tela1:
    def __init__ (self): #Inserindo funções
        self.root = root
        self.telinha()
        self.frame()
        self.wid()
        self.texto()
        self.imagem()
        root.mainloop()
    def telinha(self):
        self.root.title('BOMTCHAU')       # Inserindo nome da janela
        self.root.geometry('300x647+540+15')    # Inserindo tamanho da janela
        #Inserindo cores na tela
    def frame(self):
        self.frame1 = Frame(self.root, bg='#7030A0').place(relx=0.001, rely=0.001, relwidth=1, relheight=1)
        # Inserindo botão
    def wid(self):
        self.login = Button (self.frame1,text='Login',font=('Arial', 12, 'bold'), bg = '#ED7D31', command= self.clica2).place(relx=0.54, rely=0.9, relwidth=0.4, relheight=0.05)
        self.cadastrar = Button (self.frame1,text='Cadastrar',font=('Arial', 12, 'bold'), bg = '#ED7D31', command= self.clica).place(relx=0.06, rely=0.9, relwidth=0.4, relheight=0.05)
        #Inserindo Texto
    def texto(self):
        root.titulo= Label(self.frame1,text='BOMTCHAU',font='PoppinsBlack 16',bg='#7030A0').place(x=90, y=40)
        root.palavrinha = Label(self.frame1, text = 'Seja bem-vinda(o)', font = 'PoppinsBlack 12',bg='#7030A0').place(x= 85, y= 430)
        #Inserindo imagem
    def imagem(self):
        self.imagem = PhotoImage(file= 'cleber.png')
        self.imagem = self.imagem.subsample(1, 1)
        self.imageg= Label(self.frame1, image=self.imagem, bd=0,).place(relx=0.1, rely=0.17, relwidth=0.82, relheight=0.4)
    def clica(self): #Comando para próxima tela
        self.hide()
        self.subTela = Tela2(self)
    def clica2(self): #Comando para próxima tela
        self.hide()
        self.subTela = Tela3(self)
    def hide(self): # Escondendo tela
        self.root.withdraw()
    def show(self):  # Comando para destruir tela
        self.root.update()
        self.root.deiconify()


class Tela5(Toplevel): #Pagina do cadastro
    def __init__(self, original): #Inserindo inicialização
        self.frame_original = original
        Toplevel.__init__(self)
        self.title('LOGIN')             # Inserindo nome da janela
        self.geometry('300x647+540+15')    # Inserindo tamanho da janela
        self.configure(bg="#7030A0")       # Inserindo cor da tela
        # Inserindo texto
        Label(self, text='Nome de usuário: ', bg='#7030A0').place(relx=0.1, rely=0.67)
        Label(self, text='Senha:', bg='#7030A0').place(relx=0.1, rely=0.75)
        Label(self, text='Confirmar senha:', bg='#7030A0').place(relx=0.1, rely=0.83)
        # Comando para mudar escrita inserida na lacuna
        self.senha = StringVar()
        self.senha1 = StringVar()
        # Inserindo lacunas
        self.entra = Entry(self, bd=2).place(relx=0.1, rely=0.70, relwidth = 0.78)
        self.entra2= Entry(self, textvariable = self.senha, show = '*', bd=2).place(relx=0.1, rely=0.78)
        self.entra3 = Entry(self, textvariable = self.senha1, show = '*', bd=2).place(relx=0.1, rely=0.86)
        #Inserindo botão
        self.avancar = Button(self, text='LOGAR', font=('Arial', 10, 'bold'),bg = '#7030A0', command= self.onClose).place(relx=0.35,rely=0.93,relwidth=0.3,)
        self.buton = Button(self, text='⇦', command= self.onbotao, bg='#7030A0', bd=5).place(relx=0.05, rely=0.027,relwidth=0.088,relheight=0.037)
        #Inserindo imagem
        self.imaG = PhotoImage(file='cleber.png')
        self.imaG = self.imaG.subsample(4, 4)
        self.imag = Label(self, image=self.imaG, bd=1, bg = '#7030A0' ).place(relx=0.064, rely=0.12, relwidth=0.85, relheight=0.5)
    def onClose(self): # Comando para ir a próxima tela
        self.hide()
        self.abrir = Tela7(self)
    def onbotao(self): # Comando para voltar a tela anterior
        self.hide()
        self.abrir = Tela1(self)
    def hide(self):  # Esconde a janela root
        self.withdraw()

root = Tk()
Tela1()

