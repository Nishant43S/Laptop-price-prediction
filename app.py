import streamlit as st

laptop_price_prediction = st.Page(
    page="laptop_price_prediction.py",
    title="Laptop price Prediction",
    icon=":material/manufacturing:",
    default=True
)


about_app = st.Page(
    page="about_app.py",
    title="About App",
    icon=":material/person:"
)

pg = st.navigation(
    pages=[laptop_price_prediction,about_app],
    expanded=False,position="sidebar"
)
pg.run()

st.sidebar.write("**Created By - Nishant Maity**")
st.sidebar.link_button(
    label="Project Source Code",
    use_container_width=True,
    url="https://github.com/Nishant43S/Laptop-price-prediction.git",
    icon=":material/code:"
)