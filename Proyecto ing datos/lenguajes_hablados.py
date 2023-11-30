#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:27:38 2023

@author: jsdinge
"""

import psycopg2
import pandas as pd
try:
    connection=psycopg2.connect(
        host= 'LocalHost',
        user= 'postgres',
        database='postgres')
    print(1)
    cursor=connection.cursor()
    cursor.execute('''CREATE table lenguajes_hablados (
    Id_pelicula integer,
    lenguaje character(50),
    	FOREIGN key (Id_pelicula) REFERENCES info_especial (Id_pelicula));''')
    df= pd.read_excel('/home/jsdinge/Proyecto ing datos/Datos_peliculas (1).xlsx')
    l=[]
    
    for index, row in df.iterrows():
        if type(row['spoken_languages'])==str and type(row['id'])==int:
            lenguajes_list = row['spoken_languages'].split(', ')
            for lenguaje in lenguajes_list:
                cursor.execute("INSERT INTO lenguajes_hablados VALUES ({}, '{}');".format(row['id'], lenguaje))
        
    
except Exception as ex:
    print(ex)
finally:
    connection.commit()
    cursor.close()
    connection.close()
    print(2)