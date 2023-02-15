import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regression = data["model"]



def show_predict_page():
    st.title("Yarn Properties Prediction from Fibre Properties")

    st.write("""### We need some information for Prediction""")

   
    A = st.number_input(label="2.5% span length (mm)",step=1.,format="%.2f")
    B = st.number_input(label="UR (%)",step=1.,format="%.2f")
    C = st.number_input(label="Fineness (ug/inch)",step=1.,format="%.2f")
    D = st.number_input(label="Bundle Strength (cN/tex)",step=1.,format="%.2f")
    E = st.number_input(label="Trash content (%)",step=1.,format="%.2f")


    ok = st.button("Calculate Yarn Count (tex)")
    ok1 = st.button("Calculate CSP")
    
    if ok:
        x = np.array([[A,B,C,D,E]])     
        Count = regression.predict(x)
        st.subheader(f"The estimated count is {Count[0]:.8f}")
    
    
    if ok1:
        x = np.array([[A,B,C,D,E]])     
        Count = regression.predict(x)
        st.subheader(f"The estimated CSP is {Count[0]:.8f}")
