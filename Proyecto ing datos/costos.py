
import psycopg2
import pandas as pd
try:
    connection=psycopg2.connect(
        host= 'LocalHost',
        user= 'postgres',
        database='postgres')
    print(1)
    cursor=connection.cursor()
    cursor.execute('''create table Costos(
	Id_compañia integer,
	Compañia_de_produccion character(100),
	Ganancia bigint,
	primary key (Id_compañia));''')
    df= pd.read_excel('/home/jsdinge/Proyecto ing datos/Datos_peliculas (1).xlsx')
    l=[]
    for index, row in df.iterrows():
        if type(row['production_companies']) != float:
            p = row['production_companies'].replace("'", "").split(', ')
            match_found = False  # Flag to track if any item has a coincidence
            missing_items = []  # List to store items without a coincidence
        
            for x in p:
                found_match = False  # Flag to track if the current item has a coincidence
                for i, sublist in enumerate(l):
                    if x in sublist:
                        l[i][1] += row['revenue']
                        break
                        found_match=True
                if not found_match:
                    missing_items.append(x)
        
            
            # Add a new sublist only if every item in the list has no coincidence
            for x in missing_items:
                l.append([x, row['revenue']])
    it=0
    for x, y in l:
        if type(y)!= str and y>0:
            cursor.execute("INSERT INTO Costos values({}, '{}', {}); \n".format(it, x, y))
            it+=1
    
    
except Exception as ex:
    print(ex)
finally:
    connection.commit()
    cursor.close()
    connection.close()
    print(2)
