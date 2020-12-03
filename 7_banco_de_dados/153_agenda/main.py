import sqlite3

class AgendaDB:
    def __init__(self, nome_arquivo):
        self.conn = sqlite3.connect(nome_arquivo)
        self.cursor = self.conn.cursor()

    def insert_contato(self, nome, numero):
        consulta = "INSERT OR IGNORE INTO contatos (nome, numero) VALUES (?, ?)"
        self.cursor.execute(consulta, (nome, numero))
        self.conn.commit()

    def delete_contato(self, ids):
        self.cursor.execute("DELETE FROM contatos WHERE id=?", (ids))
        self.conn.commit()

    def update_contate(self, ids, nome, numero):
        self.cursor.execute("UPDATE contatos SET nome=?, numero=? WHERE id=?", (nome, numero, ids))

    def listar(self):
        self.cursor.execute("SELECT * FROM contatos")

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    agenda1 = AgendaDB("agenda_igreja.db")
    agenda1.insert_contato("Fernando", "123345")
    agenda1.insert_contato("Caua", "32132")
    agenda1.insert_contato("Andre", "432234")
    agenda1.insert_contato("Ana", "412312")
    agenda1.insert_contato("Julie", "654456")

    agenda1.update_contate(1, "Jose", "4324355")

    agenda1.fechar()