from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from bancoDados import *

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
janela.geometry('1137x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

def incluir():

    global tree

    nome = e_nome.get()
    beneficio = combo_beneficio.get()
    data = e_cal.get()
    operacao = combo_operacao.get()

    lista = [nome, beneficio,data,operacao]

    inserir_info(lista) #insere o cadastro no banco de dados

    tree.insert("", 'end', values=lista)  # insere o cadastro no treeview

def excluir():
    global tree
    a = tree.focus() # coloca o elemento da árvore treeviw focado na variável a. São vários os elementos mas queremos só os valores
    b = tree.item(a, "values") # extrai somente os values (aquilo que é visível no treeview)
    tree.delete(a)  # exlui o elemento selecionado da árvore. No entanto temos que exluir do banco de dados
    """ 
                         Para exluir do banco de dados  temos ver como está cadastrado
                        O cadastro no banco de dados é igual a varável b acima. No banco de dados vamos exluir pelo nome(vide BancoDados.py)
                        O nome é o primeiro item da variável b.
                        Então vamos selecioná-lo usando o método islaice e atribuindo o valor a variável c: c = b[0].                         
                         O valor de c será 'fffff'. No entanto eu preciso que seja ['fffff'] com aspas e entre colchetes.
                        Preciso de  ["fffff"] porque no meu banco de dados eu o configurei para receber o valor dessa forma
                        Conforme acima 'ffff' está atribuído à variável c. 
                        Para obtermos de 'ffff' o valor ["fffff"]  basta fazer o seguinte: d = [c]
                        O valor de d será ["fffff"].                        
                        Pronto. Agora temos o valor para colocarmos como parametro para a função de exclusão que está no banco de dados
                        
    """
    c = b[0]
    d = [c]

    exluir_info(d) # irá excluir do banco de dados o item selecionado do treeview










################### Dividindo a janela principal ######################

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

###################### Label cima ########################

"""
Veja que usamos o place dentro do frame_cima criado por grid. O place nos dará a distancia do label da borda do frame, 
no caso frame_cima.
"""
app_nome = Label(frame_cima, text= 'Cadastro de Beneficios', anchor=NW, font=('Helvetica', '16'), background=co2)
app_nome.place(x=10, y=10)


###################### Configurando frame-baixo ########################

l_nome = Label(frame_baixo, text= 'Nome*', anchor=NW, font=('Helvetica', '12'), bg=co1 )
l_nome.place(x=10, y=10)

e_nome = Entry(frame_baixo, width=40, relief=SOLID)
e_nome.place(x=10, y= 40)

l_beneficio = Label(frame_baixo, text= 'Beneficio*', anchor=NW, font=('Helvetica', '12'), bg=co1 )
l_beneficio.place(x=10, y=90)

b_list = ["Auxílio transporte", "Pre Escolar", "Natalidade", "AGU transporte"]
b_list.sort()
combo_beneficio = ttk.Combobox(frame_baixo, values=b_list)
combo_beneficio.place(x=10, y= 120)

l_data = Label(frame_baixo, text= 'Data*', anchor=NW, font=('Helvetica', '12'), bg=co1 )
l_data.place(x=10, y=170)

e_cal = DateEntry(frame_baixo, width=12)
e_cal.place(x=10, y= 200)

l_operacao = Label(frame_baixo, text= 'Operacao*', anchor=NW, font=('Helvetica', '12'), bg=co1 )
l_operacao.place(x=10, y=240)


vlist = ["Exclusão", "Suspensão", "Inclusão", "Atualização"]
vlist.sort()
combo_operacao = ttk.Combobox(frame_baixo, values = vlist)
combo_operacao.place(x=10, y= 270)

#######BOTOÕES###########

## Botao incluir ##
b_inserir = Button(frame_baixo, text= 'Incluir', command=incluir, font=('Helvetica', '12'), bg=co6, fg=co1 )
b_inserir.place(x=10, y=340)

## Botao excluir##
b_excluir = Button(frame_baixo, text= 'Excluir', command=excluir,  font=('Helvetica', '12'), bg=co6, fg=co1 )
b_excluir.place(x=65, y=340)

## Botao suspender##
b_suspender = Button(frame_baixo, text= 'Suspender', font=('Helvetica', '12'), bg=co6, fg=co1)
b_suspender.place(x=127, y=340)

## Botao atualizar##
b_atualizar = Button(frame_baixo, text= 'Atualizar', font=('Helvetica', '12'), bg=co6, fg=co1)
b_atualizar.place(x=220, y=340)


###################### Configurando frame-direita (TREEVIW) ########################

def mostrar():

    global tree
    df_list = mostrar_info() # pega a tabela que está no banco de dados e coloca na variável df_list

    head = ["Nome", "Beneficio","Data","Operacao"]
    tree = ttk.Treeview(frame_direita, columns=head, height=20, show='headings')


    tree.heading('#0', text='vazio')
    tree.heading('Nome', text='Nome')
    tree.heading('Beneficio', text='Beneficio')
    tree.heading('Data', text='Data')
    tree.heading('Operacao', text="Operacao")

    tree.column("Nome", width=300)
    tree.column("Data", width=100)


    vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

    """
        Aqui será mostrado os valores que se encontram no banco de dados. Eles serão puxados para o treeview
        
       Inserindo no treeviw os valores que estão no banco de dados.
       
       - Antes de tudo é preciso buscar os valores no banco de dados. Busca-se os valores através do SELECT
       - No banco de dados vamos criar uma função que retorna os valores do banco de dados.
       - Os valores de cada linha da tabela no banco de dados estão na forma de tupla.
       - Precisamos colocar todos as linhas da tabela entro de uma lista.
       - Essa lista que conterá várias tuplas é o retorno da nossa função mostrar_info que está no banco de dados
       - Todas as informações do banco de dados estarão na lista mencionada
       - É preciso percorrer a lista de informação e inserila no treeview
       - Para isso usa-se a função insert que está logo abaixo        
    
    """

    for i in df_list:
        tree.insert("",'end', values=i)


    tree.grid(column=0, row=0)
    vsb.grid(column=1, row=0)
    hsb.grid(column=0, row=1)

mostrar()
janela.mainloop()