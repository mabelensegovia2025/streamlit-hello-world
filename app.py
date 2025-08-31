import streamlit as st

st.title("Hello World from Streamlit!")
st.write("Este es mi primer despliegue en Streamlit Community Cloud")

nombre = st.text_input("Escribe tu nombre:")
if nombre:
    st.success(f"¡Hola, {nombre}! Bienvenido a mi app en la nube")
