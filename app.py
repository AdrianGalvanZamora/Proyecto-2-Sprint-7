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

# Casillas de verificación
show_histogram = st.checkbox('Mostrar histograma del odómetro')
show_scatter = st.checkbox('Mostrar diagrama de dispersión entre odómetro y precio')
show_box = st.checkbox('Mostrar diagrama de cajas del precio por tipo de vehículo')
show_manufacturer_bar = st.checkbox('Mostrar gráfico de barras de cantidad de vehículos por fabricante')
show_facet_histogram = st.checkbox('Mostrar histograma del odómetro por tipo de vehículo')

# Generación de gráficos según las casillas seleccionadas
if show_histogram:
    st.write('Creando un histograma para el odómetro de los anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('Creando un diagrama de dispersión entre el odómetro y el precio de los anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="year", trendline="ols", hover_data=['model','manufacturer'])
    st.plotly_chart(fig_scatter, use_container_width=True)

if show_box:
    st.write('Creando un diagrama de cajas del precio por tipo de vehículo')
    fig_box = px.box(car_data, x="type", y="price")
    st.plotly_chart(fig_box, use_container_width=True)

if show_manufacturer_bar:
    st.write('Creando un gráfico de barras de cantidad de vehículos por fabricante')
    manufacturer_counts = car_data['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['manufacturer', 'count']
    fig_bar = px.bar(manufacturer_counts, x='manufacturer', y='count')
    st.plotly_chart(fig_bar, use_container_width=True)

if show_facet_histogram:
    st.write('Creando un histograma del odómetro por tipo de vehículo')
    fig_facet = px.histogram(car_data, x="odometer", facet_col="type")
    st.plotly_chart(fig_facet, use_container_width=True)