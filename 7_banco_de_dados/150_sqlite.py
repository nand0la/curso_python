import sqlite3
   
conexao = sqlite3.connect("base_dados.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL
);
""")

while True:
    inserir = input('Deseja Inserir dados na Base de dados? [Y] [N] ')
    print()

    if inserir.lower() == 'y':
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        print()

        cursor.execute(f'INSERT INTO clientes (nome, cpf) VALUES ("{nome}", "{cpf}")')
        conexao.commit()

    else:
        break

cursor.close()
conexao.close()