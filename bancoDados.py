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

def exluir_info(name):
    with con:
        cur = con.cursor()
        query = '''DELETE FROM cadastroBeneficio WHERE nome = ?'''
        cur.execute(query, name)



