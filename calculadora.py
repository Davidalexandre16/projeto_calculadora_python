from tkinter import *
from tkinter import ttk



# CORES DA CALCULADORA
cor1 = "#000000" #preto
cor2 = "#1c5cff" #azulclaro
cor3 = "#ffffff" #branco
cor4 = "#ff851c" #laranja



janela = Tk()
janela.title("Calculadora")
janela.geometry("235x305")
janela.config(bg=cor1)



# CRIANDO FRAMES
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


# VARIAVEL TODOS OS VALORES

todos_valores = ''

#CRIANDO FUNÇÃO
def recebendo_valores(event):

 global todos_valores

 todos_valores = todos_valores + str(event)


#PASSANDO VALOR PARA TELA
 valor_texto.set(todos_valores)


#FUNÇÃO PARA CALCULAR
def calcular():
 global todos_valores
 resultado = eval(todos_valores)
 valor_texto.set(str(resultado))
 todos_valores = str(resultado)


#FUNÇÃO LIMPAR TELA
def limpar_tela():
 global todos_valores
 todos_valores = ""
 valor_texto.set("")



#CRIANDO LABEL
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('arial'), bg = cor3, fg=cor1)
app_label.place(x=0,y=0)



#CRIANDO OS BOTÕES
b_1 = Button(frame_corpo, command=limpar_tela , text ="C", width=5, height=2, bg=cor3, fg=cor4, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frame_corpo,command = lambda: recebendo_valores('( )'), text="( )", width=5, height=2,bg=cor3,fg=cor2, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59,y=0)
b_2 = Button(frame_corpo, command = lambda: recebendo_valores('%'),text="%", width=5, height=2,bg=cor3,fg=cor2, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118,y=0)
b_3 = Button(frame_corpo,command = lambda: recebendo_valores('/'), text="/", width=5, height=2,bg=cor3, fg=cor2, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177,y=0)


b_4 = Button(frame_corpo, command = lambda: recebendo_valores('7'),text="7", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0,y=52)
b_5 = Button(frame_corpo,  command = lambda: recebendo_valores('8'),text="8", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59,y=52)
b_6 = Button(frame_corpo,  command = lambda: recebendo_valores('9'),text="9", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118,y=52)
b_7 = Button(frame_corpo, command = lambda: recebendo_valores('*'), text="*", width=5, height=2,bg=cor3, fg=cor2, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177,y=52)


b_8 = Button(frame_corpo,  command = lambda: recebendo_valores('4'), text="4", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0,y=102)
b_9 = Button(frame_corpo,  command = lambda: recebendo_valores('5'), text="5", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59,y=102)
b_10 = Button(frame_corpo,  command = lambda: recebendo_valores('6'), text="6", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118,y=102)
b_11 = Button(frame_corpo,  command = lambda: recebendo_valores('-'), text="-", width=5, height=2,bg=cor3, fg=cor2, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177,y=102)


b_12 = Button(frame_corpo,  command = lambda: recebendo_valores('1'), text="1", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0,y=152)
b_13= Button(frame_corpo,  command = lambda: recebendo_valores('2'), text="2", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59,y=152)
b_14 = Button(frame_corpo,  command = lambda: recebendo_valores('3'), text="3", width=5, height=2,bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118,y=152)
b_15 = Button(frame_corpo,  command = lambda: recebendo_valores('+'), text="+", width=5, height=2,bg=cor3, fg=cor2, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177,y=152)


b_16 = Button(frame_corpo,  command = lambda: recebendo_valores('0'), text="0", width=11, height=2, bg=cor3, fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0,y=202)
b_17 = Button(frame_corpo,  command = lambda: recebendo_valores('.'), text=".", width=5, height=2,bg=cor3,fg=cor1, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118,y=202)
b_18 = Button(frame_corpo, command = calcular, text= "=", width= 5, height=2,bg=cor2, fg=cor3, font=('arial'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177,y=202)



janela.mainloop()