import psycopg2
import pandas as pd
try:
    connection=psycopg2.connect(
        host= 'LocalHost',
        user= 'postgres',
        database='postgres')
    print(1)
    cursor=connection.cursor()
    cursor.execute('''create table Pelicula(
	Id integer not null,
	Titulo character(100),
	Fecha_lanzamiento date,
	Tiempo_ejecucion integer,
	adulto bool,
	Ganancia bigint,
	Estado character(20),
	primary key (id));''')
    df= pd.read_excel('/home/jsdinge/Proyecto ing datos/Datos_peliculas (1).xlsx')
    l=[]
    
    for index, row in df.iterrows():
        if type(row['release_date']) != float and type(row['release_date']) != str :
            release_date = row['release_date'].strftime('%Y-%m-%d')
            title= str(row['title']).replace("'", '`')
            cursor.execute("INSERT INTO pelicula values({}, '{}', '{}', '{}', {}, {}, '{}')".format(row['id'], title, release_date, row['runtime'], row['adult'], row['revenue'], row['status']))
    

    
    
except Exception as ex:
    print(ex)
finally:
    connection.commit()
    cursor.close()
    connection.close()
    print(2)
