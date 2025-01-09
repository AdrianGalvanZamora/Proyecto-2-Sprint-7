import pandas as pd
import plotly_express as px
import streamlit as st

try:
    car_data = pd.read_csv('Proyecto_2_Sprint_7/Proyecto-2-Sprint-7/data/vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo vehicles_us.csv no se encontró. Asegúrate de que esté en el directorio correcto.")
    st.stop()  # Detiene la ejecución de la app si no se encuentra el archivo
except pd.errors.ParserError:
    st.error("Error: No se pudo analizar el archivo CSV. Verifica su formato.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error inesperado: {e}")
    st.stop()

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

