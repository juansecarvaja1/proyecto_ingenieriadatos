
import psycopg2
import pandas as pd
try:
    connection=psycopg2.connect(
        host= 'LocalHost',
        user= 'postgres',
        database='postgres')
    print(1)
    cursor=connection.cursor()
    cursor.execute('''create table info_especial(
	pagina_principal character(150),
	imbd_id character(100),
	idioma_original character(100),
	Id_pelicula integer,
    titulo_original character(100),
    ruta_telon_fondo character(150),
    ruta_poster character(150),
    presupuesto integer,
	primary key	(Id_pelicula),
	FOREIGN key (Id_pelicula) REFERENCES Pelicula (Id));''')
    df= pd.read_excel('/home/jsdinge/Proyecto ing datos/Datos_peliculas (1).xlsx')
    l=[]
    
    for index, row in df.iterrows():
        if type(row['id']) == float:
            break
        ot=str(row['original_title']).replace("'", '`')
        cursor.execute("INSERT INTO info_especial VALUES ('{}', '{}', '{}', {}, '{}', '{}', '{}', {});".format(
    row['homepage'],
    row['imdb_id'],
    row['original_language'],
    row['id'],
    ot,
    row['backdrop_path'],
    row['poster_path'],
    row['budget']
))
        

    
    
except Exception as ex:
    print(ex)
finally:
    connection.commit()
    cursor.close()
    connection.close()
    print(2)