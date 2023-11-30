
import psycopg2
import pandas as pd
try:
    connection=psycopg2.connect(
        host= 'LocalHost',
        user= 'postgres',
        database='postgres')
    print(1)
    cursor=connection.cursor()
    cursor.execute('''CREATE table Genero (
    Id_pelicula integer,
    genero character(50),
	FOREIGN key (Id_pelicula) REFERENCES Pelicula (Id));''')
    df= pd.read_excel('/home/jsdinge/Proyecto ing datos/Datos_peliculas (1).xlsx')
    l=[]
    
    for index, row in df.iterrows():
        if type(row['genres'])==str and type(row['id'])==int:
            genre_list = row['genres'].split(', ')
            for genre in genre_list:
                cursor.execute("INSERT INTO Genero VALUES ({}, '{}');".format(row['id'], genre))
        
    
except Exception as ex:
    print(ex)
finally:
    connection.commit()
    cursor.close()
    connection.close()
    print(2)