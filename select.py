import connect

def select():
    #sentencia sql
    sql='SELECT * FROM personas WHERE id_persona=%s'

    #executar sentencia sql
    id_persona=input('id del registre que vols mostrar: ')

    #guardar resultat a variable registro
    connect.cur.execute(sql,id_persona)

    registro=connect.cur.fetchone()

    #output
    print(registro)

    #tancar connexio
    connect.cur.close()
    connect.conn.close()
