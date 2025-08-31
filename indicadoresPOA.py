import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Calculadora de Indicadores", layout="centered")

st.title("📊 Calculadora de Indicadores Automáticos")

# Subir archivo
archivo = st.file_uploader("Sube tu archivo Excel o CSV", type=["csv", "xlsx"])

if archivo:
    # Leer el archivo
    if archivo.name.endswith('.csv'):
        df = pd.read_csv(archivo, encoding="utf-8", sep=",")
    else:
        df = pd.read_excel(archivo)

    st.subheader("📁 Datos cargados")
    st.dataframe(df, use_container_width=True)

    # Calcular indicadores estadísticos básicos
    indicadores = df.describe().T[["mean", "std", "min", "max"]]
    indicadores.rename(columns={
        "mean": "Promedio",
        "std": "Desviación estándar",
        "min": "Mínimo",
        "max": "Máximo"
    }, inplace=True)

    st.subheader("📈 Indicadores Calculados")
    st.dataframe(indicadores, use_container_width=True)

    # Convertir a Excel para exportar
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        indicadores.to_excel(writer, sheet_name='Indicadores')
        df.to_excel(writer, sheet_name='Datos Originales', index=False)
    output.seek(0)

    # Botón para descargar
    st.download_button(
        label="⬇️ Descargar indicadores en Excel",
        data=output,
        file_name="indicadores.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

