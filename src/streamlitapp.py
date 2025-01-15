import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import sqlite3
'''
Explicación:
Conexión y creación de tablas: Se establece una conexión a la base de datos y se crean las tablas necesarias.
Formulario: Se crea un formulario para recolectar los datos del usuario.
Inserción de datos: Al enviar el formulario, los datos se insertan en la base de datos.
Clustering: Se carga un DataFrame con los datos relevantes, se aplica K-Means y se asignan etiquetas.
Etiqueta del usuario: Se obtiene la última etiqueta, que corresponde al usuario recién agregado.
Personalizaciones:

Número de clusters: Ajusta n_clusters en KMeans según tus necesidades.
Características: Agrega más campos al formulario y a las tablas para incluir más características en el clustering.
Visualización: Utiliza st.pyplot para visualizar los clusters.
Base de datos: Puedes usar otras bases de datos como PostgreSQL o MongoDB.
Modelos de clustering: Explora otros algoritmos como DBSCAN o Hierarchical Clustering.
Preprocesamiento de datos: Realiza escalado, normalización o transformación de los datos antes de aplicar K-Means.
Consideraciones:

Escalabilidad: Para grandes conjuntos de datos, considera usar una base de datos más robusta y optimizar el código.
Interpretabilidad de clusters: Analiza las características de cada cluster para darles una interpretación significativa.
Validación: Evalúa la calidad del clustering utilizando métricas como el índice de silueta.
Ampliaciones:

Interfaz más sofisticada: Utiliza componentes de Streamlit como selectores, deslizadores, etc. para crear una interfaz más interactiva.
Personalización de clusters: Permite al usuario elegir el número de clusters o seleccionar características específicas para el clustering.
Integración con otras herramientas: Conecta Streamlit con herramientas de visualización como Plotly o Tableau.
Este es un punto de partida sólido. Puedes adaptarlo y ampliarlo según tus necesidades específicas y el nivel de complejidad que desees alcanzar.
'''
# Conexión a la base de datos (ajusta según tu configuración)
conn = sqlite3.connect('tablas.db')

# Función para crear tablas si no existen
def create_tables():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            # ... otras columnas
        )
    ''')
    # Crear otras tablas según tus necesidades

# Función para insertar datos en las tablas
def insert_data(data):
    cursor = conn.cursor()
    # Insertar datos en la tabla users
    cursor.execute('''
        INSERT INTO users (name, age, ...) VALUES (?, ?, ...)
    ''', data)
    # Insertar datos en otras tablas

# Función para realizar el clustering
def perform_clustering(data):
    # Cargar datos relevantes para el clustering
    df = pd.read_sql_query("SELECT * FROM users", conn)
    # Aplicar K-Means
    kmeans = KMeans(n_clusters=3)  # Ajusta el número de clusters
    kmeans.fit(df)
    # Asignar etiquetas
    labels = kmeans.labels_
    return labels

# Interfaz de usuario
st.title("Formulario de registro y clustering")

with st.form("my_form"):
    name = st.text_input("Nombre")
    age = st.number_input("Edad")
    # ... otros campos
    submitted = st.form_submit_button("Enviar")

if submitted:
    # Insertar datos en la base de datos
    data = (name, age, ...)
    insert_data(data)

    # Realizar clustering y asignar etiqueta
    labels = perform_clustering(data)
    user_label = labels[-1]  # Última etiqueta corresponde al nuevo usuario
    st.write(f"El usuario {name} pertenece al cluster {user_label}")

conn.close()