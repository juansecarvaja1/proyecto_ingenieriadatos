

import dash
from dash import dcc, html
import plotly.express as px
import psycopg2


connection = psycopg2.connect(
    host='LocalHost',
    user='postgres',
    database='postgres'
)
cursor = connection.cursor()


cursor.execute('''SELECT genero, COUNT(*) AS cantidad
                  FROM Genero
                  GROUP BY genero;''')
rows = cursor.fetchall()


labels, values = zip(*rows)
labels_cleaned = [label.replace(' ', '') for label in labels]


r1 = px.bar(x=labels_cleaned, y=values, labels={'x': 'Género', 'y': 'Número de Películas'},
             title='Número de Películas por Género')

cursor.execute('''SELECT lenguaje, COUNT(*) AS cantidad
    FROM lenguajes_hablados
    GROUP BY lenguaje
    ORDER BY cantidad DESC;
    ''')

rows = cursor.fetchall()

labels, values = zip(*rows)
labels_cleaned = [label.replace(' ', '') for label in labels]

r2 = px.pie(names=labels_cleaned, values=values, title='Distribución de Géneros')
r2.update_traces(textinfo='none') 


cursor.execute('''
    SELECT EXTRACT(YEAR FROM Fecha_lanzamiento) AS Año, COUNT(*) AS Cantidad
    FROM Pelicula
    GROUP BY Año
    ORDER BY Año;
''')

rows = cursor.fetchall()

labels, values = zip(*rows)

r3 = px.bar(x=labels, y=values, labels={'x': 'a;o ', 'y': 'peliculas'},
             title='Número de Películas por Género')



cursor.execute('''
    SELECT genero AS Genero, SUM(Popularidad) AS Popularidad_Total
    FROM Genero
    JOIN Op_publica ON Genero.Id_pelicula = Op_publica.Id_pelicula
    GROUP BY genero
''')


rows = cursor.fetchall()

labels, values = zip(*rows)

r4 = px.bar(x=labels, y=values, labels={'x': 'a;o ', 'y': 'peliculas'},
             title='Número de Películas por Género')


r1.show()

r2.show()

r3.show()

r4.show()

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Diseño de la aplicación
app.layout = html.Div([
    dcc.Graph(figure=r1),
    html.H3("analisis Sebastian"),
    html.Div("podemos ver como drama tiene la mayor cantidad de peliculas con 1099, en lugares siguientes podemos ver a accion, thriller y comedia con un numero de peliculas entre 782 y 868, tambien podemos ver que pelicula TV es la que menos peliculas ha sacado con solo 6 peliculas"),
    html.H3("analisis Andres"),
    html.Div("Las compañías evalúan producciones ya lanzadas para tener una idea de que genero podría llegar a impactar mas a la población en general, dejando como resultado que para cubrir el mayor rango de publico y salir beneficiados de ello deciden lanzar peliculas cuya trama se base en el drama, la comedia, la accion o el suspenso."),
    dcc.Graph(figure=r2, style={'height': '80vh'}, config={'displayModeBar': False}),
    html.H3("analisis Sebastian"),
    html.Div("El inglés es predominante, mostrando el dominio de EE. UU. También vemos representacion de el francés y español, dando asi que el resto de lenguas no romances no tienen tanta representacion"),
    html.H3("analisis Andres"),
    html.Div("En la grafica de pastel se puede notar un gran dominio del idioma inglés en las películas lanzadas diría yo por el hecho de que las mayores productoras cinematográficas son estadounidenses, como lo serian Pixar, Universal Pictures, 20th century studios, walt Disney studios, Warner Bros, etc. Estas dominan el mercado cinematográfico por sus reconocidas películas que han marcado la infancia de muchas personas y sus productos son muy consumidos por las personas del mismo país."),
    dcc.Graph(figure=r3, style={'height': '100vh'}, config={'displayModeBar': False}),
    html.H3("analisis Sebastian"),
    html.Div("La cantidad de películas estrenadas por año fue casi nula desde 1940, por el hecho de que en pleno siglo XX las comunicaciones y formas de entretenimiento se basaban en emisiones radiales, programas a blanco y negro y/o metodologías mas convencionales, en esta época no se había explorado tanto el mundo del séptimo arte por lo que las personas se divertían viendo las noticias desde la comodidad de su casa."),
    html.H3("analisis Andres"),
    html.Div("De esta grafica de barras puedo concluir que el crecimiento en la producción de películas que se dio a partir de los años 2000, se debe al avance tecnológico que ha presentado las compañías a la hora de iniciar un nuevo largometraje, esto hizo que los tiempos de"),
    dcc.Graph(figure=r4, style={'height': '100vh'}, config={'displayModeBar': False}),
    html.H3("analisis Sebastian"),
    html.Div("Esta grafica es muy similar a la primera que se mostró, lo cual de cierta forma complementa y respalda la gran cantidad de películas estrenadas por género, ya que si comparamos números de la cantidad de personas que ven mas llamativa una película de acción antes que un documental, veremos que son dos extremos totalmente distintos que dan una idea de los gustos de la población y sus intereses en general."),
    html.H3("analisis Andres"),
    html.Div("De la grafica podemos deducir que la categoría de TV movie es la menos popular, seguido de Western, Documental y War, lo cual podemos intuir que se podría tratar  lo extensas que pueden llegar a ser estos tipos de películas, bien sea por la gran contextualización que estas pueden llevar o por otro lado lo poco llamativa que puede ser la trama en la cual se basen."),
])


if __name__ == '__main__':
    app.run_server(debug=True)