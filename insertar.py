import connect

def insert():
    #SENTENCIA SQL
    sql='INSERT INTO personas (nombre,apellido,edad) VALUES(%s,%s,%s)'

    #solicitud noms
    nombre=input('nom:')
    apellido=input('cognom: ')
    edad=input('edat: ')

    #recolecció
    datos=(nombre,apellido,edad)

    connect.cur.execute(sql,datos)

    connect.conn.commit()

    registros=connect.cur.rowcount

    print(f'Registre insertat: {registros}')

    connect.cur.close()
    connect.conn.close()