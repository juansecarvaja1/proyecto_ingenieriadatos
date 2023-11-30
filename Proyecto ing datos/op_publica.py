import psycopg2
import pandas as pd
try:
    connection=psycopg2.connect(
        host= 'LocalHost',
        user= 'postgres',
        database='postgres')
    print(1)
    cursor=connection.cursor()
    cursor.execute('''create table Op_publica(
	Voto_promedio float,
	Recuento_votos integer,
	Popularidad float,
	Id_pelicula integer,
	primary key	(Id_pelicula),
	FOREIGN key (Id_pelicula) REFERENCES Pelicula (Id));''')
    df= pd.read_excel('/home/jsdinge/Proyecto ing datos/Datos_peliculas (1).xlsx')
    l=[]
    
    for index, row in df.iterrows():
        if type(row['id']) == float:
            break
        elif type(row['popularity']) == float:
            cursor.execute("INSERT INTO Op_publica values({}, {}, NULL, {}); \n".format(row['vote_average'], row['vote_count'], row['id']))

        
        else:
            cursor.execute("INSERT INTO Op_publica values({}, {}, {}, {}); \n".format(row['vote_average'], row['vote_count'], row['popularity'], row['id']))

    
    
except Exception as ex:
    print(ex)
finally:
    connection.commit()
    cursor.close()
    connection.close()
    print(2)
