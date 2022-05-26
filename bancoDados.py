import sqlite3



# Criando conexão
con = sqlite3.connect('dados.db')

# conectando ao banco de dados
with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE cadastroBeneficio
                   (nome TEXT, data date, beneficio TEXT, operacao TEXT)''')