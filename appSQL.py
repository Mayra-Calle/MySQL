import mysql.connector    
import pandas as pd
import streamlit as st
import plotly.express as px

#Conectar a mysql
conexion = mysql.connector.connect(
    host="localhost",       
    user="root",
    password="Martin$0119",
    database="bd_lavadora"
)

#Crear cursor
cursor = conexion.cursor()

#Consultar los datos de la tabla clientes mostrar en un dataframe
cursor.execute("SELECT * FROM cliente")
resultados=cursor.fetchall()
df=pd.DataFrame(resultados,columns=[i[0]for i in cursor.description])
st.title("Datos de Clientes")
st.dataframe(df)

#leer directamente desde mysql a un dataframe
df_mysql=pd.read_sql("SELECT * FROM cliente",conexion)
st.title("Datos de Clientes desde MySQL a DataFrame")
st.dataframe(df_mysql)

df_productos=pd.read_sql("SELECT * FROM producto",conexion)
st.title("Datos de Productos desde MySQL a DataFrame")
st.dataframe(df_productos)

df_proveedores=pd.read_sql("SELECT * FROM proveedor",conexion)
st.title("Datos de Proveedores desde MySQL a DataFrame")
st.dataframe(df_proveedores)

if conexion.is_connected():
    st.success("Conexión a MySQL exitosa")
    df=pd.read_sql("SELECT * FROM cliente",conexion)
    st.dataframe(df)
    df_localidad=df.groupby("localidad").size().reset_index(name="cantidad")
    st.dataframe(df_localidad)
    fig=px.bar(df_localidad,x="localidad",y="cantidad",title="Cantidad de Clientes por Localidad")
    st.plotly_chart(fig)

    df_productos=pd.read_sql("SELECT * FROM producto",conexion)
    st.header("Datos de Productos")
    st.dataframe(df_productos)
    fig_productos=px.bar(df_productos,x="nombre",y="costo",title="Productos vs Costo")
    st.plotly_chart(fig_productos)
    st.title("Comandos básicos de MySQL")
    st.dataframe(df.head())
    st.dataframe(df.tail())
    st.dataframe(df.info())
    st.dataframe(df.describe())
    print(df.info)
    st.write("Informacion del DataFrame:", df.info())
    st.write("Numero de filas y columnas:", df.shape)
    st.write("Nombres de las columnas:", df.columns)
    st.dataframe(df.describe())
    st.write("Valores nulos:", df.isnull().sum())
    st.write("Tipos de datos de las columnas:", df.dtypes)
    st.write("Valores duplicados clientes:", df.duplicated().sum())
    st.write("Valores duuplicados productos:", df_productos.duplicated().sum())


else:
    st.error("Error al conectar a MySQL")


