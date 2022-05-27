import sqlite3



# Criando conexão
con = sqlite3.connect('dados.db')

"""
# criando tabela
with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE cadastroBeneficio
                   (nome TEXT, data date, beneficio TEXT, operacao TEXT)''')



lista = ['Elizabete Maria da Silva', 'AGU transporte','5/27/22','Inclusão']
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = ('''INSERT INTO cadastroBeneficio (nome,data,beneficio,operacao) VALUES(?,?,?,?)''')
        cur.execute(query, i)
inserir_info(lista)
"""


def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cadastroBeneficio"
        cur.execute(query)
        informacao = cur.fetchall()
        print(f'Primeiro print {informacao}')

        for i in informacao:
            print(i)
            lista.append(i)
    return lista

a = mostrar_info()
print(f'Eu sou o valor de retorno:    {a}')
"""

lista = ["Exclusão","Orlando Pedro Souto"]
with con:
    cur = con.cursor()
    query = '''UPDATE cadastroBeneficio SET operacao=? WHERE nome = ?'''
    cur.execute(query,lista)


lista = ["Orlando Pedro Souto"]
with con:
    cur = con.cursor()
    query = '''DELETE FROM cadastroBeneficio WHERE nome = ?'''
    cur.execute(query,lista)
"""