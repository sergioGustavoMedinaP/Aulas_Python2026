import sqlite3
import io

conn = sqlite3.connect('bd_clientes.db')

with io.open('bd_clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)

print('Backup realizado com sucesso.')
print('Salvo como clientes_dump.sql')

conn.close()
