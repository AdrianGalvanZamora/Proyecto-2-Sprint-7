import pandas as pd
import plotly_express as px
import streamlit as st
import os

def cargar_datos():
    ruta_archivo = os.path.join("data", "vehicles_us.csv")
    try:
        car_data = pd.read_csv(ruta_archivo)
        return car_data
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en: {ruta_archivo}")
        return None

datos = cargar_datos()
if datos is not None:
    print(datos.head())

st.header('Análisis Exploratorio de Datos de Anuncios de Coches')

build_histogram = st.checkbox('Construir Histograma')
build_scatter = st.checkbox('Construir Gráfico de Dispersión')

if build_histogram:
    st.write('Creando un histograma para la columna odómetro')
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma del Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.write('Creando un gráfico de dispersión entre odómetro y precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odómetro vs. Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)