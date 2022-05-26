from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

janela = Tk()

janela.title('BENEFÍCIOS')
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

#### Dividindo a janela principal #######

frame_cima = Frame(janela, width=310, height=50, background=co2, relief='flat')
frame_cima.grid(row=0,column=0)

frame_baixo= Frame(janela, width=310, height=403, background=co1, relief='flat')
frame_baixo.grid(row=1,column=0, pady=1, padx=1)

"""
Veja que no frame_cima temos um frame com width (largura) de 310 e hight (altura) de 50. logo a única célula defiida
para esse frame terá o mesmo tamanho.
Observe que o frame_direta tem a mesma altura do frame_baixo, Entretanto ele oculpa 2 linhas mescladas (rowspan). Por isso
haverá espaços acima e abaixo do frame_direita. Observe que a altura dele é 403 e a altura da janela é 453.
Diferença de 50, ou seja 25 na parte de cima e 25 na parte de baixo.
Esse espaço é necessário porque haverá uma barra de rolagem horizontal e vertical
O pady e padx basicamente separam os frames. Experimente aumentar qualquer um deles em 100 e verá o resultado.
"""
frame_direita= Frame(janela, width=588, height=403, background=co1, relief='flat')
frame_direita.grid(row=0,column=1, rowspan=2, pady=0, padx=1)

#### Label cima #######

"""
Veja que usamos o place dentro do frame_cima criado por grid. O place nos dará a distancia do label da borda do frame, 
no caso frame_cima.
"""
app_nome = Label(frame_cima, text= 'Cadastro de Beneficios', anchor=NW, font=('Helvetica', '16'), background=co2)
app_nome.place(x=10, y=10)


#### Configurando frame-baixo #######

l_nome = Label(frame_baixo, text= 'Nome*', anchor=NW, font=('Helvetica', '12'), bg=co1 )
l_nome.place(x=10, y=10)

e_nome = Entry(frame_baixo, width=40, relief=SOLID)
e_nome.place(x=10, y= 40)

l_beneficio = Label(frame_baixo, text= 'Beneficio*', anchor=NW, font=('Helvetica', '12'), bg=co1 )
l_beneficio.place(x=10, y=90)

b_list = ["Auxílio transporte", "Pre Escolar", "Natalidade", "AGU transporte"]
combo_beneficio = ttk.Combobox(frame_baixo, values=b_list)
combo_beneficio.place(x=10, y= 120)

l_data = Label(frame_baixo, text= 'Data*', anchor=NW, font=('Helvetica', '12'), bg=co1 )
l_data.place(x=10, y=170)

e_cal = DateEntry(frame_baixo, width=12)
e_cal.place(x=10, y= 200)

l_operacao = Label(frame_baixo, text= 'Operacao*', anchor=NW, font=('Helvetica', '12'), bg=co1 )
l_operacao.place(x=10, y=240)


vlist = ["Exclusão", "Suspensão", "Inclusão"]
combo_operacao = ttk.Combobox(frame_baixo, values=vlist)
combo_operacao.place(x=10, y= 270)

janela.mainloop()