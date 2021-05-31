import sqlite3
from faker import Faker


fake = Faker()

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()


for _ in range(300):
    nome = (fake.name()).split()[0]
    sobrenome = (fake.name()).split()[1]

    cur.execute(f'INSERT INTO home_contato (nome, sobrenome, telefone, email, descricao, categoria_id, data_criacao) VALUES ("{nome}", "{sobrenome}", "{fake.phone_number()}", "{fake.email()}", "{fake.text()}", 1, datetime("now"))')
    con.commit()

