import streamlit as st

st.title("🎈 GeoCal: Cálculo de propiedades de secciones planas")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

cantidad = st.slider("Selecciona una cantidad: ")
st.write(f"La cantidad seleccionada es: {cantidad}")

for i in range(cantidad):
    st.button(f"{i}")