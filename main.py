import streamlit as st

st.set_page_config(page_title="Portfolio Distance Delivery",
                   layout="wide", page_icon=":rocket:")
#st.title('Portofolio Distance Food Delivery')
#st.title("Portfolio Saya")
#st.header("Data Scientist & Developer")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["About Project", "EDA", "Machine Learning"])

if page == 'About Project':
    import introduction
    introduction.project()
elif page == 'EDA':
    import exploration
    exploration.eksplorasi_data()
elif page == 'Machine Learning':
    import prediksi
    prediksi.predict()