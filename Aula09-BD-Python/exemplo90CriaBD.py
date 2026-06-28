import sqlite3      # 02_create_schema.py

conn = sqlite3.connect('bd_Clientes.db')   # conectando...

cursor = conn.cursor()    # definindo um cursor

# criando a tabela (schema)
cursor.execute("""
        CREATE TABLE tb_clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
        );
        """)

print('Tabela criada com sucesso.')
conn.close()     # desconectando...
