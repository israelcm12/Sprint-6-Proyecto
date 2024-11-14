import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear casillas de verificación para el histograma y el gráfico de dispersión
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Construir y mostrar el histograma si la casilla de verificación está seleccionada
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Construir y mostrar el gráfico de dispersión si la casilla de verificación está seleccionada
if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre el kilometraje y el precio")
    st.plotly_chart(fig, use_container_width=True)

