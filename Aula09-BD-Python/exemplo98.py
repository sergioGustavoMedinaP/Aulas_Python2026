import sqlite3
import io

conn = sqlite3.connect('tb_clientes_recuperado.db')
cursor = conn.cursor()

f = io.open('tb_clientes_dump.sql', 'r')
sql = f.read()
cursor.executescript(sql)

print('Banco de dados recuperado com sucesso.')
print('Salvo como clientes_recuperado.db')

conn.close()
