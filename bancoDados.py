import sqlite3



# Criando conexão
con = sqlite3.connect('dados.db')

"""
# criando tabela
with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE cadastroBeneficio
                   (nome TEXT, data date, beneficio TEXT, operacao TEXT)''')


"""

def inserir_info(i):
    with con:
        cur = con.cursor()
        query = ('''INSERT INTO cadastroBeneficio (nome,data,beneficio,operacao) VALUES(?,?,?,?)''')
        cur.execute(query, i)



def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM cadastroBeneficio"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista



"""
with con:
    cur = con.cursor()
    query = '''UPDATE cadastroBeneficio SET operacao=? WHERE nome = ?'''
    cur.execute(query,lista)

"""

"""
Tentei excluir com duas condições na qual uma delas é a data mas não consegui. Com uma está funcionando tranquilamente
Mas troquei a condição data e coloquei a condição  operacao e deu certo
"""
#lista = ['Elizabete Maria', 'Suspensão']
def exluir_info(lista):
    with con:
        cur = con.cursor()
        query = '''DELETE FROM cadastroBeneficio WHERE nome = ? AND operacao = ?'''
        cur.execute(query, lista)

#exluir_info(lista)
#print(mostrar_info())